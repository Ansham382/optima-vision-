# Reproducibility

## Environment

**Operating System:** Windows  
**Python Version:** Python 3.14.2  
**Environment:** Python virtual environment (`.venv`)

Create the environment from the repository root:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the pinned dependencies:

```bash
python -m pip install -r requirements.txt
```

Start JupyterLab:

```bash
jupyter lab
```

---

## Dataset

The project uses the official Fashion-MNIST release from Zalando
Research.

The following original IDX gzip files are stored in `data/raw/`:

- `train-images-idx3-ubyte.gz`
- `train-labels-idx1-ubyte.gz`
- `t10k-images-idx3-ubyte.gz`
- `t10k-labels-idx1-ubyte.gz`

The files were downloaded manually using a web browser and are not
downloaded programmatically by the project.

The official Fashion-MNIST split is preserved:

- Training images: 60,000
- Test images: 10,000
- Classes: 10

---

## IDX Loading

`src/data.py` implements the IDX loader used by the project.

Expected dataset shapes are:

- Training images: `(60000, 28, 28)`
- Training labels: `(60000,)`
- Test images: `(10000, 28, 28)`
- Test labels: `(10000,)`

The official training set contains 6,000 examples from each class.

---

## Preprocessing

### Image Representation

Each 28x28 image is flattened into a 784-dimensional feature vector.

### Pixel Scaling

Original unsigned 8-bit pixel intensities in the range `[0,255]`
are converted to floating-point values in the range `[0,1]` by
division by 255.

### Training and Validation Split

The official 60,000-image training set is divided into:

- Model-fitting subset: 48,000 images
- Validation subset: 12,000 images

The split is stratified by class.

The official 10,000-image test set remains separate.

---

## Random Seeds

The primary reproducibility seed used throughout applicable
stochastic operations is:

`random_state = 42`

It is used for:

- the stratified training-validation split;
- creation of the stratified SVM hyperparameter-search subset;
- Random Forest initialization;
- MLP initialization.

KNN is deterministic for the fixed data and parameters used here.

The RBF SVM configuration used by the project does not require a
random seed for its standard deterministic fitting procedure.

---

## PCA

PCA is fitted exclusively on the model-fitting subset. Validation
and official test data are transformed using the PCA model learned
from the fitting subset and are never used to fit PCA.

Explained-variance analysis produced:

- 90% cumulative variance: 84 components
- 95% cumulative variance: 187 components
- 99% cumulative variance: 459 components

The primary representation uses the minimum number of principal
components required to retain at least 95% cumulative explained
variance.

**Selected PCA components: 187**

This reduces the original representation from 784 to 187 dimensions.

---

## Checkpoint 1 Baseline

The Checkpoint-1 baseline uses Logistic Regression on the
187-component PCA representation.

Results:

- Official test accuracy: `0.8451`
- Fit time: `42.8113` seconds
- Official test prediction time: `0.0064` seconds

The official test set was not used for PCA fitting or
hyperparameter selection.

---

## Hyperparameter Selection

All hyperparameter selection was performed using validation data.

### K-Nearest Neighbours

Candidate values:

`k = [3, 5, 7, 9, 11]`

Selected configuration:

`k = 5`

Tuning-stage results:

- Validation accuracy: `0.866167`
- Macro-F1: `0.865841`

### RBF Support Vector Machine

Candidate `C` values:

`[1, 10, 100]`

Candidate `gamma` values:

`["scale", 0.01, 0.001]`

For computational efficiency, the SVM hyperparameter search used a
stratified 15,000-example subset of the model-fitting data. The
subset contained 1,500 examples from each of the ten classes.

Selected configuration:

- `C = 10`
- `gamma = "scale"`

Search-stage validation accuracy:

`0.891250`

After selection, this configuration was trained using the complete
48,000-example model-fitting subset.

### Random Forest

Selected configuration:

- `n_estimators = 200`
- `max_depth = 40`
- `random_state = 42`

Tuning-stage results:

- Validation accuracy: `0.869583`
- Macro-F1: `0.867920`

