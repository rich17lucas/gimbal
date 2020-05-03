from libs.piconzero import piconzero as pz 
import time
import logging

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
panVal = 90
tiltVal = 90
clickVal = 90
pz.setOutput (pan, panVal)
pz.setOutput (tilt, tiltVal)
pz.setOutput (click, clickVal)


def set_servo(pos):
    
    try:
        panVal = int(pos.get('left_right'))
        sc_logger.debug(f'panVal {panVal}')
        pz.setOutput(pan, panVal)
    except TypeError:
        pass
    except Exception as error:
        sc_logger.error(error)
    
    try:
        tiltVal = int(pos.get('up_down'))
        sc_logger.debug(f"tiltval: {tiltVal}")
        pz.setOutput(tilt, tiltVal)
    except TypeError:
        pass
    except Exception as error:
        sc_logger.error(error)

    try:
        clickVal = pos.get('click')
        sc_logger.debug(f"clickVal: {clickVal}")
        if clickVal == 'YES':
            pz.setOutput(click, 55)
            time.sleep(0.5)
            pz.setOutput(click, 90)
    except TypeError:
        pass
    except Exception as error:
        sc_logger.error(error)
