import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu

df = pd.read_csv("merged_data.csv")

# Rainy vs non-rainy
rainy = df[df['precipitation'] > 0]['accident_count']
non_rainy = df[df['precipitation'] == 0]['accident_count']

t_stat, p_val = ttest_ind(rainy, non_rainy)
print(f"T-test p-value (rain vs no rain): {p_val:.4f}")

# Weekdays vs weekends
df['weekday'] = pd.to_datetime(df['date']).dt.weekday
weekends = df[df['weekday'] >= 5]['accident_count']
weekdays = df[df['weekday'] < 5]['accident_count']

u_stat, p_val_week = mannwhitneyu(weekdays, weekends)
print(f"Mann-Whitney U test p-value (weekday vs weekend): {p_val_week:.4f}")
