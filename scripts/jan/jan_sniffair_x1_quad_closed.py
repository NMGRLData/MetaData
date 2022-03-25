#===============================================================================
# EXTRACTION SCRIPT jan_sniffair_x1_quad_closed.py
#===============================================================================
'''
modifier: 02
eqtime: 12
'''
def main():
    info("Jan Air Sniff Pipette x1")
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    close(name="Q", description="Quad Inlet")
    gosub('jan:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('jan:PrepareForAirShotExpansion')
    
    close('T')

    gosub('common:SniffPipette2')

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
        set_resource(name='CO2PumpTimeFlag', value=30)
        release('JanCO2Flag')
        
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
    
