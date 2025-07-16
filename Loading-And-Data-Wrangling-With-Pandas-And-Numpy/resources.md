## Data Wrangling With Pandas and Numpy
Data sources comes in many formats: plain text files, CSVs, SQL databases, Excel files and many more.
The pandas library is a core tool for data scientist and we will learn how to use it effectively in this chapter.
This section we will explore:
Loading data and saving data to several different data source types.
Some basic explonatory data analysis (EDA) and plotting with pandas
preparing and cleaning data for later use, including the imputation of missing data and outlier detection.
Essential data wrangling tools as filtering, groupby and replace.

Overall, this chapter will be another foundational chapter in your data science journey, giving you the tools necessary to get started working with data. We will go through a couple of examples to learn the basics of working with data in pandas and NumPy. In the first example, we will be using the chinook music data to clean and prepare data, then run an analysis
on song purchases. In the second example, we'll clean and prepare bitcoin price data, then analyze it

# Data wrangling and analyzing iTunes data
The term data wrangling and data munging have become common phrases in data science and generally mean to clean and prepare data for downstream uses such as analytics and modelling

# Loading and saving data with Pandas
The first step to wrangling data is, of course loading it
Pandas has several functions to load data for variety of tiles types.
We can load it to a dataframe like so:
import pandas as pd

csv = pd.read_read.csv('data/itunes_data.csv')

# Exploratory Data Analysis(EDA) and basic data cleaning with Pandas
Whenever we have some data loaded, its good idea to take a look at what we have.
In general we can follow a general EDA checklist
Examine the top and bottom of the data
Examine the data's dimensions
Examine the datatypes and missing values.
Investigate statistical properties of the data
Create plots of the data.

Some of this EDA can provide a starting point for any further analysis that we do.

