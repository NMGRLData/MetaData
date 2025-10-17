#===============================================================================
# EXTRACTION SCRIPT felix_air_x1-3.py
#===============================================================================
'''
modifier: 02
eqtime: 35
'''

def main():
    info("Air Pipette x1")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    
    open(name='Q')
    
    gosub('common:ExpandPipette2')
    
    close(name='Q')
    # close(description='Outer Pipette 2')
    
    

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
	