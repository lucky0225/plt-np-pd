import pandas as pd

# DataFrame
myDataSet = {
    "cars" : ["VW", "Citroen", "BMW", "Audi"],
    "PS": [105, 110, 150, 135]
}
myVar = pd.DataFrame(mydataset)
print(myvar)

# Series
a = [1, 7, 3]
series = pd.Series(a)
print(series)

# Labels
labels = pd.Series(a, index = ["x", "y", "z"])
print(labels)
print(labels["y"])

# Beispiel "calories"
calories = {"day1": 1200, "day2": 1600, "day3": 2100}
example1 = pd.Series(calories)
print(example1)
example2 = pd.Series(calories, index = ["day1", "day2"])
print(example2)