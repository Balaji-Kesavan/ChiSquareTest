# Titanic Data Analysis Project

## Project Overview
This project performs exploratory data analysis on the Titanic dataset, focusing on the relationship between passenger gender and survival rates using Chi-Square statistical testing.

## Project Structure
```
Week1_titanic_project/
├── data/
│   └── titanic.csv                 # Titanic dataset
├── src/
│   ├── data_loader.py             # Data loading utilities
│   ├── eda.py                     # Exploratory Data Analysis functions
│   └── models.py                  # Model implementations (placeholder)
├── reports/
│   ├── eda_report.md              # Analysis report
│   └── figures/                   # Generated visualizations
├── main.py                        # Main script
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

## Installation
1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the main analysis:
```bash
python main.py
```

## Analysis Performed
- **Chi-Square Test**: Tests independence between Gender and Survival
- **Visualizations**: Bar charts showing survival distribution by gender
- **Statistical Significance**: p-value interpretation at 0.05 significance level

## Key Findings
The analysis tests whether gender significantly affects survival rates on the Titanic using the Chi-Square test of independence.

## Requirements
- Python 3.7+
- pandas
- matplotlib
- scipy
- numpy


Test Results :
Loading Titanic dataset...

Dataset Information:
Shape: (891, 12)
Columns: ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

==================================================
CHI-SQUARE TEST: Gender vs Survival
==================================================
Contingency Table:
 Survived    0    1
Sex               
female     81  233
male      468  109

Chi-Square Value: 260.71702016732104
p-value: 1.1973570627755645e-58
Degrees of Freedom: 1
Result: Reject H0 → Gender affects survival

Generating visualizations...

Figure saved to: reports/figures/survival_by_gender.png
Analysis complete!
