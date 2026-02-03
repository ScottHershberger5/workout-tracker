# Scott Hershberger
# CS417
# 2/3/26



"""Exercise classes for the workout tracker."""

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name, date = None):
        """Initialize an Exercise.
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        # TODO: Set self.name
        # TODO: Set self.date (use datetime.now().strftime("%Y-%m-%d") if date is None)
        
        self.name = mame
        if date:
            self.date = date
        else:
            self.date = datetime.now().strftime("%Y-%m-%d")
    
    def calculate_calories(self):
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        
        return 0.0
    
    def get_duration(self):
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self):
        """Return a string representation of the exercise."""
        # TODO: Return a string like "ExerciseName: 100 calories"
        # Use self.calculate_calories() to get the calories
        return f"{self.name}: {self.calculate_calories()} calories"

class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """
    
    def __init__(self, name, distance, duration, date = None):
        """Initialize a CardioExercise.
        
        Args:
            name: Exercise name (e.g., "Running", "Cycling")
            distance: Distance covered in miles
            duration: Time spent in minutes
            date: Date performed (optional)
        """
        # TODO: Call parent class __init__ with super()
        # TODO: Set self.distance
        # TODO: Set self.duration
        super().__init__(self, name, date = None)
        self.distance = float(distance)
        self.duration = float(duration)
    
    def calculate_calories(self):
        """Calculate calories burned based on distance.
        
        Formula: distance * 100
        
        Returns:
            float: Estimated calories burned
        """
        # TODO: Implement the formula
        return float(self.distance * 100)
    
    def get_duration(self):
        """Get the duration of the cardio exercise.
        
        Returns:
            float: Duration in minutes
        """
        # TODO: Return the duration attribute
        return self.duration
    
    def __str__(self):
        """Return detailed string representation."""
        # TODO: Return something like "Running (3.5 miles, 30 min): 350 calories"
        # Include self.name, self.distance, self.duration, and self.calculate_calories()
        return f"You did {self.name}, you went {self.distance} miles in {self.duration} minutes. You burned {self.calculate_calories()}"