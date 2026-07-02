#===============================================================================
# EXTRACTION SCRIPT jan_microbone.py
#===============================================================================
'''
modifier: 01
eqtime: 12 
'''
def main():
    info('Jan microbone blank analysis')

    if analysis_type=='blank':
        info('is blank. not heating')
        
        close(name="L", description="Microbone to Minibone")
        close(name="A", description="CO2 Laser to Jan")
        open(name="T", description="Microbone to CO2 Laser")
        close(name="K", description="Microbone to Getter NP-10C")
        close(name="M", description="Microbone to Getter NP-10H")
        open(name="S", description="Microbone to Inlet Pipette")
        sleep(duration=30.0)
        close(description='Microbone to Turbo')
        
        sleep(duration)
        sleep(cleanup)



    

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