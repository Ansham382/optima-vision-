from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier


def create_logistic_regression():
    return LogisticRegression(
        max_iter=1000,
        random_state=42
    )


def create_knn(n_neighbors):
    return KNeighborsClassifier(
        n_neighbors=n_neighbors
    )


def create_svm(C, gamma):
    return SVC(
        kernel="rbf",
        C=C,
        gamma=gamma
    )


def create_random_forest(
    n_estimators,
    max_depth,
    random_state=42
):
    return RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1
    )


def create_mlp(
    hidden_layer_sizes,
    activation,
    max_iter,
    random_state=42
):
    return MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        max_iter=max_iter,
        random_state=random_state
    )