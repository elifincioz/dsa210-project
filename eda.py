import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("merged_data.csv")

# Hourly accident count
df['hour'] = pd.to_datetime(df['date']).dt.hour
sns.histplot(df['hour'], bins=24, kde=False)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.savefig("accidents_by_hour.png")
plt.clf()

# Precipitation vs Accident Count
precip_groups = df.groupby('precipitation').size().reset_index(name='accident_count')
sns.scatterplot(data=precip_groups, x='precipitation', y='accident_count')
plt.title("Precipitation vs Number of Accidents")
plt.savefig("precip_vs_accidents.png")
