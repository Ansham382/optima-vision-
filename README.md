# Optima Vision

### Clothing-Item Recognition Using Classical Machine Learning

**Course:** Applied Machine Learning (CSAI2017P)  
**Project Theme:** P06 — Clothing-item Recognition with Classical Machine Learning  
**Group Name:** Optima Vision  
**Institution:** UPES, Dehradun  
**Academic Year:** 2026–2027

---

## Team Members

| Name | Enrolment Number | GitHub Username |
|---|---|---|
| Ansh Monga | 590025575 | *To be added* |
| Raunak Singh Negi | 590022626 | Raunak-Singh-Negi |
| Prince Sai | 590022756 | *To be added* |
| Anirudh Awasthi | 590027460 | *To be added* |

> GitHub usernames will be completed once all members have joined the project repository.

---

## Overview

**Optima Vision** investigates how effectively classical machine learning algorithms can recognize clothing items from grayscale images.

The project uses the **Fashion-MNIST** dataset to compare K-Nearest Neighbors (KNN), Support Vector Machines (SVM), Random Forests, and Multilayer Perceptrons (MLP) under a common experimental protocol.

Particular emphasis is placed on **Principal Component Analysis (PCA)**, classification performance, computational efficiency, and understanding confusion between visually similar clothing categories.

---

## Dataset

**Dataset:** Fashion-MNIST  
**Source:** Zalando Research  
**Images:** 70,000  
**Classes:** 10  
**Image Resolution:** 28 × 28 pixels  
**Official Training Set:** 60,000 images  
**Official Testing Set:** 10,000 images  

Source: https://github.com/zalandoresearch/fashion-mnist

The four original IDX gzip files are stored in `data/raw/`.

The official 60,000/10,000 train-test split is preserved throughout the project.

---

## Objectives

1. Implement and understand a custom IDX dataset loader.
2. Perform exploratory data analysis on Fashion-MNIST.
3. Apply and justify pixel scaling.
4. Apply PCA and analyze cumulative explained variance.
5. Select and justify an appropriate number of PCA components.
6. Compare at least four classical ML classifiers under a common experimental protocol.
7. Evaluate models using accuracy, macro-F1, fit time, and prediction time.
8. Analyze per-class precision and recall.
9. Investigate classification errors using confusion matrices and misclassified examples.
10. Study the relationship between PCA dimensionality and classification performance.
11. Explore experimental feature/pixel-weighting strategies.
12. Explore additional extensions while preserving the required baseline pipeline.
13. Develop an optional interactive image-classification demonstration.

---

## Models

The primary model comparison will include:

- K-Nearest Neighbors (KNN)
- Support Vector Machine (RBF SVM)
- Random Forest
- Multilayer Perceptron (MLP)

Hyperparameters will be selected using validation data derived from the official training set. The official test set will be reserved for final evaluation.

---

## Project Structure

```text
optima-vision/
│
├── README.md
├── requirements.txt
├── REPRODUCIBILITY.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01-eda.ipynb
│   ├── 02-preprocessing.ipynb
│   ├── 03-models.ipynb
│  