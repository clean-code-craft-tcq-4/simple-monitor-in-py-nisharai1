class BatteryManagementSystem:

    def __init__(self):
        self.charging_temperature = None
        self.state_of_charge = None
        self.charge_rate = None

    def set_charging_temperature(self, charging_temperature):
        self.charging_temperature = charging_temperature

    def set_state_of_charge(self, state_of_charge):
        self.state_of_charge = state_of_charge

    def set_charge_rate(self, charge_rate):
        self.charge_rate = charge_rate

    def verify_charging_temperature_range(self):
        if self.charging_temperature < 0 or self.charging_temperature > 45:
            raise ValueError("Charging Temperature is  out of range")
        return True

    def verify_state_of_charge_range(self):
        if self.state_of_charge < 20 or self.state_of_charge > 80:
            raise ValueError("State of charge is out of range")
        return True

    def verify_charge_rate_range(self):
        if self.charge_rate < 0.2 or self.charge_rate > 0.8:
            raise ValueError("Charge rate is out of range")
        return True

    def battery_is_ok(self):
        battery_validation = [self.verify_charging_temperature_range(), self.verify_state_of_charge_range(),
                              self.verify_charge_rate_range()]
        for limit in battery_validation:
            if limit is False:
                print("Batteries are not working fine")
                return False
        return True
