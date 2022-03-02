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
    gosub('jan:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('jan:PrepareForAirShotExpansion')
    #sleep(duration=2.0)
    #close(name="M", description="Microbone to Getter NP-10H")
    #sleep(duration=2.0)
    close('T')
    
    gosub('common:ExpandPipette1')

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
        #gosub('jan:PumpMicrobone')
        v=get_resource_value(name='JanMiniboneFlag')
        info('get resource value {}'.format(v))
        if v:
            info('Pumping Minibone')

            #close('I')
            #close('C')
            #close('Q')
            open('P')
            open('L')
            open('T')
            open('Q')
            open('M')

            close(description='Bone to Minibone')
            open(description='Minibone to Bone')         
            #close(description='Microbone to Minibone')
            
            #sleep(duration=1.0)
            open(description='Minibone to Turbo')
            #open(description='Quad Inlet')
            
            open('S')

            set_resource(name='MinibonePumpTimeFlag',value=30)
            sleep(duration=15.0)
            close(description="Outer Pipette 1")
            close(description="Outer Pipette 2")
            
            release('JanMiniboneFlag')

        else:
            info('Not Pumping Minibone')

#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O', cancel_on_failed_actuation=False)
    
