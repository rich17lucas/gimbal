"""
Unit tests for the conversion of the Control Box co-ordinates 
into values that fit in the horizontal and vertical range of 
the servos
"""
import pytest
from libs.servocontrol.boxcontroller import BoxController


class TestControlBox:
    """
    Tests for the pan and tilt value conversion
    """
    
    def setup_class(self):
        self.box_controller = BoxController()

    def test_min_pan(self):
        """
        Testing the min pan value is 0
        """
        #box_controller = BoxController()
        assert self.box_controller.convert_pan(-127) == 0

    def test_max_pan(self):
        """
        Test that the max pan is 180
        """
        assert self.box_controller.convert_pan(127) == 180

    def test_mid_pan(self):
        assert self.box_controller.convert_pan(0) == 90

    def test_too_low_pan(self):
        """
        Testing the min pan value is 0
        """
        assert self.box_controller.convert_pan(-127) == 0

    def test_too_high_pan(self):
        """
        Testing the max pan value is 180
        """
        assert self.box_controller.convert_pan(256) == 180

    def test_min_tilt(self):
        """
        Testing the min pan value is 55
        """
        assert self.box_controller.convert_tilt(-127) == 55

    def test_max_tilt(self):
        """
        Testing the max pan value is 120
        """
        assert self.box_controller.convert_tilt(127) == 120

    def test_too_low_tilt(self):
        """
        Testing that the system replaces negative values
        """
        assert self.box_controller.convert_tilt(-200) == 55
