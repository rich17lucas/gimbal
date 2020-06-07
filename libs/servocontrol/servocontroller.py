"""
Module for controlling the servos via the piconzero library
"""
import time
import logging
from libs.piconzero import piconzero as pz 
from libs.servocontrol.boxcontroller import BoxController
from dataclasses import dataclass


@dataclass
class Servo():
    # Class to control servos via the PiconZero library
    # Uses dataclass to generate the scaffold methods

    def __init__(self, pz, pin, name):
        """Constructor"""
        print(f"Initalizing {name}")
        #self.logger = logging.getLogger()
        logger.debug("Setting reference to PiconZero instance")
        self.pz = pz
        logger.debug(" Set the PiconZero output to 'Servo' mode")
        self.pin = pin
        self.pz.setOutputConfig(pin, 2) 
        self.current_pos = 90
        
        #logger.debug("current_pos %", self.current_pos)

    def set_position(self, pos):
        print(f"Current Postion: {self.current_pos}")
        #logger.debug("Current Postion: %s", self.current_pos)
        #############################################
        # TODO - insert movement speed code here.
        #############################################
        self.pz.setOutput(self.pin, pos)
        self.current_pos = pos


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, 
                        format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        filename='app.log',
                        filemode='w')
logger.info("Setting up servo pins")
# Define which pins are the servos
pan = 1
tilt = 0
click = 2

logger.info("Initialising PiconBoard")
pz.init()

pan_servo = Servo(pz, pan, 'Pan')
tilt_servo = Servo(pz, tilt, 'Tilt')
click_servo = Servo(pz, click, 'Click')

#logger.info("Setting output mode to Servo")
#pz.setOutputConfig(pan, 2)
#pz.setOutputConfig(tilt, 2)
#pz.setOutputConfig(click, 2)

logger.info("Centre all servos")
pan_val = 90
tilt_val = 90
click_val = 90
#pz.setOutput(pan, pan_val)
#pz.setOutput(tilt, tilt_val)
#pz.setOutput(click, click_val)
pan_servo.set_position(pan_val)
tilt_servo.set_position(tilt_val)
click_servo.set_position(click_val)

logger.debug("Initialising BoxController")
bc = BoxController()

def set_servo(pos):
    '''
    Sets the position of the servo
    '''
    try:
        pan_val = int(bc.convert_pan(int(pos.get('left_right'))))
        logger.debug(f'panVal {pan_val}')
        #pz.setOutput(pan, pan_val)
        pan_servo.set_position(pan_val)
    except TypeError:
        pass
    except Exception as error:
        logger.error(error)

    try:
        tilt_val = int(bc.convert_tilt(int(pos.get('up_down'))))
        logger.debug(f"tiltval: {tilt_val}")
        #pz.setOutput(tilt, tilt_val)
        tilt_servo.set_position(tilt_val)
    except TypeError:
        pass
    except Exception as error:
        logger.error(error)

    try:
        click_val = pos.get('click')
        logger.debug(f"clickVal: {click_val}")
        if click_val == 'YES':
            #pz.setOutput(click, 55)
            click_servo.set_position(55)
            time.sleep(0.5)
            #pz.setOutput(click, 90)
            click_servo.set_position(90)
    except TypeError:
        pass
    except Exception as error:
        logger.error(error)
