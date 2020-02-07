## Handling Missing Values

* Change working directory

```
import os
os.chdir("D:\Nish")
```

* Identify missing values in entire dataset
```
print(logicalname.isna())
print(logicalname.isnull())
```

* Identify number of NaN values in each columns
```
print(logicalname.isna().sum())
```

* Subsetting **rows** with one or more missing values: Subset has all the columns
```
missing = lname[lname.isna().any(axis=1)]
```

* Replacing Missing Values

**1. Numerical Variable:** replaced with measures of central tendency (excluding NaN) which can be found using `lname.describe()`
```
lname['col'].fillna(lname['col'].mean(), inplace=True)
```

> Note: for mode, we need mode()[0]

**2. Categorical Variable:** replaced with maximum frequency category

> value_counts() function returns each categorical data and their counts in descending order

```
lname['col'].fillna(lname['col'].value_counts().index[0],inplace=True))
```

### Handling all missing data at once using Lambda Functions

```
lname = lname.apply(lambda x: x.fillna(x.mean()) if x.dtype=='float' else x.fillna(x.value_counts().index[0]))
```
