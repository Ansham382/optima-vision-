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

### PCA

PCA is fitted exclusively on the model-fitting subset.

Explained-variance analysis produced the following candidate
component counts:

- 90% variance: 84 components
- 95% variance: 187 components
- 99% variance: 459 components

The final PCA component-selection criterion is to be determined.