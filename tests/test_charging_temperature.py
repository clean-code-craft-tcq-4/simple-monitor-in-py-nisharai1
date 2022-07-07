from unittest import TestCase

from src.check_limits import BatteryManagementSystem


class TestChargingTemperature(TestCase):

    def setUp(self) -> None:
        self.battery_obj = BatteryManagementSystem()

    def test_low_temperature_scenario(self):
        self.battery_obj.set_charging_temperature(-1)
        self.assertRaises(ValueError, self.battery_obj.verify_charging_temperature_range)

    def test_high_temperature_scenario(self):
        self.battery_obj.set_charging_temperature(70)
        self.assertRaises(ValueError, self.battery_obj.verify_charging_temperature_range)

    def test_normal_temperature_scenario(self):
        self.battery_obj.set_charging_temperature(37)
        self.assertTrue(self.battery_obj.verify_charging_temperature_range)

