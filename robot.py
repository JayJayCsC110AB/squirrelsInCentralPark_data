import csv
import pandas as pd

data = 1
trial_id = 0
def log_trial(object_name, result, error_code=None):
    global trial_id
    trial_id +=1
   
    trial = {   
            "trial_id" : trial_id,
            "object_name": object_name,
            "result" : result,
            "error code": error_code}
    data.append(trial)
    