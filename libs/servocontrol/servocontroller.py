from libs.piconzero import piconzero as pz 
import time
#import logging
#logging.basicConfig(level=logging.INFO)
#mlogger = logging.getLogger(__name__)

print("Setting up servo pins")
# Define which pins are the servos
pan = 1
tilt = 0
click = 2

print("Initialising PiconBoard")
pz.init()

print("Setting output mode to Servo")
pz.setOutputConfig(pan, 2)
pz.setOutputConfig(tilt, 2)
pz.setOutputConfig(click, 2)

print("Centre all servos")
panVal = 90
tiltVal = 90
clickVal = 90
pz.setOutput (pan, panVal)
pz.setOutput (tilt, tiltVal)
pz.setOutput (click, clickVal)


def set_servo(pos):
    
    try:
        panVal = int(pos.get('left_right'))
        print(f'panVal {panVal}')
        pz.setOutput(pan, panVal)
    except TypeError:
        pass
    except Exception as error:
        print(error)
    
    try:
        tiltVal = int(pos.get('up_down'))
        print(f"tiltval: {tiltVal}")
        pz.setOutput(tilt, tiltVal)
    except TypeError:
        pass
    except Exception as error:
        print(error)

    try:
        clickVal = pos.get('click')
        print(f"clickVal: {clickVal}")
        if clickVal == 'YES':
            pz.setOutput(click, 55)
            time.sleep(0.5)
            pz.setOutput(click, 90)
    except TypeError:
        pass
    except Exception as error:
        print(error)
