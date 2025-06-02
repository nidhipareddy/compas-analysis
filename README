# 🔍 Recidivism Prediction with Machine Learning

This repository explores how machine learning can be used to build a fairer and more accurate model for predicting the likelihood of recidivism (reoffending), without heavily relying on race-based features. The project benchmarks multiple models against ethical and performance metrics and compares them to the existing COMPAS tool.

## 📌 Objective

To build a transparent and fair recidivism prediction model that improves public safety while addressing the racial bias issues seen in current tools like COMPAS.

## ⚖️ Background

COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) is a risk assessment tool used in the U.S. criminal justice system. Studies have shown that COMPAS disproportionately misclassifies Black defendants as high risk. This project aims to:

- Reduce racial bias in recidivism prediction.
- Improve model transparency and accuracy.
- Promote ethical usage of ML in criminal justice.

## 🗃️ Dataset

- Source: [ProPublica COMPAS Dataset (2016)](https://github.com/propublica/compas-analysis)
- 11,757 unique individuals in a relational SQLite database.
- Includes:
  - 6 continuous features (e.g., age, priors_count)
  - 10 categorical features (e.g., race, sex, charge degree)

## 📊 Exploratory Data Analysis (EDA)

- Racial and gender imbalance.
- Skewed age distribution (more younger individuals).
- Age negatively correlated with recidivism.
- Race was found to be a disproportionately influential feature.

## 🧠 Models Used

| Model                  | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Logistic Regression     | Baseline, interpretable, audit-friendly, but racially biased                 |
| Gradient Boosting       | Strong performance, non-linear modeling, some reduction in racial bias      |
| Multi-Layer Perceptron  | Best performance, high recall, less dependence on race                      |

## ✅ Model Performance

| Metric     | Logistic Regression | Gradient Boosting | MLP (Best Model) |
|------------|---------------------|-------------------|------------------|
| Accuracy   | 0.79                | 0.89              | **0.97**         |
| Precision  | 0.77                | 0.90              | **0.93**         |
| Recall     | 0.79                | 0.89              | **0.99**         |
| AUC-ROC    | 0.80                | 0.95              | **~0.98**        |

- The MLP model outperformed COMPAS (which has an accuracy of ~61%) in all metrics.
- Significantly lower false positive and false negative rates.

## 🔍 Feature Importance

- Most predictive features: `priors_count`, `age`, `juv_fel_count`
- Race still appears in the top features but carries less influence than in COMPAS
- MLP assigns higher risk to Caucasian individuals than COMPAS, indicating a shift in bias patterns

## 🧾 Conclusion

The Multi-Layer Perceptron model is the most accurate and equitable among the evaluated models. It:

- Achieves a 97% accuracy
- Maintains high precision and recall
- Shows reduced dependence on race and other demographic factors
- Lowers the risk of unfair misclassification compared to COMPAS

## 🔗 Resources

- 📁 Dataset: [ProPublica GitHub Repo](https://github.com/propublica/compas-analysis)
- 💻 Full code: [GitHub - compas-analysis](https://github.com/ursulaGUO/compas-analysis)

## 📚 References

- [ProPublica: How We Analyzed the COMPAS Algorithm](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm)
- [Pew Research: Racial Disparities in US Jails](https://www.pew.org/en/research-and-analysis/issue-briefs/2023/05/racial-disparities-persist-in-many-us-jails)
- [Prison Policy Initiative – Racial Disparities](https://www.prisonpolicy.org/research/racial_and_ethnic_disparities/)
- [Validation of the COMPAS Risk Assessment Tool (FSU)](https://criminology.fsu.edu/sites/g/files/upcbnu3076/files/2021-03/Validation-of-the-COMPAS-Risk-Assessment-Classification-Instrument.pdf)
