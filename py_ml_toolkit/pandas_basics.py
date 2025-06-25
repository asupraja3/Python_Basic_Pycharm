#All essential pandas functions for data manipulation and analysis with detailed explanations of parameters and outputs.
import numpy as np
import pandas as pd
# Create a DataFrame from a dictionary
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("DataFrame from dictionary:")
print(df)
# Create a DataFrame from a list of lists
data = [[1, 4], [2, 5], [3, 6]]
#All the parameters explained of DataFrame():
# data: The data to be stored in the DataFrame can be a dictionary, list of lists, or other data structures.
# index: Optional parameter to specify the row labels. If not provided, default integer index is used.
# columns: Optional parameter to specify the column labels. If not provided, default column names are used.
# dtype: Optional parameter to specify the data type of the DataFrame. If not provided, pandas will infer the data type.
# # copy: Optional parameter to specify whether to copy the data or not. Default is True, meaning a copy is made.
df_from_list = pd.DataFrame(data, columns=['A', 'B'])
print("\nDataFrame from list of lists:")
print(df_from_list)
#Output:
# DataFrame from list of lists:
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6

# Create a DataFrame from a CSV file
#All the parameters explained of read_csv():
# filepath_or_buffer: The path to the CSV file to be read.
# sep: The delimiter used in the CSV file. Default is ','.
# header: Row number(s) to use as the column names. Default is 'infer', meaning pandas will try to infer the header.
# index_col: Column(s) to set as the index of the DataFrame. Default is None, meaning no index column is set.
# dtype: Data type to use for the DataFrame. Default is None, meaning pandas will infer the data types.
df_from_csv = pd.read_csv('file.csv')  # Uncomment this line to read from a CSV file
print("\nDataFrame from CSV file:", df_from_csv)

# Create a DataFrame from a JSON file
df_from_json = pd.read_json('file.json')
print("\nDataFrame from JSON file:", df_from_json)

# Create a DataFrame from a NumPy array
df_from_array = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['A', 'B'])
print("\nDataFrame from NumPy array:", df_from_array)

# Create a DataFrame from a Series
#All Parameters explained of Series():
# data: The data to be stored in the Series can be a list, NumPy array, or other data structures.
# index: Optional parameter to specify the index labels for the Series. If not provided, default integer index is used.
# dtype: Optional parameter to specify the data type of the Series. If not provided, pandas will infer the data type.
# # name: Optional parameter to specify the name of the Series. If not provided, the Series will have no name.
df_from_series = pd.DataFrame(pd.Series([1, 2, 3], name='A'))
print("\nDataFrame from Series:",df_from_series)

# Create a DataFrame from a dictionary of Series
df_from_dict_series = pd.DataFrame({'A': pd.Series([1, 2, 3]), 'B': pd.Series([4, 5, 6])})
print("\nDataFrame from dictionary of Series:", df_from_dict_series)

# Create a DataFrame from a list of dictionaries
df_from_list_dicts = pd.DataFrame([{'A': 1, 'B': 4}, {'A': 2, 'B': 5}, {'A': 3, 'B': 6}])

# Create a DataFrame from a list of tuples
df_from_list_tuples = pd.DataFrame([(1, 4), (2, 5), (3, 6)], columns=['A', 'B'])

# Create a DataFrame from a NumPy structured array
df_from_structured_array = pd.DataFrame(np.array([(1, 4), (2, 5), (3, 6)], dtype=[('A', 'i4'), ('B', 'i4')]))

#Other Essential Pandas Functions

# Display the first few rows of the DataFrame
# All the parameters explained of head():
# n: Number of rows to return. Default is 5.
print("\nFirst few rows of DataFrame:",df.head())

# Display the last few rows of the DataFrame
# All the parameters explained of tail():
# n: Number of rows to return. Default is 5.
print("\nLast few rows of DataFrame:", df.tail())

# Display the shape of the DataFrame
# All the parameters explained of shape:
# Returns a tuple representing the dimensions of the DataFrame (number of rows, number of columns).
print("\nShape of DataFrame:", df.shape)

# Display the columns of the DataFrame
# All the parameters explained of columns:
# Returns the column labels of the DataFrame as an Index object.
print("\nColumns of DataFrame:", df.columns)

