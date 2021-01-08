from components.Text import Text
from components.Constants import *


class Time_Unit():
    def __init__(self):
        self.week = 0
        self.month = 0
        self.year = 0

    def increment(self, weeks):
        self.week += weeks
        self.correct()

    def correct(self):
        if self.week > 4:
            self.month += 1
            self.week = 0

        if self.month > 12:
            self.year += 1
            self.month = 0

    def __str__(self):
        return f"W: {self.week}, M: {self.month}, Y: {self.year}"


class Game_time:
    def __init__(self, max_years):
        self.max_years = max_years
        self.speed = 1
        self.unit = Time_Unit()
        self.display = Text(str(self.unit))
        self.display.setPos((width-180, 0))

    def each_second(self):
        self.unit.increment(self.speed)
        self.display.setText(str(self.unit))
