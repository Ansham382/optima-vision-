from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

def flatten_images(images):
    return images.reshape(images.shape[0], -1)


def scale_pixels(images):
    return images.astype("float32") / 255.0


def create_validation_split(X, y, test_size=0.20, random_state=42):
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

def fit_pca(X_train, n_components):
    pca = PCA(
        n_components=n_components,
        svd_solver="full"
    )

    X_train_pca = pca.fit_transform(X_train)

    return pca, X_train_pca


def transform_pca(pca, X):
    return pca.transform(X)