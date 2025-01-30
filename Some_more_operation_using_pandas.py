import pandas as pd

#Create a sample DataFrame
data = {
    'Department': ['HR', 'Engineering', 'HR', 'Engineering', 'HR'],
    'Employee' : ['Shrey', 'ishu', 'charlie', 'david', 'Eve'],
    'salary' : [50000, 60000, 70000, 90000, 10000000]
}

df = pd.DataFrame(data)

# Group by the department and calculate average salary
grouped_df = df.groupby('Department')['salary'].mean()

#Display the result
print(grouped_df)
