# Student Disengagement Early-Warning System — 35% Phase

## Scope

This ZIP contains the first 35% project phase covering four technical roles:

1. Data Engineer
2. EDA Engineer
3. ML Engineer
4. Evaluation Engineer

## Included Work

### Data Engineer
- Synthetic dataset generation
- Data preprocessing and validation
- Raw and cleaned datasets

### EDA Engineer
- Exploratory data analysis
- Engagement/disengagement visualisations
- Correlation matrix

### ML Engineer
- Random Forest model training
- Feature importance
- Test predictions
- Model metrics
- Saved trained model

### Evaluation Engineer
- Attendance-only baseline
- Baseline/model comparison
- Accuracy, precision, recall and F1 evaluation

## Not Included in This 35% Package

The following later-phase deliverables are intentionally excluded:
- Streamlit dashboard
- Failure analysis
- Edge-case testing
- Workflow experiment
- Stakeholder validation documentation
- Risk register
- User guide
- Final project report
- Automated tests
- Architecture/data-schema documentation

These belong to later project phases.

## Main Execution Order

```text
python src/data_engineer_data_generator.py
python src/data_engineer_preprocessing.py
python notebooks/eda_engineer.py
python notebooks/evaluation_engineer_baseline.py
python models/ml_engineer.py
python notebooks/evaluation_engineer_model_comparison.py
```

The dataset in this package is synthetic and is intended for technical feasibility demonstration.
