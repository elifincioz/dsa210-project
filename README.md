# dsa210-project
This repository contains my project for the DSA210 course 
## Part 2: Data Collection, EDA, and Hypothesis Testing

###  Data Collection

I'm working on this project using Istanbul traffic accident data that has been enhanced with meteorological data. The [Istanbul Metropolitan Municipality Open Data Portal](https://data.ibb.gov.tr/) makes the principal dataset accessible to the general public. It has thorough records of road accidents, including the accident's type, time, and location.

I used historical meteorological data from [Open-Meteo](https://open-meteo.com/) to enhance this data, paying particular attention to important variables like temperature, precipitation, humidity, and wind speed. To match the

---

###  Exploratory Data Analysis (EDA)

Some of the key exploratory steps taken:

- **Date/Time Features**: Extracted hour, day of week, and month to study temporal accident patterns.
- **Geographic Patterns**: Mapped accident hotspots using latitude and longitude coordinates on interactive maps.
- **Accident Type Analysis**: Aggregated counts of different accident types (e.g., vehicle-only, pedestrian-involved).
- **Weather Influence**: Merged weather data with accidents to examine how rain, temperature, or fog relate to accident frequency.

**Key Visualizations:**
- The accident count histogram by hour of the day, with the peak hours plainly visible
- A heatmap showing the incidence of accidents per district
- Scatterplots showing the number of accidents in relation to wind and precipitation

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

- Duplicate records were eliminated, and time-based interpolation was used to fill in missing weather variables.
- To get rid of outlier effects, data from national holidays was filtered out.
- Time formats were standardized, and the alignment of meteorological data and accident timestamps was guaranteed.

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
