#===============================================================================
# EXTRACTION SCRIPT jan_co2_microbone_only.py
#===============================================================================
'''
eqtime: 15
'''
def main():
    info('Jan CO2 laser analysis')
    gosub('jan:WaitForCO2Access')
    gosub('jan:PrepareForCO2Analysis')
    gosub('jan:CO2Analysis')
    close(name="T", description="Microbone to CO2 Laser")
    sleep(duration=5.0)
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
    
