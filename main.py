import csv
import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
print(len(black))