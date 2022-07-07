from unittest import TestCase

from src.check_limits import BatteryManagementSystem


class TestBatteryPerformance(TestCase):

    def setUp(self) -> None:
        self.battery_obj = BatteryManagementSystem()

    def test_battery_is_ok(self):
        self.battery_obj.set_charging_temperature(34)
        self.battery_obj.set_state_of_charge(70)
        self.battery_obj.set_charge_rate(0.7)
        self.assertTrue(self.battery_obj.battery_is_ok())

    def test_battery_is_not_ok(self):
        self.battery_obj.set_charging_temperature(65)
        self. battery_obj.set_state_of_charge(87)
        self.battery_obj.set_charge_rate(0.99)
        self.assertRaises(ValueError, self.battery_obj.battery_is_ok)
