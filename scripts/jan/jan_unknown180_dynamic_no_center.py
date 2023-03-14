#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 30
  detector: H1
  mass: 34.2
  settling_time: 25
default_fits: nominal_linear
equilibration:
  eqtime: 1.0
  inlet: S
  inlet_delay: 3
  outlet: O
  use_extraction_eqtime: true
  post_equilibration_delay: 3
multicollect:
  counts: 180
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  detectors:
  - H1
  - AX
  - CDD
  isotope: Ar40
  integration_time: 0.262144
peakhop:
  hops_name: ''
  use_peak_hop: false
'''
ACTIVE_DETECTORS=('H2','H1','AX','L1','L2','CDD')

def main():
    info('unknown measurement script')

    activate_detectors(*ACTIVE_DETECTORS)


    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)

    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=mx.baseline.settling_time)

    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #sniff the gas during equilibration
    if mx.equilibration.use_extraction_eqtime:
        eqt = eqtime
    else:
        eqt = mx.equilibration.eqtime
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    equilibrate(eqtime=eqt, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet,
               delay=mx.equilibration.inlet_delay)
    set_time_zero()

    sniff(eqt)
    set_fits()
    set_baseline_fits()

    # delay to migitate 39Ar spike from inlet valve close
    sleep(mx.equilibration.post_equilibration_delay)

    #multicollect on active detectors
    multicollect(ncounts=mx.multicollect.counts, integration_time=1)

    if mx.baseline.after:
        # set the default counts to be the values pulled from header section, lines 3-9
        ncounts = mx.baseline.counts
        settling_time = mx.baseline.settling_time
        
        # setup your dynamic baseline conditions here
        ar40intensity = get_intensity('H1')
        if ar40intensity < 100:
            settling_time = 7
        elif ar40intensity < 300:
            settling_time = 10
        elif ar40intensity < 700:
            settling_time = 15
        elif ar40intensity > 5000:
            settling_time = 60
        
        baselines(ncounts=ncounts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=settling_time)
    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope,
                    integration_time=mx.peakcenter.integration_time)
    else:
        position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector, for_collection=False)
    if use_cdd_warming:
       gosub('warm_cdd', argv=(mx.equilibration.outlet,))

    info('finished measure script')
