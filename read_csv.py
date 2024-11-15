import pandas as pd
failure_data = pd.read_csv("failure_data.csv")
print(failure_data.describe())