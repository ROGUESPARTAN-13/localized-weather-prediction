import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/seattle-weather.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nWeather Count:")
print(df['weather'].value_counts())
plt.figure(figsize=(8,5))
sns.countplot(x='weather', data=df)

plt.title("Weather Distribution")
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df['temp_max'], kde=True)

plt.title("Maximum Temperature Distribution")
plt.xlabel("Maximum Temperature")
plt.ylabel("Frequency")

plt.show()
plt.figure(figsize=(8,5))

sns.heatmap(
    df.select_dtypes(include='number').corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()