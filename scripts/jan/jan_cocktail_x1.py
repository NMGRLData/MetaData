#===============================================================================
# EXTRACTION SCRIPT jan_cocktail_x1.py
#===============================================================================
'''
modifier: 03
eqtime: 15
'''
def main():
    info("Jan Cocktail Pipette x1")
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    close(name="Q", description="Quad Inlet")
    gosub('jan:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('jan:PrepareForAirShotExpansion')
    #sleep(duration=2.0)
    #close(name="M", description="Microbone to Getter NP-10H")
    #sleep(duration=2.0)
    gosub('common:ExpandPipette1')

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
    if ar40intensity> 600:
        sleep(100)
    elif ar40intensity>3000:
        sleep(10)