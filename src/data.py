import gzip
import struct
from pathlib import Path

import numpy as np


DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def load_idx_images(filepath):
    with gzip.open(filepath, "rb") as file:
        magic, count, rows, cols = struct.unpack(
            ">IIII", file.read(16)
        )

        if magic != 2051:
            raise ValueError("Invalid IDX image file")

        data = np.frombuffer(file.read(), dtype=np.uint8)

    expected = count * rows * cols

    if data.size != expected:
        raise ValueError("Image data size mismatch")

    return data.reshape(count, rows, cols)


def load_idx_labels(filepath):
    with gzip.open(filepath, "rb") as file:
        magic, count = struct.unpack(
            ">II", file.read(8)
        )

        if magic != 2049:
            raise ValueError("Invalid IDX label file")

        labels = np.frombuffer(file.read(), dtype=np.uint8)

    if labels.size != count:
        raise ValueError("Label count mismatch")

    return labels


def load_fashion_mnist():
    X_train = load_idx_images(
        DATA_DIR / "train-images-idx3-ubyte.gz"
    )

    y_train = load_idx_labels(
        DATA_DIR / "train-labels-idx1-ubyte.gz"
    )

    X_test = load_idx_images(
        DATA_DIR / "t10k-images-idx3-ubyte.gz"
    )

    y_test = load_idx_labels(
        DATA_DIR / "t10k-labels-idx1-ubyte.gz"
    )

    return X_train, y_train, X_test, y_test