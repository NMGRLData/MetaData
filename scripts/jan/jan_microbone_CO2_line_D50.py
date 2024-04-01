#===============================================================================
# EXTRACTION SCRIPT jan_microbone_CO2_line_D50.py
#===============================================================================
'''
eqtime: 15 
'''
def main():
    info('Jan microbone, CO2 line, D50 blank analysis')

    if analysis_type=='blank':
        info('is blank. not heating')
        '''
        sleep cumulative time to account for blank
        during a multiple position analysis
        '''
        
        close(name="L", description="Microbone to Minibone")
        close(name="A", description="CO2 Laser to Jan")
        open(name="T", description="Microbone to CO2 Laser")
        open(name="K", description="Microbone to Getter D-50")
        close(name="M", description="Microbone to Getter NP-10")
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

    if extract_device=="FusionsDiode":
        info('Pump after Jan diode analysis')
        gosub('jan:PumpMicroBoneAfterDiodeAnalysis')
        gosub('jan:PumpMiniboneAfterDiodeAnalysis')
    else:
        gosub('jan:PumpMicrobone')
        v=get_resource_value(name='JanMiniboneFlag')  
        info('get resource value {}'.format(v))
        if get_resource_value(name='JanMiniboneFlag'):
            gosub('jan:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O')
    