# Display the index of the DataFrame
# All the parameters explained of index:
# Returns the row labels of the DataFrame as an Index object.
print("\nIndex of DataFrame:", df.index)

# Display the data types of each column in the DataFrame
# All the parameters explained of dtypes:
# Returns a Series with the data type of each column in the DataFrame.
print("\nData types of each column in DataFrame:", df.dtypes)

# Display basic statistics of the DataFrame
# All the parameters explained of describe():
# percentiles: List of percentiles to include in the output. Default is [0.25, 0.5, 0.75].
# include: Data types to include in the output. Default is 'number', meaning only numeric columns are included.
# exclude: Data types to exclude from the output. Default is None, meaning no data types are excluded.
print("\nBasic statistics of DataFrame:",df.describe())

# memory_usage(): Display the memory usage of the DataFrame
# All the parameters explained of memory_usage():
# index: Whether to include the index in the memory usage calculation. Default is True.
# deep: Whether to calculate the memory usage of the DataFrame's elements. Default is False.
# Returns a Series with the memory usage of each column in bytes.
print("\nMemory usage of DataFrame:", df.memory_usage(deep=True))

# unique(): Display the unique values in a column
# All the parameters explained of unique():
# Returns an array of unique values in the specified column.
print("\nUnique values in column 'A':", df['A'].unique())

# nunique(): Count the number of unique values in a column
# All the parameters explained of nunique():
# dropna: Whether to exclude NaN values from the count. Default is True.
print("\nNumber of unique values in column 'A':", df['A'].nunique(dropna=True))

# value_counts(): Count the occurrences of each unique value in a column
# All the parameters explained of value_counts():
# normalize: Whether to return the relative frequencies of the unique values. Default is False.
# sort: Whether to sort the output by the counts. Default is True.
print("\nValue counts in column 'A':", df['A'].value_counts(normalize=False, sort=True))

# sort_values(): Sort the DataFrame by a column
# All the parameters explained of sort_values():
# by: Column(s) to sort by. Can be a single column name or a list of column names.
# ascending: Whether to sort in ascending order. Default is True.
# inplace: Whether to modify the DataFrame in place. Default is False, meaning a new sorted DataFrame is returned.
print("\nDataFrame sorted by column 'A':", df.sort_values(by='A', ascending=True, inplace=False))

# sort_index(): Sort the DataFrame by its index
# All the parameters explained of sort_index():
# axis: Axis to sort along. 0 for rows (default) and 1 for columns.
# ascending: Whether to sort in ascending order. Default is True.
# inplace: Whether to modify the DataFrame in place. Default is False, meaning a new sorted DataFrame is returned.
print("\nDataFrame sorted by index:", df.sort_index(axis=0, ascending=True, inplace=False))

# groupby(): Group the DataFrame using a column and apply aggregate functions
# All the parameters explained of groupby():
# by: Column(s) to group by. Can be a single column name or a list.
# axis: Axis to group along (0 for rows, 1 for columns). Default is 0.
# as_index: Whether to return grouped keys as index. Default is True.
# sort: Sort group keys. Default is True.
grouped = df.groupby('Department')['Salary'].mean()

# pivot_table(): Create a spreadsheet-style pivot table
# All the parameters explained of pivot_table():
# data: DataFrame to use for creating the pivot table.
# index: Column(s) to use to make new frame’s index.
# values: Column(s) to aggregate.
# aggfunc: Function to use for aggregation. Default is 'mean'.
# fill_value: Replace missing values with this value.
pivot = pd.pivot_table(df, index='Department', values='Salary', aggfunc='mean')

# isnull(): Detect missing values in the DataFrame
# All the parameters explained of isnull():
# No parameters. Returns a DataFrame of same shape with boolean values.
print(df.isnull())

# fillna(): Fill NA/NaN values with a specific value
# All the parameters explained of fillna():
# value: Scalar or dict to fill NaN values.
# method: Fill method ('ffill', 'bfill'). Default is None.
# inplace: Whether to modify the DataFrame in place. Default is False.
# limit: Max number of NaN values to fill.
filled_df = df.fillna(value={'Salary': 0})

# dropna(): Remove missing values from the DataFrame
# All the parameters explained of dropna():
# axis: 0 to drop rows, 1 to drop columns. Default is 0.
# how: 'any' to drop if any NA present, 'all' if all are NA.
# inplace: Modify the original DataFrame. Default is False.
dropped_na_df = df.dropna()

