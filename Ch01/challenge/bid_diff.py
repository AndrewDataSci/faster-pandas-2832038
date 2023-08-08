# Find the median betweeen the highest price and the 2nd highest price for each bid

import pandas as pd


def second(values):
    """Return second highest value

    >>> second([1, 7, 9, 3, 5])
    7
    """
    top, second = -1, -1
    for value in values:
        if value > top:
            top, second = value, top
        elif value > second:
            second = value
    return second


def median_diff(csv_file): #get the name of the CSV file.
    df = pd.read_csv(csv_file)
    top1 = df.groupby('id')['price'].max() #group by the ID and get the maximum price
    top2 = df.groupby('id')['price'].apply(second) #group by ID and get the second to maximum price as per function above
    diffs = top1 - top2 # calculate the difference
    return diffs.median() #return the median between the differences.

#Find out where the code is spedning it's time and use bods.csv.xz for data
