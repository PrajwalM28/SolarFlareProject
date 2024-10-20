## Solar Flare Prediction using Machine Learning

This project aims to develop a predictive model for forecasting solar flares—intense bursts of energy from the Sun’s surface. Accurate prediction of these events is crucial for mitigating their impacts on Earth's technological systems.

## Dataset

- **Source**: Kaggle
- **Type**: Time-series data spanning multiple years
- **Features**: Sunspot counts, magnetic field measurements, historical flare data.
- **Size**: ~1.5 GB, comprising 1,000,000+ data points.

The dataset is preprocessed to ensure high quality and consistency.

## Model Development

The project uses an LSTM (Long Short-Term Memory) model, well-suited for time-series forecasting:

- **Loss Function**: Mean Squared Error (MSE)
  
  \[
  \text{MSE} = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)^2
  \]
  
- **Optimizer**: Adam with a learning rate of 0.001.

The model is trained over 50 epochs with early stopping to avoid overfitting, using an 80/20 train-validation split.

## Data Analysis

Key analyses include:

- **Correlation Coefficient** between sunspot numbers and flare occurrences: \( r = 0.87 \)
- **Feature Importance**: Magnetic field strength is the most predictive feature, contributing to 65% of the model’s decision-making process.
- **Visualization**: Heatmaps and time-series plots illustrate the correlation between different solar parameters and flare events.

## Model Evaluation

Performance metrics:

- **Training Loss**: 0.0012
- **Validation Loss**: 0.0018
- **Accuracy**: ~76% in predicting flare occurrences.

Loss curves show steady convergence without signs of overfitting.

## Deployment

The model can be integrated into space weather forecasting systems. It will provide predictions for potential solar flares with lead times up to 72 hours.
