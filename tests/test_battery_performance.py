from unittest import TestCase

from src.check_limits import BatteryManagementSystem


class TestBatteryPerformance(TestCase):

    def setUp(self) -> None:
        self.battery_obj = BatteryManagementSystem()

    def test_battery_is_ok_en(self):
        self.battery_obj.set_charging_temperature(34)
        self.battery_obj.set_state_of_charge(70)
        self.battery_obj.set_charge_rate(0.7)
        self.assertTrue(self.battery_obj.battery_is_ok_en())

    def test_battery_is_ok_de(self):
        self.battery_obj.set_charging_temperature(30)
        self.battery_obj.set_state_of_charge(80)
        self.battery_obj.set_charge_rate(0)
        self.assertTrue(self.battery_obj.battery_is_ok_de())

    def test_battery_is_not_ok_en(self):
        self.battery_obj.set_charging_temperature(87)
        self. battery_obj.set_state_of_charge(0)
        self.battery_obj.set_charge_rate(0)
        self.assertRaises(ValueError, self.battery_obj.battery_is_ok_en)

    def test_battery_is_not_ok_de(self):
        self.battery_obj.set_charging_temperature(30)
        self. battery_obj.set_state_of_charge(50)
        self.battery_obj.set_charge_rate(0.9)
        self.assertRaises(ValueError, self.battery_obj.battery_is_ok_de)

    def test_battery1_en(self):
        self.battery_obj.set_charging_temperature(-1)
        self. battery_obj.set_state_of_charge(79)
        self.battery_obj.set_charge_rate(0)
        self.assertRaises(ValueError, self.battery_obj.battery_is_ok_en)

    def test_battery1_de(self):
        self.battery_obj.set_charging_temperature(30)
        self. battery_obj.set_state_of_charge(10)
        self.battery_obj.set_charge_rate(0)
        self.assertRaises(ValueError, self.battery_obj.battery_is_ok_de)


