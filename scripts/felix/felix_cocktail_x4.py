#===============================================================================
# EXTRACTION SCRIPT felix_cocktail_x4.py
#===============================================================================
'''
modifier: 03
eqtime: 25
'''

def main():
    info("Cocktail Pipette x1")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')

    #shot 1
    gosub('common:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette1')
    close(description='Outer Pipette 1')
    sleep(1)
    
    #shots 2-4
    for i in range(3):
        info('Shot {}'.format(i+2))
        gosub('common:FillPipette1')
        gosub('common:ExpandPipette1')
        close(description='Outer Pipette 1')
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
	open(name='V', cancel_on_failed_actuation=False)
	