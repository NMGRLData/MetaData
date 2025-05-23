#===============================================================================
# EXTRACTION SCRIPT jan_air_x1_NP10C.py
#===============================================================================
'''
modifier: 01
eqtime: 12
'''
def main():
    info('Jan Air Script x1')
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    gosub('jan:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('jan:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    sleep(duration=10.0)
    close(name="Q", description="Quad Inlet")
    close(name="U", description="Microbone to Turbo")
    sleep(duration=2.0)
    open(name="L", description="Microbone to Minibone")
    sleep(duration=10.0)
    close(name="L", description="Microbone to Minibone")
    sleep(duration=2.0)
    close(name="K", description="Microbone to Getter NP-10C")
    sleep(duration=2.0)
    open(name="U", description="Microbone to Turbo")
    sleep(duration=15.0)
    close(name="U", description="Microbone to Turbo")
    sleep(duration=2.0)
    open(name="K", description="Microbone to Getter NP-10C")
    sleep(duration=5.0)


#===============================================================================
# POST EQUILIBRATION SCRIPT jan_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')

    if extract_device=="FusionsDiode" or extract_device=='NMGRLFurnace':
        info('Pump after Jan diode analysis')
        gosub('jan:PumpMicroBoneAfterDiodeAnalysis')
        gosub('jan:PumpMiniboneAfterDiodeAnalysis')
    else:
        gosub('jan:PumpMicrobone')
        v=get_resource_value(name='JanMiniboneFlag')
        info('get resource value {}'.format(v))
        if v:
            info('Pumping Minibone')
            gosub('jan:PumpMinibone')
        else:
            info('Not Pumping Minibone')

#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O', cancel_on_failed_actuation=False)
    
    # setup dynamic pumping
    # delay extra time of the ar40 intensity is greater than a set threshold
    
    ar40intensity = get_intensity('H1')
    if ar40intensity> 4900:
        sleep(20)
    elif ar40intensity>3000:
        sleep(10)