import pandas as pd

data = pd.read_csv("./Day25_Squirrel/Squirrel_Data.csv")

counts = data["Primary Fur Color"].value_counts()

counts.to_csv("./Day25_Squirrel/new_csv.csv")
