# DDoSim – DDoS Detection & Mitigation Simulation

A real-time DDoS detection and mitigation simulation system using machine learning and interactive visualization.

## Overview

DDoSim is a comprehensive project developed as part of a Communication Networks course at MNU. It combines machine learning, network simulation, and real-time visualization to detect and mitigate DDoS attacks.

## Key Features

- **Real-time DDoS Detection**: Live network traffic replay with the CIC-DDoS2019 dataset
- **Machine Learning Model**: Random Forest classifier achieving 81% accuracy
  - Classifies benign traffic
  - Detects 12 different DDoS attack categories
- **Interactive Dashboard**: 
  - Live predictions and confidence scores
  - Attack distribution visualizations
  - Feature importance analysis
- **Network Topology Visualization**: Animated D3.js-based visualization of:
  - Packet flows
  - Attack traffic patterns
  - Mitigation actions in real-time
- **Automatic Mitigation**: 
  - IP blocking logic
  - Malicious traffic detection and blocking
  - Traffic source tracking

## Technologies Used

- **Machine Learning**: Python, scikit-learn (Random Forest)
- **Data Processing**: Pandas, NumPy
- **Visualization**: D3.js, Plotly/Matplotlib
- **Network Simulation**: CIC-DDoS2019 dataset
- **Backend**: Python
- **Frontend**: JavaScript/D3.js

## Dataset

- **CIC-DDoS2019**: A comprehensive DDoS dataset with:
  - Benign traffic samples
  - 12 DDoS attack category samples
  - Real network traffic characteristics

## Model Performance

- **Accuracy**: 81%
- **Benign Traffic Classification**: High precision
- **DDoS Attack Detection**: 12-category classification

## Project Highlights

### Data Pipeline
- Complete data processing and cleaning
- Feature extraction from network traffic
- Dataset preprocessing and normalization

### Machine Learning Model
- Random Forest classifier
- 81% classification accuracy
- Robust to new traffic patterns

### Real-time Detection System
- Live network traffic analysis
- Automatic attack classification
- Confidence scores for predictions

### Interactive Visualization
- Dashboard with live predictions
- Attack distribution charts
- Feature importance analysis
- Network topology animation using D3.js

### Mitigation System
- Automatic IP blocking
- Malicious source tracking
- Real-time mitigation actions display

## Course Information

- **Course**: Communication Networks Project
- **Institution**: MNU (Misr Nile University)

## Technologies Stack

- Python 3.x
- scikit-learn
- Pandas, NumPy
- Plotly/Matplotlib
- D3.js
- Flask/FastAPI (Backend)

## Results & Performance

- **Detection Accuracy**: 81%
- **Real-time Processing**: Live traffic analysis
- **Mitigation Response**: Automatic IP blocking with tracking
- **Visualization**: Multi-layer attack analysis

## Key Achievements

✅ Real-time DDoS detection from live network traffic
✅ Comprehensive data pipeline with cleaning and preprocessing
✅ Interactive dashboard with multiple visualization types
✅ Network topology animation showing attack patterns
✅ Automated mitigation system with IP tracking
✅ 81% accuracy across benign and 12 DDoS attack categories

## License

MIT License