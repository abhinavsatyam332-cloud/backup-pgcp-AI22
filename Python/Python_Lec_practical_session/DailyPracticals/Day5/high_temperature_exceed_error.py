class High_temperature_exceed_error(Exception):
    pass



class Sensor:
    def __init__(self, temp):
        self._temperature = temp

    def check_temp(self):
        if self._temperature > 50:
            raise High_temperature_exceed_error('temp too high')

try:
    s = Sensor(80)
    s.check_temp()

except High_temperature_exceed_error as er:
    print(er)
