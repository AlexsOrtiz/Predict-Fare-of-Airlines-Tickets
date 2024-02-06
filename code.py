import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


train_data = pd.read_excel("/content/drive/MyDrive/Project #1/Data_Train.xlsx")

train_data.head(4)

train_data.isnull().sum()

train_data[train_data["Total_Stops"].isnull()]

train_data.dropna(inplace=True)

train_data.isnull().sum()

data = train_data.copy()

def change_into_Datetime(col):
  data[col] = pd.to_datetime(data[col])

**Defines a function to convert specific columns to datetime format.**

import warnings
from warnings import filterwarnings
filterwarnings("ignore")


data.columns

for feature in ['Dep_Time', 'Arrival_Time', 'Date_of_Journey']:
  change_into_Datetime(feature)

**Function is applied change_into_Datetimeto the 'Dep_Time', 'Arrival_Time', and 'Date_of_Journey' columns**

data["Jorney_day"] = data['Date_of_Journey'].dt.day

data["Jorney_month"] = data['Date_of_Journey'].dt.month

data["Jorney_year"] = data['Date_of_Journey'].dt.year

data.head(3)

def extract_hour_min(df, col):
  df[col+"_hour"] = df[col].dt.hour
  df[col+"_minute"] = df[col].dt.minute
  return df.head(3)

**Defines a function to extract the hour and minutes from a datetime column and create new columns.**




data.columns

extract_hour_min(data, "Dep_Time")

extract_hour_min(data, "Arrival_Time")

cols_to_drop = ["Arrival_Time",  "Dep_Time"]
data.drop(cols_to_drop, axis=1, inplace = True)

Definition of Columns to Delete:

    * cols_to_drop = ["Arrival_Time", "Dep_Time"]

This line creates a list called cols_to_dropWhat the names of the columns do you want to remove from the DataFrame?  In this case, the columns are "Arrival_Time"and "Dep_Time".


Removing Columns from the DataFrame:

    * data.drop(cols_to_drop, axis=1, inplace = True)

This line uses the method dropof the DataFrame datato remove the columns.

    * cols_to_drop

It is the first argument and represents the columns that are wanted removed.

    * axis=1

indicates that the operation must be carried out in the columns. In pandas,  axis=0refers to rows and  axis=1 to columns.

    * inplace=True
Meaning the change will be made to the DataFrame .  datadirectly, without assigning it to a new variable. If I were Falseyou would have to assign the result to  dataor another variable to save changes.

data.head(3)

data.shape

def flight_dep_time(x):
  if (x>4) and (x<=6):
    return "Early morning"
  elif (x>6) and (x<=12):
    return "morning"
  elif (x>12) and (x<=16):
    return "noon"
  elif (x>16) and (x<=20):
    return "Evening"
  elif (x>20) and (x<=24):
    return "Night"
  else:
    return "late night"

data["Dep_Time_hour"].apply(flight_dep_time).value_counts()

!pip install plotly
!pip install chart_studio

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.offline as pyo
import cufflinks as cf
from plotly.offline import iplot

cf.go_offline(connected=True)

!pip install cufflinks

# Your existing code to create a bar plot
bar_plot = data["Dep_Time_hour"].apply(flight_dep_time).value_counts()

# Use iplot to display the interactive plot
bar_plot.iplot(kind="bar", title="Flight Departure Times", xTitle="Time of Day", yTitle="Count")
