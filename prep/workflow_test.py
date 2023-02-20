import workflow
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_score(snapshot):
    model = pipeline.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.score(model, X_train, X_test, y_train, y_test)), 'score_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_l(snapshot):
    snapshot.assert_match(repr(workflow.l()), 'l_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_score(snapshot):
    model = pipeline.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.score(model, X_train, X_test, y_train, y_test)), 'score_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_score(snapshot):
    model = pipeline.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.score(model, X_train, X_test, y_train, y_test)), 'score_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_prep(snapshot):
    df = df.join(predicates).drop(['Unnamed: 0'], axis=1)
    df = pd.read_csv('https://raw.githubusercontent.com/getdatachimp/demo/main/prep/borked_iris.csv')
    snapshot.assert_match(repr(workflow.prep(df, df)), 'prep_output.txt')
def test_get_data(snapshot):
    snapshot.assert_match(repr(workflow.get_data()), 'get_data_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
