"""
Module for converting the Control Box co-ordinates into
values that fit in the horizontal and vertical range of
the servos
"""
import logging

class BoxController:
    """
    Converts the X, Y values from the Control Box on the website
    from 0-255 to the values that will stop the servos from trying
    to go past their limits.
    """

    min_tilt = 55   # The minimum position fo the vertical servo
    max_tilt = 120  # The maximum position of the vertical servo

    min_pan = 0     # The minimum position of the pan servo
    max_pan = 180   # The maximum position of hte pan servo

    max_controlbox = 127    # The maximum value that could be returned by the controlbox
    min_controlbox = -127      # The minimum value that could be returned by the controlbox

    def __init__(self):
        self.logger = logging.getLogger(__name__)


    def convert_pan(self, pan):
        """
        Convert the pan value into a range between min_ and max_pan
        """
        #new_pan = (pan * BoxController.max_pan / (BoxController.max_controlbox + 127)) + BoxController.min_pan
        new_pan = (pan * BoxController.max_pan / (BoxController.max_controlbox + 127)) + 90
        # Ensure that value is within permitted range.
        new_pan = BoxController.max_pan if new_pan > BoxController.max_pan else new_pan
        new_pan = BoxController.min_pan if new_pan < BoxController.min_pan else new_pan

        self.logger.debug(f"Input pan {pan} converted to {new_pan}")
        return int(new_pan)


    def convert_tilt(self, tilt):
        """
        Convert the tilt value into a range between min_ and max_pan
        """
        #new_tilt = (tilt * BoxController.max_tilt / (BoxController.max_controlbox + 127)) + BoxController.min_tilt + 127
        new_tilt = (tilt * BoxController.max_tilt / (BoxController.max_controlbox + 127)) + 60
        # Esnure that value is within permitted range.
        new_tilt = BoxController.max_tilt if new_tilt > BoxController.max_tilt else new_tilt
        new_tilt = BoxController.min_tilt if new_tilt < BoxController.min_tilt else new_tilt

        self.logger.debug(f"Input tilt {tilt} converted to {new_tilt}")
        return int(new_tilt)
