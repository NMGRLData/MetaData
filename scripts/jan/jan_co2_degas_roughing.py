#===============================================================================
# EXTRACTION SCRIPT jan_co2_degas_roughing.py
#===============================================================================
    
def main():
    info('Jan CO2 laser degas')
    gosub('jan:WaitForCO2Access')
    
    #gosub('jan:PrepareForCO2Analysis')

    set_motor('beam',beam_diameter)

    '''
    this is the most generic what to move and fire the laser
    position is always a list even if only one hole is specified
    '''
       
    enable()
    for pi in position:
        ''' 
        position the laser at pi, pi can be an holenumber or (x,y)
        '''
        move_to_position(pi)
        sleep(1)
        #close(description='Microbone to Turbo')
        do_extraction()
        if disable_between_positions:
            end_extract()
    end_extract()
    disable()
        
    #sleep(cleanup)


def do_extraction():
    if ramp_duration>0:
        '''
        style 1.
        '''
#               begin_interval(duration)
#               info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units)
#               ramp(setpoint=extract_value, rate=ramp_rate)
#               complete_interval()
        '''
        style 2.
        '''
        elapsed=ramp(setpoint=extract_value, duration=ramp_duration)
        pelapsed=execute_pattern(pattern)
        sleep(min(0, duration-elapsed-pelapsed))

    else:
                
        
        begin_interval(duration)
        
        info('set extract to {}'.format(extract_value))
        extract(extract_value)
        sleep(2)
    
        if pattern:
            info('executing pattern {}'.format(pattern))
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
        if get_resource_value(name='JanMiniboneFlag'):
            gosub('jan:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O')
    