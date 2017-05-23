import classifer
import pandas as pd

# Load simulated data set for experiment
df = pd.read_csv('../usage.txt',index_col=0)

# Create a model object using the loaded data
pred = classification.Model(df,'nograd')

# Run classification using 10-fold cross validation
# Classifier used: Logistic Regression (LR)
# Output format:List of risk scores for weak student
pred.runClassification(outputFormat='risk', models=['LR'], nFolds=10)