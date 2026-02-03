# Scott Hershberger
# CS 417
# Workout Tracker
# 2/3/26

from typing import List
from workout_tracker.exercises import Exercise

class Workout():
    
    def __init__(self):
        
        _exercises = []

    def add_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout")
        _exercises.append(exercise)

    def get_exersices(self):
        return _exercises.copy()

    # total calories method