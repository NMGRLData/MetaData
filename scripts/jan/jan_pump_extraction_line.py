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
