#Data Validator
#https://www.ers.usda.gov/data-products/food-price-outlook/food-price-outlook/#Consumer%20Price%20Index

#missing data, validating data, duplicate

#open file
import pandas as pd
import openpyxl 
#installed for error (bc 2010 excel sheet)

# Load the Excel files into dataframes
df1 = pd.read_excel('apples_2013.xlsx')
df2 = pd.read_excel('apples_2020.xlsx')

#Print 2013 apples data
print('Dataframe for 2013 apple prices')
print(df1.head())        # View the first few rows
print(df1.info())        # Get information about columns and data types
#print(df1.describe())    # Generate summary statistics

#Print 2020 apples data
print('Dataframe for 2020 apple prices')
print(df2.head())        # View the first few rows
print(df2.info())        # Get information about columns and data types
#print(df2.describe())    # Generate summary statistics

are_equal = df1.equals(df2)
differences = df1.compare(df2)

if are_equal:
    print("The two dataframes are equal.")
else:
    print("Differences between the dataframes:")
    print(differences)

differences.to_excel('differences.xlsx', index=False)
print(differences.head())
