#!Measurement
'''
default_fits: nominal
equilibration:
  eqtime: 1.0
  inlet: H
  inlet_delay: 3
  outlet: V
  use_extraction_eqtime: true
multicollect:
  counts: 180
  detector: L2(CDD)
  isotope: Ar36
peakcenter:
  after: false
  before: false
  detector: L2(CDD)
  detectors:
  - H2
  - AX(CDD)
  - L2(CDD)
  isotope: Ar36
  integration_time: 1.048576
peakhop:
  hops_name: ''
  use_peak_hop: false
'''
ACTIVE_DETECTORS=('H2','H1','AX(CDD)','L1','L2(CDD)')
    
def main():
    info('unknown measurement script')
    
    activate_detectors(*ACTIVE_DETECTORS)
   
    
    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    
    
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
    
    #multicollect on active detectors
    multicollect(ncounts=mx.multicollect.counts, integration_time=1.048576)
    
  
    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope, 
                    integration_time=mx.peakcenter.integration_time,
                    config_name='CDD_on_36')

    if use_cdd_warming:
       gosub('warm_cdd', argv=(mx.equilibration.outlet,))    
       
    info('finished measure script')
    