# drop(): Drop specified rows or columns
# All the parameters explained of drop():
# labels: The labels to drop (row index or column name).
# axis: 0 for rows, 1 for columns. Default is 0.
# inplace: Whether to modify in place. Default is False.
dropped_column_df = df.drop(columns=['Age'])

# rename(): Rename the labels (index or columns)
# All the parameters explained of rename():
# columns: Dict mapping old column names to new ones.
# index: Dict mapping old row labels to new ones.
# inplace: Whether to perform operation in place. Default is False.
renamed_df = df.rename(columns={'Salary': 'AnnualSalary'})

# apply(): Apply a function to rows or columns
# All the parameters explained of apply():
# func: The function to apply.
# axis: 0 for columns, 1 for rows. Default is 0.
# result_type: Type of output ('expand', 'reduce', 'broadcast'). Default is None.
df['Bonus'] = df['Salary'].apply(lambda x: x * 0.10)

# duplicated(): Return boolean Series for duplicate rows
# All the parameters explained of duplicated():
# subset: Columns to consider for identifying duplicates.
# keep: 'first', 'last', or False. Default is 'first'.
print(df.duplicated())

# drop_duplicates(): Remove duplicate rows
# All the parameters explained of drop_duplicates():
# subset: Columns to consider for identifying duplicates.
# keep: 'first', 'last', or False. Default is 'first'.
# inplace: Modify the original DataFrame. Default is False.
unique_df = df.drop_duplicates()

# astype(): Convert the data type of a Series or column
# All the parameters explained of astype():
# dtype: Target data type (e.g., 'float', 'int', 'str').
# errors: Error handling ('raise' or 'ignore'). Default is 'raise'.
df['Age'] = df['Age'].astype(float)

# set_index(): Set one or more columns as the DataFrame index
# All the parameters explained of set_index():
# keys: Column(s) to use as index.
# drop: Drop the column from DataFrame. Default is True.
# inplace: Modify in place. Default is False.
indexed_df = df.set_index('Name')

# reset_index(): Reset the index to default integer index
# All the parameters explained of reset_index():
# drop: Drop index instead of inserting as a column. Default is False.
# inplace: Modify in place. Default is False.
reset_df = indexed_df.reset_index()

# query(): Query the DataFrame with a boolean expression
# All the parameters explained of query():
# expr: Query string.
# inplace: Modify in place. Default is False.
# engine: Evaluation engine. Default is 'python'.
query_df = df.query('Salary > 50000')

# sample(): Return a random sample of rows
# All the parameters explained of sample():
# n: Number of samples.
# frac: Fraction to return (instead of n).
# replace: Sample with replacement. Default is False.
# random_state: Seed for reproducibility.
sample_df = df.sample(n=2, random_state=1)

# concat(): Concatenate pandas objects along a given axis
# All the parameters explained of concat():
# objs: List of DataFrames.
# axis: 0 for rows, 1 for columns. Default is 0.
# ignore_index: Reindex the result. Default is False.
concatenated_df = pd.concat([df, df])

# melt(): Convert wide DataFrame to long format
# All the parameters explained of melt():
# id_vars: Columns to keep fixed.
# value_vars: Columns to unpivot.
# var_name: Name for variable column.
# value_name: Name for value column.
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'Salary'])

# isin(): Check whether each element is in the given list
# All the parameters explained of isin():
# values: Iterable to check membership.
# Returns a boolean Series.
isin_result = df['Department'].isin(['HR', 'Finance'])

# between(): Check if values are between two values
# All the parameters explained of between():
# left: Lower bound.
# right: Upper bound.
# inclusive: Include boundaries. Default is 'both'.
between_result = df['Age'].between(26, 35)

# to_csv(): Write DataFrame to a CSV file
# All the parameters explained of to_csv():
# path_or_buf: File path or object to write to.
# sep: Delimiter to use. Default is ','.
# index: Whether to write row names. Default is True.
df.to_csv('output.csv', index=False)

# pivot(): Reshape the DataFrame
# All the parameters explained of pivot():
# index: Column(s) to use as index.
# columns: Column(s) to use as columns.
# values: Column(s) to use for populating new frame’s values.
pivoted_df = df.pivot(index='Name', columns='Department', values='Salary')

























