###### Add new column ######
# New column is a substring of an existing column A
df["new_col"] = df["A"].str[-2:]

print(df)

##############################
###### Index ######
# Reset index
print(df.reset_index())

##############################
###### Regex ######
# Reset index - Is x a valid phone number?
import re
x = "123-456-7890"
print(bool(re.compile("\d{3}-\d{3}-\d{4}").match(x)))

##############################
###### Merge & Concat ######
# Merge tables on keys
pd.merge(left=df1, right=df2, left_on="customer_id", right_on="customer_id")

##############################
###### Missing Values ######
# Fill N/A of a column using mean
print(df['A'].fillna(df['A'].mean()))

#nope
