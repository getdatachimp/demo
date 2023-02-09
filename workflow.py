from sklearn.model_selection import train_test_split

@dchimp.task
def prep(df):
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['variety'].map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})
    return train_test_split(X, y, random_state=0)
