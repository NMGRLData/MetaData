#===============================================================================
# EXTRACTION SCRIPT jan_co2_whiff.py
#===============================================================================
'''
eqtime: 15
'''
def main():
    """
    The CO2 whiff script is the same as a normal co2 extraction script
    !except! for the last step

    instead of equilibrating with the mass spec back to the co2 chamber
    the chamber is isolated. If the whiff action is "run remainder" than
    equilibrate with the chamber
    """
    info('Jan CO2 laser analysis')
    gosub('jan:WaitForCO2Access')
    gosub('jan:PrepareForCO2Analysis')

    gosub('jan:CO2Analysis')

    # isolate chamber
    info('Isolating CO2 chamber for whiffing')
    close('T')    

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
    