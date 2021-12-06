#===============================================================================
# EXTRACTION SCRIPT jan_air_x2.py
#===============================================================================
'''
modifier: 01
eqtime: 25
'''
def main():
    info('Jan Air Script x1')
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    gosub('jan:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('jan:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    gosub('common:FillPipette2')
    gosub('jan:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')

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
    