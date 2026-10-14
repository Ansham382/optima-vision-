from sklearn.linear_model import LogisticRegression


def create_logistic_regression():
    return LogisticRegression(
        max_iter=1000,
        random_state=42
    )