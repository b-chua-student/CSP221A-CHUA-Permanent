# 1. Turn raw_rows into DataFrame
# 2. Reject all records with invalid scores (NaN, outside range 0-100) with specific, informative error
# 3. Create Student instances from cleaned data
#   - records should be locked
#   - modifying records should raise custom exception
#   - create __str__
#   - create __repr__
#   - create .average() method that returns np.mean of every Student @classmethod
#   - create .lock() method that ensures records are locked @classmethod
#   - create .add_score() method that fails when records are lcoked

import pandas as pd
import numpy as np

raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

raw_df = pd.DataFrame(raw_rows)

print("Running")
print(raw_df)

def clean_data(df):
    df.dropna()
    df.drop_duplicates(subset=["name"])
    df["name"] = df["name"].str.strip()

    return df

cleaned_data = clean_data(raw_df)
print(cleaned_data)

class Student:
    def __init__(self, name, is_locked: bool = False):
        self.name = name
        self.scores = np.array([])

    def lock(self):
        self.is_locked = True

    def add_score(self, scores):
        if self.is_locked is True:
            raise ValueError("Record is locked.")

        for score in scores:
            self.scores.append(score)

    def average(self):
        return np.mean(self.scores)

    def __str__():
        pass

    def __repr__():
        pass

class InvalidScoreError(Exception):
    pass

class StudentRecordLockedError(Exception):
    pass