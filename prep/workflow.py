from sklearn.model_selection import train_test_split

@dchimp.task
def prep(df):
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
import pandas as pd
import pandas as pd

@dchimp.task
def get_data():
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    return df
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

@dchimp.task
def train(X_train, y_train):
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    return pipeline.fit(X_train, y_train)
