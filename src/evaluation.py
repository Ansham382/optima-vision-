import time

from sklearn.metrics import (
    accuracy_score,
    f1_score
)


def train_and_evaluate(
    model,
    X_train,
    y_train,
    X_eval,
    y_eval
):
    start = time.perf_counter()

    model.fit(
        X_train,
        y_train
    )

    fit_time = time.perf_counter() - start

    start = time.perf_counter()

    predictions = model.predict(
        X_eval
    )

    predict_time = time.perf_counter() - start

    accuracy = accuracy_score(
        y_eval,
        predictions
    )

    macro_f1 = f1_score(
        y_eval,
        predictions,
        average="macro"
    )

    return {
        "model": model,
        "predictions": predictions,
        "accuracy": accuracy,
        "macro_f1": macro_f1,
        "fit_seconds": fit_time,
        "predict_seconds": predict_time
    }