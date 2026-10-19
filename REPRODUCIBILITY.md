# Reproducibility

## Environment

Operating System: Windows
Python Version: To be recorded
Environment: Python virtual environment (.venv)

## Installation

python -m venv .venv
python -m pip install -r requirements.txt

## Dataset

Fashion-MNIST, official Zalando Research release.

Files:
- train-images-idx3-ubyte.gz
- train-labels-idx1-ubyte.gz
- t10k-images-idx3-ubyte.gz
- t10k-labels-idx1-ubyte.gz

Location: data/raw/

## Random Seeds

To be documented during model development.

## Execution Order

To be documented as notebooks are implemented.

## Hardware and Runtime

To be measured during experimentation.

## Preprocessing

### Image Representation

Each Fashion-MNIST image is flattened from 28 x 28 pixels into
a 784-dimensional feature vector.

### Pixel Scaling

Original uint8 pixel intensities in the range [0, 255] are
normalized to [0, 1] by division by 255.

### Validation Split

The official 60,000-image training set is divided into:

- Model-fitting subset: 48,000 images
- Validation subset: 12,000 images

The split is stratified by class and uses random seed 42.

The official 10,000-image test set remains separate.

### PCA Component Selection

PCA is fitted exclusively on the model-fitting subset.

The project uses a 95% cumulative explained-variance threshold
for its primary PCA representation.

The minimum number of components satisfying this threshold was
187, reducing the original 784-dimensional representation to
187 dimensions.

Validation data is transformed using the PCA model fitted on the
model-fitting subset. The validation data is not used to fit PCA.

## Checkpoint 1 Baseline

Model: Logistic Regression

PCA components: 187

PCA selection criterion:
Minimum number of components required to retain at least
95% cumulative explained variance.

Model-fitting samples: 48,000

Validation samples: 12,000

Official test samples: 10,000

Random seed: 42

The official test set was not used for PCA fitting or model
hyperparameter selection.
## Model Selection

Hyperparameter selection was performed exclusively using the
validation subset.

### KNN

Candidate k values:

3, 5, 7, 9, 11

Selected:

k = 5

Validation accuracy: 0.866167

### RBF SVM

Candidate C values:

1, 10, 100

Candidate gamma values:

scale, 0.01, 0.001

The hyperparameter search used a stratified 15,000-example
subset of the model-fitting data.

Selected:

C = 10  
gamma = scale

Search-stage validation accuracy: 0.891250

The selected configuration was subsequently trained using the
complete model-fitting subset.

### Random Forest

Selected configuration:

n_estimators = 200  
max_depth = 40

Validation accuracy during tuning: 0.869583

### MLP

Selected architecture:

(128, 64)

Activation:

tanh

Maximum iterations:

200

Validation accuracy during initial tuning:

0.893750

The initial 100-iteration model reached the maximum iteration
limit before satisfying the optimizer convergence criterion.
A follow-up convergence experiment was therefore performed.