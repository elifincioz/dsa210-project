# dsa210-project
This repository contains my project for the DSA210 course 
## Part 2: Data Collection, EDA, and Hypothesis Testing

###  Data Collection

For this project, I am working with traffic accident data in Istanbul, enriched with weather data. The primary dataset is publicly available from the [Istanbul Metropolitan Municipality Open Data Portal](https://data.ibb.gov.tr/). It includes detailed records of traffic accidents, including time, location, and type of accident.

To enrich this data, I integrated historical weather data from [Open-Meteo](https://open-meteo.com/), focusing on key variables such as temperature, precipitation, humidity, and wind speed. The weather data is matched by time and district to align with the accident records.

All datasets were collected using APIs and CSV downloads, and combined using pandas.

---

###  Exploratory Data Analysis (EDA)

Some of the key exploratory steps taken:

- **Date/Time Features**: Extracted hour, day of week, and month to study temporal accident patterns.
- **Geographic Patterns**: Mapped accident hotspots using latitude and longitude coordinates on interactive maps.
- **Accident Type Analysis**: Aggregated counts of different accident types (e.g., vehicle-only, pedestrian-involved).
- **Weather Influence**: Merged weather data with accidents to examine how rain, temperature, or fog relate to accident frequency.

**Key Visualizations:**
- Histogram of accident counts by hour of day (peak hours clearly visible)
- Heatmap of accident frequency across districts
- Scatterplots of accident count vs. precipitation and wind speed

---

###  Hypothesis Testing

Several hypothesis tests were conducted to validate assumptions:

**1. Does rain significantly increase the number of accidents?**

- **H₀**: Rainy days and non-rainy days have equal mean accident counts.
- **H₁**: Rainy days have higher accident counts.
- **Method**: Two-sample t-test  
- **Result**: *p-value = 0.018*, reject H₀ ⇒ Rain has a statistically significant effect.

**2. Are weekends safer than weekdays?**

- **H₀**: Mean accident count is equal on weekdays and weekends.
- **H₁**: Weekend accident counts are lower.
- **Method**: Mann-Whitney U test  
- **Result**: *p-value = 0.03*, reject H₀ ⇒ Weekends are statistically safer.

---

###  Data Cleaning Notes

- Removed duplicate records and filled missing weather values using time-based interpolation.
- Filtered out data from national holidays to eliminate outlier effects.
- Standardized time formats and ensured alignment between accident timestamps and weather data.

---

###  Summary of Key Findings

- **Temporal Trends**: Most accidents occur during morning (7–9 AM) and evening (5–7 PM) rush hours.
- **Weather Impact**: Precipitation and strong winds significantly correlate with increased accident rates, especially in urban centers.
- **Geographic Insights**: Districts like Kadıköy, Şişli, and Üsküdar consistently report higher accident frequencies.
- **Accident Types**: Rear-end collisions are the most common, especially during rainy days.
- **Seasonal Effects**: Winter months show a small but notable increase in accident frequency compared to summer.

---

###  Strengths of the Analysis

- **Rich Dataset Integration**: Combining weather and traffic data provided more context to draw meaningful insights.
- **Temporal and Spatial Analysis**: Trends were analyzed both in time and across locations.
- **Statistical Rigor**: Hypothesis testing ensured analytical conclusions were not anecdotal.

---

###  Limitations and Challenges

- **Missing Data**: Some weather observations were missing or inconsistent, especially from rural stations.
- **Granularity**: Some accident records had limited information about exact cause or vehicle type.
- **Causality**: Correlation observed between weather and accidents does not imply direct causation.

---

###  Next Steps (For Part 3)

- **Feature Engineering**: Create binary features for "rainy day", "weekend", and "peak hour" to improve prediction accuracy.
- **Machine Learning Models**: Apply classification models (e.g., decision trees, random forest) to predict accident likelihood based on time, weather, and location.
- **Model Evaluation**: Use metrics like accuracy, F1 score, and AUC to evaluate prediction success.
- **Dashboard Creation**: Build an interactive web-based dashboard to visualize real-time accident predictions.
