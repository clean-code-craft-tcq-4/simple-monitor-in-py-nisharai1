# def print_message(message):
#     print(message)


def verify_warning_en(min_value, max_value, value):
    threshold = 0.5 * max_value
    if value >= min_value + threshold:
        print('Warning: Approaching discharge')
    if value <= max_value - threshold:
        print('Warning: Approaching charge-peak')


def verify_warning_de(min_value, max_value, value):
    threshold = 0.5 * max_value
    if value >= min_value + threshold:
        print('Warnung: Naht Entladung')
    if value <= max_value - threshold:
        print('Warnung: Ladespitze nähert sich')


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

    def verify_charging_temperature_range_en(self):
        verify_warning_en(0, 45, self.charging_temperature)
        if self.charging_temperature < 0 or self.charging_temperature > 45:
            raise ValueError("Charging Temperature is  out of range")
        return True

    def verify_charging_temperature_range_de(self):
        verify_warning_de(0, 45, self.charging_temperature)
        if self.charging_temperature < 0 or self.charging_temperature > 45:
            raise ValueError("Die Ladetemperatur liegt außerhalb des zulässigen Bereichs")
        return True

    def verify_state_of_charge_range_en(self):
        verify_warning_en(20, 80, self.state_of_charge)
        if self.state_of_charge < 20 or self.state_of_charge > 80:
            raise ValueError("State of charge is out of range")
        return True

    def verify_state_of_charge_range_de(self):
        verify_warning_de(20, 80, self.state_of_charge)
        if self.state_of_charge < 20 or self.state_of_charge > 80:
            raise ValueError("Der Ladezustand ist außerhalb des Bereichs")
        return True

    def verify_charge_rate_range_en(self):
        verify_warning_en(0, 0.8, self.charge_rate)
        if self.charge_rate < 0 or self.charge_rate > 0.8:
            raise ValueError("Charge rate is out of range")
        return True

    def verify_charge_rate_range_de(self):
        verify_warning_de(0, 0.8, self.charge_rate)
        if self.charge_rate < 0 or self.charge_rate > 0.8:
            raise ValueError("Der Ladestrom liegt außerhalb des Bereichs")
        return True

    def battery_is_ok_en(self):
        battery_validation = [self.verify_charging_temperature_range_en(), self.verify_state_of_charge_range_en(),
                              self.verify_charge_rate_range_en()]
        for limit in battery_validation:
            if limit is False:
                print("Batteries are not working fine")
                return False
        return True

    def battery_is_ok_de(self):
        battery_validation = [self.verify_charging_temperature_range_de(), self.verify_state_of_charge_range_de(),
                              self.verify_charge_rate_range_de()]
        for limit in battery_validation:
            if limit is False:
                print("Batterien funktionieren nicht einwandfrei")
                return False
        return True
