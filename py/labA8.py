import pandas as pd
# Create first DataFrame
data1 = {
'rollno': [1, 2, 3],
'name': ['Alice', 'Bob', 'Charlie'],
'total_marks': [250, 270, 300]
}
df1 = pd.DataFrame(data1)
# Create second DataFrame
data2 = {
'rollno': [4, 5],
'name': ['David', 'Eva'],
'total_marks': [280, 260]
}
df2 = pd.DataFrame(data2)
# Join along rows (axis=0)
joined_df = pd.concat([df1, df2], axis=0, ignore_index=True)
# Display the result
print("Joined DataFrame:")
print(joined_df)