#===============================================================================
# EXTRACTION SCRIPT jan_co2_video_ramp.py
#===============================================================================
'''
eqtime: 12
'''
def main():
    info('Jan CO2 laser analysis')
    gosub('jan:WaitForCO2Access')
    gosub('jan:PrepareForCO2Analysis')

    set_motor('beam',beam_diameter)

    cooldown = 2
    accum = 0
    if analysis_type=='blank':
        info('is blank. not heating')
        '''
        sleep cumulative time to account for blank
        during a multiple position analysis
        '''
        close(description='Microbone to Turbo')
        numPositions=len(position)

        sleep(duration*max(1,numPositions))
    else:

        '''
        this is the most generic what to move and fire the laser
        position is always a list even if only one hole is specified
        '''

        # make sure light is on before moving
        with grain_polygon():
            with video_recording('{}/{}'.format(load_identifier,run_identifier)):
                for i,pi in enumerate(position):
                    '''
                    position the laser at pi, pi can be a holenumber or (x,y)
                    '''
                    with lighting():
                        sleep(2)
                        accum+=2
                        move_to_position(pi, autocenter=True)
                        sleep(2)
                        accum+=2

                    if i==0:
                        close(description='Microbone to Turbo')

                    do_extraction()

                    if disable_between_positions:
                        end_extract()
                end_extract()
                disable()
                sleep(cooldown)

    sleep(max(0,cleanup-cooldown-accum))


def do_extraction():
    info('enable laser')
    enable()

    info('begin interval')
    begin_interval(duration)
    if ramp_duration>0:
        info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units))
        ramp(setpoint=extract_value, duration=ramp_duration, period=0.5)
    else:
        info('set extract to {}, {}'.format(extract_value, extract_units))
        extract(extract_value, extract_units)
        #sleep(2)

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
    