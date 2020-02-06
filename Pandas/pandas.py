# import pandas library with alias
import pandas as pd

# Create logical file name
'''
Three ways:
    1. read_excel #xlsx file
    2. read_csv #csv file
    3. read_table #txt file
'''
# fname = pd.read_excel("Hello.xlsx")
# fname = pd.read_excel("Hello.xlsx",index_col=1)
'''
Index column can be anything from 0 to n-1 number of columns and it replaces that column
index_col is generally used when first variable is serial number etc.
'''

# Data type -> Logical file variable (DataFrame)
# print(type(fname)) #pandas.core.frame.DataFrame

# Missing Values
'''
Missing values are stated as nan object in variable explorer
'''
# Replace unknown values with missing values
# does not write back to the original file, only changes in variable buffer
fname = pd.read_excel("Hello.xlsx",na_values=["#","nish"])
                                              
# print fname
# print(fname) 
# prints original file with left side having index but index starts after headings
                                              
                                              
# Head function
# print(fname.head()) # By default shows 5 values only
# print(fname.head(n=10)) # Override default value                                        
# print(fname.head(10))

# Tail function -> print -5 to -1
# print(fname.tail())

'''Shape and Dimensions'''
# print(fname.shape) # Tuple of rows*columns
# print(fname.size) # total elements (rows*columns) 
# print(fname.columns) #Tells name of all the columns and data type
# BCD!! All columns are of type object always     
# print(fname.dtypes) #one data type as output -> object
# print(fname.info())
# print(fname.index) # Tells number of rows 0 - N
# print(fname.ndim) # number of variables or columns
# print(fname.memory_usage()) # Tells memory used for all the columns including index in int64
# print(pd.unique(fname['city'])) # Unique elements of the column
# print(fname.get_dtype_counts()) #deprecated
# print(fname.dtypes.value_counts())

''' Accessing single cell of the file (Element Lookup)'''
# print(fname.at(5,0))
# print(fname.iat(5,0))

# Store a column in a variable
#col = fname[1] # Cannot access by index
# col = fname['World'] # Only access by name {Why does Hello not work}
# col = fname['World','Zero'] # Column wise subsetting
# print(col)   

# Row wise access
# row = fname[start:end-1]
# row = fname[4:11]   # (Way 1: Slicing) 
# row = fname.loc[4:11] # (Way 2: loc with slicing -> end inclusive
# row = fname.loc[4] # Fetch a single row                
# row = fname.tail(1) # Access last row without iloc -> Output is DF -> Better
# Way 3: iloc
# row = fname.iloc[-1] -> Output is series
# print(row)

''' loc vs iloc
1. iloc can take integer input only
2. iloc can take -ve as well as +ve indexing
3. iloc slicing has exclusive end
4. Accessing final element of the dataset
'''

# Accessing some columns and rows only
# subset = fname.loc[1:2,'Zero']
# subset = fname.iloc[1:2,2]
# print(subset)                          

# Grouping with column name -> categorical data
# Group by multiple and take operation on all one at a time
# group = fname.groupby('city')['World','Zero'].mean()
# group = fname.groupby('city')['World','Zero'].nunique()  
# print(group) 

# Copies -> Deep and Shallow Copy -> copy() default -> deep
# shallow = fname.copy(deep=False)
# Update shallow copy
# shallow.loc[1:1,'Zero'] = 41

# Null Values
# Detect null values
# print(fname.isnull()) entire table with true and false wrt nan
# print(fname.isna()) # same as isnull
# print(fname['Zero'].isnull())
# print(fname['World'].isnull().sum())


# Handling Null Values
deep = fname.copy() # wont reflect changes in original
deep = fname[fname.isnull().any(axis=1)] # Select rows with atleast 1 nan
# deep = deep['World'].fillna(deep['World'].mean(),implace=True)
