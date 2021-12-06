#===============================================================================
# EXTRACTION SCRIPT jan_co2_minibone.py
#===============================================================================
'''
modifier: 01
eqtime: 15
'''
def main():
    info('Jan CO2 laser analysis')
    gosub('jan:WaitForCO2Access')
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForCO2_minibone_Analysis')
    gosub('jan:CO2Analysis')

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
    open(name='O')
    