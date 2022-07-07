from unittest import TestCase

from src.check_limits import BatteryManagementSystem


class TestChargingRate(TestCase):

    def setUp(self) -> None:
        self.battery_obj = BatteryManagementSystem()

    def test_low_charging_rate(self):
        self.battery_obj.set_charge_rate(0.1)
        self.assertRaises(ValueError, self.battery_obj.verify_charge_rate_range)

    def test_high_charging_rate(self):
        self.battery_obj.set_charge_rate(0.9)
        self.assertRaises(ValueError, self.battery_obj.verify_charge_rate_range)

    def test_normal_charging_rate(self):
        self.battery_obj.set_charge_rate(0.45)
        self.assertTrue(self.battery_obj.verify_charge_rate_range)
