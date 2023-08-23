import enum

class WaterLevelMeasurementTypeEnum(enum.Enum):
    MAX = 1
    MIN = 2

class WaterLevelStateEnum(enum.Enum):
    LOW = 0
    HIGH = 1
    
class WaterLevelSensor:

    def __init__(self, measurement_type, pin):
        self.measurement_type = measurement_type
        self.pin = pin
