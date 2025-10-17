#!Measurement
'''
'''
#counts

#baselines
BASELINE_COUNTS= 300
BASELINE_DETECTOR= 'H1'
BASELINE_MASS= 4.975
BASELINE_BEFORE= True
BASELINE_AFTER= True
BASELINE_SETTLING_TIME= 30

#equilibration
EQ_TIME= eqtime
INLET= 'R'
OUTLET= 'O'
EQ_DELAY= 3.0

ACTIVE_DETECTORS = ('H2','H1','AX','L1','L2','CDD')
FITS = ('Ar40H2:average_SEM','Ar40H1:average_SEM','Ar40AX:average_SEM','Ar40L1:average_SEM','Ar40L2:average_SEM','Ar40CDD:average_SEM')
BASELINE_FITS=('average_SEM',)

NCYCLES=2
GENERATE_ICMFTABLE=False

def main():
    info('unknown measurement script')

    # protect the CDD
    #set_deflection('CDD', 2000)
    activate_detectors(*ACTIVE_DETECTORS)

    hops=load_hops('hops/ic_mass28_hops.yaml')
    info(hops)
    define_hops(hops)
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    #equilibrate(eqtime=EQ_TIME, inlet=INLET, outlet=OUTLET, delay=EQ_DELAY)
    set_time_zero()

    #sniff the gas during equilibration
    #sniff(EQ_TIME-1)
    #sleep(EQ_TIME-1)
    set_fits(*FITS)
    set_baseline_fits(*BASELINE_FITS)

    sleep(0.5)
    mftable_name = 'mftablemass28'
    if GENERATE_ICMFTABLE:
        mftable_name = 'ic_mftable'
        generate_ic_mftable(('H1','AX','L2'), peak_center_config='ic_peakhop')
        set_time_zero()

    peak_hop(ncycles=NCYCLES, hops=hops, mftable=mftable_name)


    if BASELINE_AFTER:
        #necessary if peak hopping
        define_detectors('Ar41','H2')
        define_detectors('Ar40','H1')
        define_detectors('Ar39','AX')
        define_detectors('Ar38','L1')
        define_detectors('Ar37','L2')
        define_detectors('Ar36','CDD')

        baselines(ncounts=BASELINE_COUNTS,mass=BASELINE_MASS, detector=BASELINE_DETECTOR,
                  settling_time=BASELINE_SETTLING_TIME, use_dac=True)

    # unprotect CDD
    #set_deflection('CDD', 50)

    info('finished measure script')
