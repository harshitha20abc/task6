import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample dataset creation
np.random.seed(42)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': np.random.randint(200, 500, size=12),
    'Profit': np.random.randint(50, 150, size=12),
    'Customer_Count': np.random.randint(100, 1000, size=12)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Month'], df['Profit'], marker='s', label='Profit')
plt.title('Monthly Sales and Profit')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Customer_Count'], color='skyblue')
plt.title('Monthly Customer Count')
plt.xlabel('Month')
plt.ylabel('Customers')
plt.grid(True, axis='y')
plt.show()

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Sales'], df['Profit'], color='green')
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

