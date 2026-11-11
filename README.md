## Analysis of Diabetes Risk Factors

> **At a glance** · ~230,000 BRFSS survey records, 21 predictors · Python (cleaning) + R (analysis) · logistic regression with **AUC 0.80** · decision threshold lowered from 0.5 to 0.3 to recover diabetic cases under 17% class imbalance
>
> 📄 [English summary](diabete_summary_EN.pdf) · full report in Italian: [`diabete.pdf`](diabete.pdf)

This project investigates the main factors associated with the presence of diabetes through descriptive, inferential, and predictive statistical analysis.
The aim of the study is to explore the relationship between diabetes and a set of clinical, behavioral, demographic, and socioeconomic characteristics, identifying the variables that show the strongest associations with the disease. The analysis also includes the development of a logistic regression model to estimate the probability of diabetes for each individual.

The project combines data preprocessing, statistical analysis, data visualization, and predictive modelling, with the goal of presenting the results in a clear and accessible way.

### Objectives
The main objective of this study is to investigate which characteristics are most strongly associated with diabetes and to understand how these factors differ between individuals with and without the disease.
The analysis begins with an exploratory description of the dataset, examining the distribution of the main variables and the characteristics of the population under study. Statistical tests and correlation analysis are then used to investigate the relationships between diabetes and the potential risk factors.

A further objective is to develop a logistic regression model capable of estimating the probability that an individual has diabetes. The predictive performance of the model is evaluated using several classification measures, with particular attention to the effects of class imbalance and the choice of the classification threshold.

### Data & Analysis
The analysis is based on data from the Behavioral Risk Factor Surveillance System (BRFSS), an annual health survey conducted in the United States by the Centers for Disease Control and Prevention (CDC).
The dataset used in this project is the Diabetes Health Indicators Dataset, publicly available on Kaggle. The final dataset contains 229,781 observations and 22 variables, describing different health, behavioral, demographic, and socioeconomic characteristics of the individuals included in the survey.

The variables considered in the analysis include general, physical, and mental health status, cardiovascular and metabolic characteristics such as high blood pressure, high cholesterol and BMI, as well as lifestyle factors including physical activity, fruit and vegetable consumption, smoking and alcohol consumption. Demographic and socioeconomic variables such as age, sex, education and income are also included.

The target variable is diabetes, which is represented as a binary variable indicating whether an individual has diabetes (1) or does not have diabetes (0). In the original dataset the outcome has three levels (no diabetes, prediabetes, diabetes); prediabetes and diabetes were merged into the positive class. Duplicate records were removed, which reduces the original 253,680 rows to 229,781.

### Methodology
The analysis was developed using both Python and R, combining data preprocessing with statistical analysis and predictive modelling.
The first stage consisted of cleaning and preparing the dataset using Python. The data were checked for consistency and the variables relevant to the analysis were selected, producing the final dataset used in the statistical analysis.

The subsequent analysis was carried out in R. Exploratory data analysis was used to investigate the distributions of the variables and compare individuals with and without diabetes. Statistical tests and correlation analysis were then performed to assess the significance and strength of the relationships between diabetes and the explanatory variables.

The predictive component of the project is based on a logistic regression model. The model estimates the probability of diabetes based on the characteristics of each individual and allows these probabilities to be converted into binary classifications.

Model performance was evaluated using Accuracy, Recall, F1-score, the ROC curve and the Area Under the Curve (AUC). The dataset was divided into training and test sets, and a 10-fold cross-validation procedure was used to assess the robustness and generalizability of the model.

### Results
The analysis highlights a strong relationship between diabetes and several metabolic, cardiovascular, and demographic characteristics.
High blood pressure, high cholesterol, BMI and age are among the variables most strongly associated with the presence of diabetes. Self-reported general health also shows a particularly strong relationship with the outcome, with poorer perceived health being associated with a higher prevalence of diabetes.

The analysis also identifies socioeconomic and behavioral patterns. Higher levels of education and income are associated with a lower prevalence of diabetes, while individuals who report engaging in physical activity tend to show a lower prevalence of the disease.

From a predictive perspective, the logistic regression model achieves an AUC of 0.80, indicating good discriminatory ability. However, the dataset is characterized by class imbalance, with approximately 17% of the observations belonging to the diabetic class.

Using the standard classification threshold of 0.5 therefore tends to favor the non-diabetic class and reduces the model's ability to identify some individuals with diabetes. Lowering the threshold to 0.3 increases the sensitivity of the model and provides a more appropriate balance between sensitivity and specificity when the objective is to identify potential cases.

The results demonstrate how statistical modelling can be used not only to investigate associations between health indicators and diabetes, but also to develop predictive tools capable of identifying individuals with a higher estimated probability of having the disease.

### Limitations
The results should be interpreted considering several limitations of the study.
The data are observational, meaning that the identified relationships represent statistical associations and cannot be interpreted as causal relationships. Furthermore, many of the variables are self-reported and may therefore be affected by reporting or measurement bias.

Another important limitation is the imbalance between the diabetic and non-diabetic classes. This affects the interpretation of standard classification metrics and makes the choice of the classification threshold particularly relevant.

Finally, the dataset does not contain detailed clinical or genetic information that could potentially provide additional explanatory power and improve the predictive performance of the model.

Despite these limitations, the study provides a useful overview of the main factors associated with diabetes and demonstrates the application of statistical and predictive techniques to real-world health data.

### Repository Contents
diabete.pdf — complete report of the statistical analysis (Italian).

diabete_summary_EN.pdf — 3-page summary in English.

analisi_diabete.R — R script containing the statistical analysis, logistic regression model, and visualizations.

clean_diabetes_v2.csv — cleaned dataset used for the analysis.

data_cleaning.py — Python script for data cleaning and preprocessing.

analisi_diabete.RData — R workspace containing the objects generated during the analysis.

### How to reproduce
1. Download `diabetes_012_health_indicators_BRFSS2015.csv` from [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) into the repository folder.
2. Run `python data_cleaning.py` to produce `clean_diabetes_v2.csv` (already included, so this step is optional).
3. Open R in the repository folder and run `analisi_diabete.R`. Required packages: tidyverse, corrplot, pROC, caret, broom, reshape2, car, pscl, ResourceSelection, PRROC, smotefamily.

### Tools
The project combines Python and R for different stages of the analysis. 
Python was used primarily for data cleaning and preprocessing, while R was used for the descriptive and inferential statistical analysis, data visualization and development of the logistic regression model.
The preprocessing phase made use of libraries such as Pandas and NumPy, while Matplotlib and Seaborn were used for exploratory visualizations. The statistical analysis and modelling were conducted in R using the appropriate statistical and visualization packages.

**Author:** Sofia Menegozzo
