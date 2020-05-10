"""
Module for controlling the servos via the piconzero library
"""
import time
import logging
from libs.piconzero import piconzero as pz 
from libs.servocontrol.boxcontroller import BoxController


sc_logger = logging.getLogger(__name__)
sc_logger.info("Setting up servo pins")
# Define which pins are the servos
pan = 1
tilt = 0
click = 2

sc_logger.info("Initialising PiconBoard")
pz.init()

sc_logger.info("Setting output mode to Servo")
pz.setOutputConfig(pan, 2)
pz.setOutputConfig(tilt, 2)
pz.setOutputConfig(click, 2)

sc_logger.info("Centre all servos")
pan_val = 90
tilt_val = 90
click_val = 90
pz.setOutput(pan, pan_val)
pz.setOutput(tilt, tilt_val)
pz.setOutput(click, click_val)

sc_logger.debug("Initialising BoxController")
bc = BoxController()

def set_servo(pos):
    '''
    Sets the position of the servo
    '''
    try:
        pan_val = int(bc.convert_pan(int(pos.get('left_right'))))
        sc_logger.debug(f'panVal {pan_val}')
        pz.setOutput(pan, pan_val)
    except TypeError:
        pass
    except Exception as error:
        sc_logger.error(error)

    try:
        tilt_val = int(bc.convert_tilt(int(pos.get('up_down'))))
        sc_logger.debug(f"tiltval: {tilt_val}")
        pz.setOutput(tilt, tilt_val)
    except TypeError:
        pass
    except Exception as error:
        sc_logger.error(error)

    try:
        click_val = pos.get('click')
        sc_logger.debug(f"clickVal: {click_val}")
        if click_val == 'YES':
            pz.setOutput(click, 55)
            time.sleep(0.5)
            pz.setOutput(click, 90)
    except TypeError:
        pass
    except Exception as error:
        sc_logger.error(error)
