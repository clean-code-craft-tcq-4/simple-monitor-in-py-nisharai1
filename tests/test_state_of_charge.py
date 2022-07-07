from unittest import TestCase

from src.check_limits import BatteryManagementSystem


class TestStateOfCharge(TestCase):

    def setUp(self) -> None:
        self.battery_obj = BatteryManagementSystem()

    def test_low_state_of_charge(self):
        self.battery_obj.set_state_of_charge(10)
        self.assertRaises(ValueError, self.battery_obj.verify_state_of_charge_range)

    def test_high_state_of_charge(self):
        self.battery_obj.set_state_of_charge(90)
        self.assertRaises(ValueError, self.battery_obj.verify_state_of_charge_range)

    def test_normal_state_of_charge(self):
        self.battery_obj.set_state_of_charge(60)
        self.assertTrue(self.battery_obj.verify_state_of_charge_range)
