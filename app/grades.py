
import json

from pydantic import BaseModel, model_validator 

class Grades(BaseModel): 
    
    quiz_1:float = 0 
    quiz_2:float = 0 
    midterm:float = 0 
    project:float = 0 
    final:float = 0
    
    @model_validator(mode="before")
    @classmethod
    def fill_missing(cls, data):
        defaults = {
            "quiz_1": 0,
            "quiz_2": 0,
            "midterm": 0,
            "project": 0,
            "final": 0
        }

        for key, val in defaults.items():
            data.setdefault(key, val)
            
        return data
    
    @classmethod
    def load_grades_from_json(cls,filepath):
        try:
            with open(filepath, 'r') as fp:
                    data = json.load(fp)
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {filepath}")
            return None
        return cls.model_validate(data)
        
    def __str__(self) -> str:
        """
        This method gets called whenever this object is
        printed to string (e.g., standard out).
        """
        grades = []
        if self.quiz_1 is not None:
            grades.append(f'Quiz 1: {self.quiz_1}')
        if self.quiz_2 is not None:
            grades.append(f'Quiz 2: {self.quiz_2}')
        if self.midterm is not None:
            grades.append(f'Midterm Exam: {self.midterm}')
        if self.project is not None:
            grades.append(f'Project: {self.project}')
        if self.final is not None:
            grades.append(f'Final Exam: {self.final}')
            
        if len(grades) <= 0:
            return 'No grades submitted yet.'
        else:
            # Create a string in which each element of the list
            # is separate by a comma
            return 'GRADES --- ' + ', '.join(grades)