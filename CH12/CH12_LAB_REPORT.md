# Lab Report 12: Regression

## Student Information
**Name:** [Uziel Beltran]

**Date:** [05/03/2026]

**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**
[A surpervised learning problem, specifically using regression to predict numerical outcomes]
**How does KNN regression differ from KNN classification?**
[In KNN regression, the output isthe average of the nearest neighbors' target values, while in classification, the output is the most common class among the neighbors.]

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**
["K" represents the number of nearest neighbors considered in making the prediction. "k=4" is chosen to balance between accuracy and overfitting.]

**In your own words, explain how the model produces a prediction for a new day.**
[The model finds the k nearest historical days based on today's conditions and averages their loaf counts to make a prediction.]

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**
[Separating features and target is crucial to train the model on inputs (features) and validate it through outputs (target).]

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**
[The input to model.predict() must be a 2D array because the model is designed to handle multiple samples at once. Each row represents a separate sample, and each column represents a feature.]

**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**
[KNN is a "lazy learner" that mostly just stores the data]

**Why do we use `.values` when extracting columns from the DataFrame?**
[We use .values when extracting columns from a DataFrame to convert them into a NumPy array.]

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**
[ overfitting, sensitive to noise]

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**
[every prediction would be the global average]

**How would you decide what value of k is best for a given dataset?**
[ cross-validation, error metrics on a validation set]

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**
[ features with larger ranges dominate the distance calculation]

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**
[Day 1:
Weather: 5 (Very good weather)
Weekend/Holiday: 0 (Weekday)
Game On: 0 (No game)
Day 2:
Weather: 1 (Poor weather)
Weekend/Holiday: 0 (Weekday)
Game On: 0 (No game)
Scenario:
Both days have identical values for weekend_holiday and game_on, but very different weather conditions.When the model calculates which days are "nearest," the large weather difference can lead to decisions more influenced by weather than intended, which may not always be relevant to loaf sales. ]

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**
[Implement feature scaling (e.g., normalization or standardization) to ensure all features contribute proportionately to the distance calculation. This would make weather, weekend_holiday, and game_on have comparable impacts on determining similarity.
]

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**
[KNN regression can perform poorly when predicting conditions that are significantly different from any historical data. It's sensitive to outliers and noise, and the accuracy decreases with sparse data in high dimensions. Scenario: Predicting sales for a day with extreme weather that hasn't been observed before might lead to an inaccurate prediction, as there are no similar historical points.]

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**
[With more data, KNN predictions tend to improve as the model has access to a wider variety of historical conditions to match against. However, more data can also slow down prediction time as the model must search through more points to find the nearest neighbors.]

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**
[Temperature, season, local events, day of week, social media buzz]

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**
[: KNN is computationally expensive at prediction time since it compares the query instance to all training samples. This leads to slower predictions. 

**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**
[If the average is 70.5 then the 4 days being averaged must also be close to 70.5. I choose days 3,15,18,19
which loaf counts are 72,70,70,75. The average of the 4 is 71.75 which is not equal to 70.5]

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**
[ consistency, scalability, data-driven decisions, reduced waste]

**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**
[ predict slightly under, use a different loss function, factor in cost of waste vs. lost sales]
