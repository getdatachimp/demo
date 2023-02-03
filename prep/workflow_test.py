import workflow
def test_prep(snapshot):
    snapshot.assert_match(repr(workflow.prep()), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_score(snapshot):
    model = pipeline.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.score(model, X_train, X_test, y_train, y_test)), 'score_output.txt')
def test_prep(snapshot):
    snapshot.assert_match(repr(workflow.prep()), 'prep_output.txt')
def test_prep(snapshot):
    snapshot.assert_match(repr(workflow.prep()), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_score(snapshot):
    model = pipeline.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.score(model, X_train, X_test, y_train, y_test)), 'score_output.txt')
def test_prep(snapshot):
    snapshot.assert_match(repr(workflow.prep()), 'prep_output.txt')
def test_train(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.train(X_train, X_test, y_train, y_test)), 'train_output.txt')
def test_score(snapshot):
    model = pipeline.fit(X_train, y_train)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.score(model, X_train, X_test, y_train, y_test)), 'score_output.txt')
def test_prep(snapshot):
    snapshot.assert_match(repr(workflow.prep()), 'prep_output.txt')
def test_trian(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.trian(X_train, X_test, y_train, y_test)), 'trian_output.txt')
def test_score(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    model = pipeline.fit(X_train, y_train)
    snapshot.assert_match(repr(workflow.score(X_train, X_test, y_train, y_test, model)), 'score_output.txt')
