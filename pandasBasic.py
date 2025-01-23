#using pandas for making dataframes and performing operations on it
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

average_age = df['Age'].mean()
print(f"Average age: {average_age}")

older_than_30 = df[df['Age'] > 30]
print("People older than 30:")
print(older_than_30)
