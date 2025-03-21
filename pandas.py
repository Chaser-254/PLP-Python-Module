#pandas in python is a data manipulation library which provides data structures like dataframes and series which are very useful for data manipulation and analysis
#pandas is built on top of numpy and is used for data manipulation and analysis

#syntax: import pandas as pd
#pandas series
#A series is a one-dimensional array that can hold any data type such as integers, floats, and strings. It is similar to a Python list but with additional functionalities.
#A series can be created using the following constructor:
#pd.Series(data, index, dtype, copy)
#data: Data can be a list, dictionary, or scalar value.
#index: Index values must be unique and hashable, same length as data. Default integer index values.
#dtype: Data type of the series.
#copy: Copy data. Default False.
#Example:
import pandas as pd
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

#pandas dataframe
df = pd.DataFrame(data)
pd.read_csv("data.csv")
df = pd.read_csv("data.csv")
print(df)

df['column_name']
df['column_name'].mean()
df['column_name'].max()
df['column_name'].min()
df['column_name'].std()
df['column_name'].describe()

#pandas dataframe
#A DataFrame is a two-dimensional array with labeled axes (rows and columns). It is similar to a spreadsheet or SQL table.
#A DataFrame can be created using the following constructor:
#pd.DataFrame(data, index, columns, dtype, copy)
#data: Data can be a list, dictionary, or ndarray.
#index: Index values for rows.
#columns: Column names.
#dtype: Data type of each column.
#copy: Copy data. Default False.
#Example:
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

#filtering data
df[df['column_name'] > 10]
df[(df['column_name'] > 10) & (df['column_name'] < 20)]
df[df['column_name'].isin([10, 20, 30])]

#sorting data
df.sort_values('column_name')
df.sort_values('column_name', ascending=False)

#aggregating data
df.groupby('column_name').mean()
df.groupby('column_name').sum()
df.groupby('column_name').count()
df.groupby('column_name').max()
df.groupby('column_name').min()

#merging data
pd.concat([df1, df2])
pd.merge(df1, df2, on='column_name')

