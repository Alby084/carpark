from abc import ABC
from Car import *


# https://blog.teclado.com/python-abc-abstract-base-classes/
class Sensor(ABC):
    pass


class EnterSensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
