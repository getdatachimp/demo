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
