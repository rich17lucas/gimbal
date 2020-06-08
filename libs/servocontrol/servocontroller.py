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
        logger.debug("Setting reference to PiconZero instance")
        self.pz = pz
        logger.debug(" Set the PiconZero output to 'Servo' mode")
        self.pin = pin
        self.pz.setOutputConfig(pin, 2) 
        self.current_degree = 90

    #-----------------------------------------------------
    def set_position(self, target_degree):
        """
        Tells the servo to go directly to the position at maximum speed
        """
        self.pz.setOutput(self.pin, target_degree)
        self.current_degree = target_degree

    #-----------------------------------------------------
    def set_position_rate(self, target_degree, slew_rate=45):
        """
        DEPRECATED: Controls the speed that a servo goes to a position
        But does not work as smoothly as expected. 
        """
        DEGSECOND = 90
   
        # Set the maximum slew rate
        slew_rate = min(slew_rate, DEGSECOND)
        DIRECTION = 1
        TIMEINTER = 0.1 # Seconds

        # How many degrees per interval
        degrees_per_interval = TIMEINTER * slew_rate

        # Calculate the angular difference between origin and target positions
        degrees_to_turn = target_degree - self.current_degree

        if degrees_to_turn < 0:
            # Negative acceleration for moving anti-clockwise
            DIRECTION *= -1

        # Initialise the other variables
        degrees_remaining = degrees_to_turn
        correction_time = 0
            
        while abs(degrees_remaining) > 0:
            start_time = time.time()
            # Calculate the next position
            next_move_degree = (degrees_per_interval * DIRECTION)
            # Where are we now?
            self.current_degree += int(next_move_degree)
            print(f"Current Degree {self.current_degree}")
            # Set the servo position
            self.set_position(self.current_degree)
            # How far have we got left to traverse
            degrees_remaining = int(target_degree - self.current_degree)
            
            end_time = time.time()
            correction_time = TIMEINTER - (end_time - start_time)
            time.sleep(TIMEINTER - correction_time )
            print(f"Next Move: {next_move_degree}; Current pos: {self.current_degree}; degrees_remaining: {degrees_remaining} ")
  
            if DIRECTION == -1 and self.current_degree < target_degree:
                print('Too far left')
                break
            elif DIRECTION == 1 and self.current_degree > target_degree:
                print('Too far right')
                break
    #-----------------------------------------------------


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

logger.info("Centre all servos")
pan_val = 90
tilt_val = 90
click_val = 90
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
        pan_servo.set_position(pan_val)
    except TypeError as te:
        logger.error(te)
        pass
    except Exception as error:
        logger.error(error)

    try:
        tilt_val = int(bc.convert_tilt(int(pos.get('up_down'))))
        logger.debug(f"tiltval: {tilt_val}")
        tilt_servo.set_position(tilt_val)
    except TypeError as te:
        logger.error(te)
        pass
    except Exception as error:
        logger.error(error)

    try:
        click_val = pos.get('click')
        logger.debug(f"clickVal: {click_val}")
        if click_val == 'YES':
            click_servo.set_position(55)
            time.sleep(0.5)
            click_servo.set_position(90)
    except TypeError:
        pass
    except Exception as error:
        logger.error(error)
