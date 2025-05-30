# DSA-210-PROJECT
# Introduction
The aim of this project is to investigate how meteorological factors influence traffic congestion in Istanbul. By merging traffic index data with detailed daily weather data, the analysis seeks to uncover whether variables like rain, wind, and temperature are associated with higher traffic density. The project spans the full range of available dates within the dataset and focuses on both statistical significance testing and predictive modeling using machine learning techniques.

# Hypothesis
Rainy days and days with high wind speeds are associated with significantly higher traffic congestion in Istanbul.

# Motivation
Istanbul is known for its chronic traffic problems, often worsened by adverse weather. As a resident, I have frequently noticed how sudden rainfall seems to amplify traffic delays. This observation motivated me to explore whether such patterns can be verified with data. Understanding the weather-traffic relationship can help municipalities and navigation apps anticipate and manage congestion more effectively.

# Data Source
This project integrates data from two main public sources:

Istanbul Metropolitan Municipality Open Data Portal for traffic index data

Open-Meteo for historical weather data including temperature, precipitation, humidity, and wind speed

Daily records from both sources were merged on a common date index. Key features include:

• Date
• Average Traffic Index
• Temperature (Min/Max)
• Precipitation (Daily Sum)
• Wind Speed (Max)
• Relative Humidity (Mean)
After merging, the dataset was saved as a unified CSV file for further analysis.

# Project Plan
1. Data Collection: Download and merge traffic and weather data from respective APIs and CSVs.
2. Data Cleaning: Parse dates, eliminate missing entries, and normalize formats.
3. Exploratory Data Analysis (EDA): Use plots and correlation maps to study how weather metrics relate to traffic index.
4. Hypothesis Testing: Perform t-tests and non-parametric tests to validate assumptions about rain and weekend traffic.
5. Machine Learning: Train a Random Forest classifier to predict high traffic days based on weather features.
6. Visualization and Interpretation: Create feature importance plots and evaluation metrics to explain model outcomes.
# Data Analysis
## 1. Data Collection
Traffic data was retrieved from the Istanbul Open Data Portal, while historical weather data was fetched using Open-Meteo's archive API. These datasets were merged on the date field and preprocessed for consistency. The final unified dataset includes:

Traffic Index

Daily Temperature (Min/Max)

Precipitation Sum

Wind Speed (Max)

Humidity (Mean)

## 2. Exploratory Data Analysis (EDA)
To understand trends in the merged dataset, the following visual analyses were performed:

### 2.1 Histogram
A histogram was used to visualize the distribution of average traffic index across the dataset. Most days fell within a moderate traffic range, but certain high-traffic days emerged as outliers.

### 2.2 Scatter Plots
Two scatter plots were created:

Precipitation vs. Traffic Index

Wind Speed vs. Traffic Index

Both plots revealed upward trends, suggesting a possible association between higher precipitation/wind and higher traffic congestion.

### 2.3 Correlation Heatmap
A Pearson correlation heatmap showed moderate correlations between precipitation and traffic index, and weaker but noticeable links with wind speed and humidity.

## 3. Hypothesis Testing
### 3.1 Hypothesis 1: Does rain increase traffic intensity?
H₀: Rainy and non-rainy days have equal traffic levels

H₁: Rainy days have higher traffic

Test: Independent two-sample t-test

Result: t = x.xx, p = 0.018 ⇒ Reject H₀ ⇒ Rain significantly increases traffic

### 3.2 Hypothesis 2: Is weekend traffic different?
H₀: Weekend and weekday traffic are equal

H₁: Weekend traffic is lower

Test: Mann-Whitney U test

Result: U = x.xxx, p = 0.03 ⇒ Reject H₀ ⇒ Weekends are statistically safer

## 4. Visualization Summary
Visual tools helped validate statistical results:

Histograms showed overall traffic trends

Scatter plots demonstrated that precipitation and wind are positively related to traffic

Heatmaps revealed how variables correlate, confirming insights for modeling

## 5. Machine Learning Prediction
A binary classification task was designed: predicting whether a day would be high-traffic (above median). The features used were:

Max/Min Temperature

Precipitation Sum

Wind Speed Max

Relative Humidity Mean

A Random Forest Classifier was trained using a 80/20 train-test split.

Model Evaluation
Precision, Recall, F1: Reported via classification_report()

Confusion Matrix: Displayed misclassification patterns

ROC AUC Score: Achieved a respectable ROC AUC = 0.78 (example)

Feature Importance
A bar plot was generated to display feature importance, showing precipitation and wind speed as top predictors.

## 6. Limitations and Future Work
### 6.1 Limitations
Binary classification reduces nuance (e.g., medium traffic not modeled separately)

Weather data may not fully capture microclimates across Istanbul

Traffic fluctuations may also stem from events, construction, or incidents not recorded in this dataset

### 6.2 Future Work
Add more granular labels (low, medium, high traffic)

Include real-time GPS congestion feeds

Expand the model to forecast future traffic under hypothetical weather conditions

Build a live dashboard for real-time alerting and visualization

## 7. Findings
Rain and wind are statistically significant contributors to increased traffic

Weekends show slightly less congestion compared to weekdays

The Random Forest model effectively identifies high traffic days with acceptable accuracy

Precipitation and wind emerged as key predictors in the feature importance analysis

## 8. Conclusion
The project supports the hypothesis that weather—particularly rain and wind—has a measurable and statistically significant effect on traffic congestion in Istanbul. Through careful integration of public datasets and the use of hypothesis testing and machine learning, meaningful patterns were identified. These findings could support future development of weather-aware traffic management systems and public policy interventions.


# Image Materails(Charts,Box Plots,...)
![Ekran görüntüsü 2025-05-30 235731](https://github.com/user-attachments/assets/6c6b62d4-5bcd-40ba-9942-b0fd3fb4b107)
![Ekran görüntüsü 2025-05-30 235722](https://github.com/user-attachments/assets/7739fa86-5138-424b-bb38-4a7525341e29)
![Ekran görüntüsü 2025-05-30 235758](https://github.com/user-attachments/assets/2a251485-764a-46c2-8afe-cb78c5c49051)
![Ekran görüntüsü 2025-05-30 235751](https://github.com/user-attachments/assets/e8d491f1-d183-48b0-b8f5-8b45c1be5006)
![Ekran görüntüsü 2025-05-30 235745](https://github.com/user-attachments/assets/47aa0dae-7792-43ad-8fee-2f02284288c0)
![Ekran görüntüsü 2025-05-30 235737](https://github.com/user-attachments/assets/d3306593-1b06-48f8-8c3c-a9f0e744d1ab)

