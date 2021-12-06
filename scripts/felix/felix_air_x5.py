#===============================================================================
# EXTRACTION SCRIPT felix_air_x5.py
#===============================================================================
'''
modifier: 01
eqtime: 30
'''

def main():
    info("Air Pipette x5")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    
    #shot 1
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    close(description='Outer Pipette 2')
    sleep(1)
    
    #shots 2-5
    for i in range(4):
        info('Shot {}'.format(i+2))
        gosub('common:FillPipette2')
        gosub('common:ExpandPipette2')
        close(description='Outer Pipette 2')
        sleep(1)

#===============================================================================
# POST EQUILIBRATION SCRIPT felix_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')
    gosub('felix:PumpBone')
    if get_resource_value(name='FelixMiniboneFlag'):
        gosub('felix:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT felix_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='V')
	