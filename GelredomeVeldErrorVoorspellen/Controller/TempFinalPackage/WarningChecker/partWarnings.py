import pandas as pd


class PartWarnings:
    upper_limit = None
    lower_limit = None

    def warning_checker(self, value):
        return not (self.lower_limit < value < self.upper_limit)


def part_warnings_factory(part):
    part_warning: PartWarnings = PartWarnings()

    if part == "ClaspPressure":
        part_warning.__class__ = ClaspPressureWarnings
    elif part == "OilTemperature":
        part_warning.__class__ = OilTemperatureWarnings
    elif part == "Position":
        part_warning.__class__ = PositionWarnings
    elif part == "PressureA":
        part_warning.__class__ = PressureAWarnings
    elif part == "PressureB":
        part_warning.__class__ = PressureBWarnings
    elif part == "PushPressure":
        part_warning.__class__ = PushPressureWarnings
    elif part == "Velocity":
        part_warning.__class__ = VelocityWarnings
    return part_warning


# TO DO:
# Add all the upper and lower amounts
class ClaspPressureWarnings(PartWarnings):
    upper_limit = 300
    lower_limit = 0
    pass


class OilTemperatureWarnings(PartWarnings):
    upper_limit = 60
    lower_limit = 20
    pass


class PositionWarnings(PartWarnings):
    upper_limit = 1000
    lower_limit = 0
    pass


class PressureAWarnings(PartWarnings):
    upper_limit = 150
    lower_limit = 0
    pass


class PressureBWarnings(PartWarnings):
    upper_limit = 250
    lower_limit = 0
    pass


class PushPressureWarnings(PartWarnings):
    upper_limit = 50
    lower_limit = -200
    pass


class VelocityWarnings(PartWarnings):
    upper_limit = 40
    lower_limit = -40
    pass
