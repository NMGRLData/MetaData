#===============================================================================
# EXTRACTION SCRIPT jan_diode.py
#===============================================================================
'''
eqtime: 15
'''

def main():

    info('Jan unknown diode laser analysis')
    
    set_motor('beam',beam_diameter)
    
    gosub('jan:PrepareForDiodeAnalysis')
 
    gosub('jan:IsolateDiodeColdfinger')
    
    '''
    keep pumping bone while cold finger isolated
    '''
    
    open(description='Bone to Turbo')
  
    if analysis_type=='blank':
        info('Blank Analyis. No laser heating')

        '''
        sleep cumulative time to account for blank
        during a multiple position analysis
        '''
        numPositions=len(position)

        sleep(duration*numPositions)
    else:
        info('Diodelaser enabled. Heating sample.')


        '''
        this is the most generic way to move and fire the laser
        position is always a list even if only one hole is specified
        '''
        enable()
        for pi in position:
            ''' 
            position the laser at pi, pi can be an holenumber or (x,y)
            '''
            move_to_position(pi)
            do_extraction()
            if disable_between_positions:
                extract(0)
        info('Diode laser disabled.')
        disable()
        
    gosub('jan:EquilibrateThenIsolateDiodeColdfinger')    
    
    sleep(cleanup)
    
    '''
    close Minibone to Bone to speed equilibration time
    then start pumping Bone
    '''
    close(description='Minibone to Bone')
    gosub('jan:PumpBoneAfterDiodeAnalysis')
   

def do_extraction():
    info('begin interval')

    begin_interval(duration)

    if ramp_duration>0:
        info(f"ramping to {extract_value} at {ramp_rate}/s units={extract_units}")
        ramp(setpoint=extract_value, duration=ramp_duration, period=0.5)
    else:
        extract(extract_value, extract_units)

    if pattern:
        info(f"executing pattern {pattern}")
        execute_pattern(pattern)
    
    complete_interval()


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
    
