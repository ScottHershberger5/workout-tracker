# Scott Hershberger
# CS 417
# Workout Tracker
# 2/3/26

from typing import List
from workout_tracker.exercises import Exercise

class Workout():
    
    def __init__(self):
        
        self._exercises = []

    def add_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout")
        self._exercises.append(exercise)

    def get_exercises(self):
        return self._exercises.copy()

    def total_calories(self):
        total_cals = sum(exercise.calculate_calories() for exercise in self._exercises)
        return float(total_cals)
    
    def total_duration(self):
        total_duration = sum(exercise.get_duration() for exercise in self._exercises)
        return float(total_duration)
    
    def exercise_count(self):
        num_exercises = [exercise for exercise in self._exercises]
        return int(len(num_exercises))
    
    def get_summary(self):
        if len(self.get_exercises()) == 0:
            return "Empty workout - no exercises added"
        summary = "-----Workout Summary-----\n"
        for index, exercise in enumerate(self._exercises):
            summary += f"{index:.0f}. {exercise}\n"
        summary += "-------------------------\n"
        summary += f"Total: {self.total_calories():.0f} calories, {self.total_duration():.0f} minutes"
        return summary

    def __str__(self):
        return f"Workout with {self.exercise_count()} exercise(s), {self.total_calories():.0f} calories"
    
    def __len__(self):
        return self.exercise_count()