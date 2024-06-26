#===============================================================================
# EXTRACTION SCRIPT felix_diode_no_cold_finger.py
#===============================================================================
'''
eqtime: 25
modifier: 01
'''

def main():

    info('Felix unknown laser analysis')
    
    set_motor('beam',beam_diameter)
    
    gosub('felix:PrepareForDiodeAnalysis')


    close(name="C", description="Bone to Turbo")

    close(name="D", description="Bone to CO2 Laser")
    close(name="E", description="Bone to Minibone")

 
    #gosub('felix:IsolateDiodeColdfinger')

    #open(name="B", description="Bone to Diode Laser")

    
    '''
    keep pumping bone while cold finger isolated
    '''
    
    #open(description='Bone to Turbo')
  
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
        with video_recording('{}/{}'.format(load_identifier, run_identifier)):
            enable()
            for pi in position:
                ''' 
                position the laser at pi, pi can be an holenumber or (x,y)
                '''
                with lighting(55):
                    sleep(2)
                    move_to_position(pi)
                    sleep(2)

                do_extraction()
                if disable_between_positions:
                    extract(0)
            info('Diode laser disabled.')
            disable()
      
    #gosub('felix:EquilibrateThenIsolateDiodeColdfinger')    
    #open(name="B", description="Bone to Diode Laser")

    
    sleep(cleanup)

def do_extraction():
    
    info('begin interval')
    begin_interval(duration)
    
    if ramp_duration>0:
        info('ramping to {} at {}/s'.format(extract_value, ramp_rate, extract_units))
        ramp(setpoint=extract_value, duration=ramp_duration, period=0.5)
    else:
        extract(extract_value, extract_units)
    
    if pattern:
        info('executing pattern {}'.format(pattern))
        execute_pattern(pattern)
        
    complete_interval()
    
#def do_extraction():
#    
#    if ramp_rate>0:
#        '''
#        style 1.
#        '''
#        #               begin_interval(duration)
#        #               info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units)
#        #               ramp(setpoint=extract_value, rate=ramp_rate)
#        #               complete_interval()
#        '''
#        style 2.
#        '''
#        elapsed=ramp(setpoint=extract_value, rate=ramp_rate)
#        pelapsed=execute_pattern(pattern)
#        sleep(min(0, duration-elapsed-pelapsed))
#
#    else:
#        begin_interval(duration)
#        
#        info('set extract to {} ({})'.format(extract_value, extract_units))
#        extract()
#        sleep(2)
#
#        if pattern:
#            info('executing pattern {}'.format(pattern))
#            execute_pattern(pattern)
#
#        complete_interval()


#===============================================================================
# POST EQUILIBRATION SCRIPT felix_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')
    gosub('felix:PumpBone')
    if get_resource_value(name='FelixMiniboneFlag'):
        open('L')
        gosub('felix:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT felix_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='V', cancel_on_failed_actuation=False)
	