### Multilayer Perceptron

Selected configuration:

- Hidden layers: `(128, 64)`
- Activation: `tanh`
- `max_iter = 200`
- `random_state = 42`

The initial search used `max_iter=100`. The selected configuration
reached this maximum before satisfying the optimizer convergence
criterion, producing a convergence warning.

A follow-up convergence check increased the maximum to 200. In that
run the optimizer converged naturally after **96 iterations**, so
200 is retained as an upper limit rather than a requirement that
training execute all 200 iterations.

Convergence-check results:

- Validation accuracy: `0.893750`
- Macro-F1: `0.894030`
- Fit time: approximately `27.99` seconds
- Actual iterations: `96`

---

## Official Test Results

The selected configurations were trained using the common
187-component PCA representation and evaluated on the official
Fashion-MNIST test set.

| Model | Accuracy | Macro-F1 | Fit Time (s) | Predict Time (s) |
|---|---:|---:|---:|---:|
| RBF SVM | 0.8991 | 0.898995 | 58.066174 | 20.218233 |
| MLP | 0.8758 | 0.875871 | 26.378397 | 0.013070 |
| KNN | 0.8579 | 0.857424 | 0.030468 | 1.068207 |
| Random Forest | 0.8575 | 0.855470 | 15.526144 | 0.092412 |

The RBF SVM achieved the strongest official-test predictive
performance.

---

## Class-Level Evaluation

For the selected RBF SVM, the principal weakness was the Shirt
class:

- Precision: `0.746098`
- Recall: `0.7170`
- F1-score: `0.731260`

Important observed confusions included:

- Shirt -> T-shirt/top: 117
- T-shirt/top -> Shirt: 98
- Coat -> Pullover: 89
- Shirt -> Pullover: 79
- Pullover -> Coat: 68
- Pullover -> Shirt: 65

Detailed results are stored in:

`results/classification_report.csv`

The confusion-matrix and misclassified-image figures are stored in:

`results/figures/`

---

## PCA Component Sweep

The required PCA dimensionality experiment evaluates the selected
classifier using:

`[10, 25, 50, 100, 200]`

principal components.

The complete numerical results are stored in:

`results/pca_sweep.csv`

The corresponding accuracy-versus-components figure is stored in:

`results/figures/pca_components_vs_accuracy.png`

---

## Execution Order

From a clean checkout, install the dependencies and ensure the four
Fashion-MNIST gzip files are present in `data/raw/`.

Then run the notebooks from top to bottom in this order:

1. `notebooks/01-eda.ipynb`
2. `notebooks/02-preprocessing.ipynb`
3. `notebooks/03-models.ipynb`
4. `notebooks/04-evaluation.ipynb`

Generated result files are written to `results/`.

---

## Hardware and Runtime

**Processor:** AMD Ryzen 7 5800H with Radeon Graphics  
**RAM:** 16 GB DDR4
**GPU:** NVIDIA GeForce RTX 3050 Ti Laptop GPU; AMD Radeon Graphics
**GPU Usage:** Not used for model training; experiments were CPU-based.
**Expected complete runtime:** Approximately 14–15 minutes for all four notebooks when run from top to bottom on the hardware above.

The project is designed to run using CPU-based classical
machine-learning implementations.

---

## Manual Steps

The following steps are not automated:

1. Downloading the four Fashion-MNIST IDX gzip files using a web
   browser.
2. Placing the four files in `data/raw/`.
3. Creating and activating the Python virtual environment.
4. Installing packages from `requirements.txt`.
5. Running the notebooks in the documented order.

---

## Expected Sources of Variation

Model accuracy should be reproducible when the documented data,
random seeds, software versions and experimental procedure are used.

Wall-clock fit and prediction times are not expected to reproduce
exactly because they depend on processor performance, available
system resources and background workload.

The MLP optimizer may show small runtime differences between
executions. The configured maximum is 200 iterations; the documented
convergence-check run terminated naturally after 96 iterations.

No test-set result is used to choose model hyperparameters.