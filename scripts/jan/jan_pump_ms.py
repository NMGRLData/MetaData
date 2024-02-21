def main():
    info('Pumping spectrometer')
    open(name='O', cancel_on_failed_actuation=False)
    
    # setup dynamic pumping
    # delay extra time of the ar40 intensity is greater than a set threshold
    
    ar40intensity = get_intensity('H1')
    if ar40intensity> 600:
        sleep(100)
    elif ar40intensity>3000:
        sleep(10)