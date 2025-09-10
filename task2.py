import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV file
# CSV file same folder-il "data.csv" enn save cheythal mathi
data = pd.read_csv("data.csv")

# Step 2: Show first 5 rows
print("Sample Data:")
print(data.head())

# Step 3: Basic statistics
print("\nColumn Average:")
print(data.mean(numeric_only=True))  # only numeric columns

# Step 4: Bar Chart
data['Marks'].plot(kind='bar', title="Student Marks")  # Marks column example
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()

# Step 5: Scatter Plot
plt.scatter(data['Hours_Studied'], data['Marks'])  # 2 columns example
plt.title("Hours vs Marks")
plt.xlabel("Hours_Studied")
plt.ylabel("Marks")
plt.show()

# Step 6: Heatmap (Correlation)
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
