import workflow
def test_tain(snapshot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    snapshot.assert_match(repr(workflow.tain(X_train, X_test, y_train, y_test)), 'tain_output.txt')
