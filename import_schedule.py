import pandas as pd
import schedule
import time
import os



my_dir = os.chdir('path to your directory')


old = pd.read_csv('Sales.csv',sep=',')


new = pd.read_csv('New_Sales.csv',sep=',')
most_recent_timestamp = old["TimeStamp"].max()

# filter the rows in file_1 where the timestamp is more recent than the most recent timestamp in file_2
new_rows = new[new["TimeStamp"] > most_recent_timestamp]

# append the new rows to file_1
file_1 = old.append(new_rows)

# save the updated file_1
file_1.to_csv("path to sales 2 csv", index=False)
