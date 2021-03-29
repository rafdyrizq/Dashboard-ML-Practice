# Basic Operations
import pandas as pd
import numpy as np

# ML Models
from sklearn.linear_model import LogisticRegression

# Feature Engineering
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler
import category_encoders as ce # untuk ordinal dan binary encoder
from sklearn.impute import SimpleImputer

# Evaluation
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import f1_score

# Model
import pickle
import joblib

# 1. DATA
titanic_train = pd.read_csv('titanic_train.csv')

# 2. PREPROCESS
# pipeline berisi imputing lalu binary encoding untuk 'embark_town' nanti
binary_encoder_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('binary encoder', ce.BinaryEncoder())
])

# ordinal mapping untuk 'class' nanti
ordinal_mapping = [
    {'col':'class',
    'mapping':{None:0, 'First':1, 'Second':2, 'Third':3}}
]

ordinal_encoder = ce.OrdinalEncoder(cols=['class'], mapping=ordinal_mapping)

# transformer 
transformer = ColumnTransformer([
    ('imputer', SimpleImputer(strategy='median'), ['age']),
    ('one hot encoder', OneHotEncoder(drop='first'), ['sex','alone']),
    ('ordinal encoder', ordinal_encoder, ['class']),
    ('binary encoder', binary_encoder_pipeline, ['embark_town'])
], remainder='passthrough')

# 3. DATA SPLITTING
X = titanic_train.drop(columns='label')
y = titanic_train['label']

# 4. MODEL SELECTION
model = LogisticRegression(solver='liblinear', random_state=2020)

estimator = Pipeline([
    ('prepocess', transformer),
    ('clf', model)
])

hyperparam_space = {
    'clf__C':[100, 10, 1, 0.1, 0.01, 0.001],
    'clf__solver':['liblinear','newton-cg']
}

skfold = StratifiedKFold(n_splits=5)

grid_search = GridSearchCV(
    estimator, 
    param_grid = hyperparam_space,
    cv = skfold,
    scoring = 'f1',
    n_jobs = -1
)

grid_search.fit(X,y)

# 5. MODEL PICKLING
# model pickle
grid_search.best_estimator_.fit(X,y) # final model

# saving model
filename = 'Titanic_Final.sav'
pickle.dump(grid_search.best_estimator_,open(filename,'wb'))
