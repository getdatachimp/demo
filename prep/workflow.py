from data_chimp_executor import execute as dchimp
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep(X_train, X_test, y_train, y_test):
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep(X_train, X_test, y_train, y_test):
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep(X_train, X_test, y_train, y_test):
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep():
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep():
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

@dchimp.task
def train(X_train, y_train):
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    return pipeline.fit(X_train, y_train)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

@dchimp.task
def train(X_train, y_train):
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    return pipeline.fit(X_train, y_train)

@dchimp.task
def score(X_test, y_test, model):
    return model.score(X_test, y_test)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep():
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep():
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

@dchimp.task
def train(X_train, y_train):
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    return pipeline.fit(X_train, y_train)

@dchimp.task
def score(X_test, y_test, model):
    return model.score(X_test, y_test)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep():
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

@dchimp.task
def train(X_train, y_train):
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    return pipeline.fit(X_train, y_train)

@dchimp.task
def score(X_test, y_test, model):
    return model.score(X_test, y_test)
import pandas as pd
from sklearn.model_selection import train_test_split

@dchimp.task
def prep():
    df = pd.read_csv('borked_iris.csv')
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

@dchimp.task
def trian(X_train, y_train):
    pipeline = make_pipeline(StandardScaler(), LogisticRegression())
    return pipeline.fit(X_train, y_train)

@dchimp.task
def score(X_test, y_test, model):
    return model.score(X_test, y_test)
