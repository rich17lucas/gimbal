"""
Module for converting the Control Box co-ordinates into
values that fit in the horizontal and vertical range of
the servos
"""

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

    max_controlbox = 255    # The maximum value that could be returned by the controlbox
    min_controlbox = 0      # The minimum value that could be returned by the controlbox

    def convert_pan(self, pan):
        """
        Convert the pan value into a range between min_ and max_pan
        """
        new_pan = (pan * BoxController.max_pan / BoxController.max_controlbox) + BoxController.min_pan
        
        # Esnure that value is within permitted range.
        new_pan = BoxController.max_pan if new_pan > BoxController.max_pan else new_pan
        new_pan = BoxController.min_pan if new_pan < BoxController.min_pan else new_pan
        return int(new_pan)


    def convert_tilt(self, tilt):
        """
        Convert the tilt value into a range between min_ and max_pan
        """
        new_tilt = (tilt * BoxController.max_tilt / BoxController.max_controlbox) + BoxController.min_tilt

        # Esnure that value is within permitted range.
        new_tilt = BoxController.max_tilt if new_tilt > BoxController.max_tilt else new_tilt
        new_tilt = BoxController.min_tilt if new_tilt < BoxController.min_tilt else new_tilt

        return new_tilt
