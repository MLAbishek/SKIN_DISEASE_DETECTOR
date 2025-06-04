# Skin Cancer Detection System

A machine learning-powered web application for detecting skin cancer from dermoscopic images using Convolutional Neural Networks (CNN). The system can classify skin lesions into different categories including melanoma, nevus, and seborrheic keratosis.

## 🔬 Project Overview

This project implements a two-stage skin cancer detection system:
1. **Primary Detection**: Determines if there's an abnormality on the skin (binary classification)
2. **Secondary Classification**: If an abnormality is detected, classifies it into specific types of skin conditions

## 🎯 Features

- **Image Upload & Analysis**: Upload dermoscopic images for instant analysis
- **Multi-class Classification**: Identifies melanoma, nevus, and seborrheic keratosis
- **Web Interface**: User-friendly Flask-based web application
- **Educational Resources**: Information pages about different skin conditions
- **Doctor Directory**: Access to dermatologist information
- **Community Reviews**: User feedback and experiences
- **E-commerce Integration**: Related skincare products

## 🏗️ System Architecture

### Model Architecture
- **Input**: 64x64 RGB images
- **Primary Model**: Binary classifier (normal vs. abnormal)
- **Secondary Model**: Multi-class classifier (3 categories)
- **Framework**: TensorFlow/Keras

### Primary Model (Binary Classification)
```
Conv2D(32, 3x3, ReLU) → MaxPool2D(2x2) → 
Conv2D(32, 3x3, ReLU) → MaxPool2D(2x2) → 
Flatten → Dense(100, ReLU) → Dense(120, ReLU) → 
Dense(1, Sigmoid)
```

### Secondary Model (Multi-class Classification)
```
Conv2D(64, 3x3, ReLU) → MaxPool2D(2x2) → 
Conv2D(64, 4x4, ReLU) → MaxPool2D(2x2) → 
Flatten → Dense(150, ReLU) → Dense(3, Softmax)
```

## 📊 Dataset Information

### Training Data
- **Primary Model**: 3,377 images (2 classes: melanoma, normal)
- **Secondary Model**: 7,341 images (3 classes: melanoma, nevus, seborrheic_keratosis)

### Test Data
- **Primary Model**: 374 images
- **Secondary Model**: 2,381 images

### Data Augmentation
- Zoom range: 0.2
- Shear range: 0.2
- Horizontal flip: True
- Rescaling: 1./255

## 🚀 Installation & Setup

### Prerequisites
```bash
Python 3.10+
TensorFlow 2.x
Flask
PIL (Pillow)
NumPy
```

### Installation Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd skin-cancer-detection
```

2. **Install dependencies**
```bash
pip install tensorflow flask pillow numpy
```

3. **Download pre-trained models**
- Ensure `punnu_detector_v3.h5` and `melanoma_v3.h5` are in the project directory
- Update model paths in `app.py` if necessary

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
- Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
skin-cancer-detection/
├── app.py                 # Flask web application
├── cancer.ipynb          # Binary classification model training
├── skinmodel.ipynb       # Multi-class classification model training
├── punnu_detector_v3.h5  # Pre-trained binary model
├── melanoma_v3.h5        # Pre-trained multi-class model
├── templates/            # HTML templates
│   ├── index.html        # Main page
│   ├── ecom.html         # E-commerce page
│   ├── er.html           # Skin disease info
│   ├── ndoc.html         # Doctor directory
│   ├── rev.html          # Community reviews
│   ├── melanoma.html     # Melanoma information
│   ├── keratosis.html    # Keratosis information
│   └── nevus.html        # Nevus information
├── static/               # CSS, JS, images
└── dataset_for_training/ # Training data
```

## 🔧 Usage

### Web Interface
1. Navigate to the homepage
2. Upload a dermoscopic image
3. Click "Predict" to analyze the image
4. View the classification results

### API Endpoint
```
POST /predict
Content-Type: application/x-www-form-urlencoded
Body: image=<base64_encoded_image>
```

## 📈 Model Performance

### Primary Model (Binary Classification)
- **Final Training Accuracy**: 99.53%
- **Final Validation Accuracy**: 99.47%
- **Training Epochs**: 10

### Secondary Model (Multi-class Classification)
- **Final Training Accuracy**: 90.71%
- **Final Validation Accuracy**: 89.88%
- **Training Epochs**: 20

## 🎨 Classification Categories

### Melanoma (Class 0)
- Malignant skin cancer
- Requires immediate medical attention
- High-risk condition

### Nevus (Class 1)
- Common mole
- Generally benign
- Monitor for changes

### Seborrheic Keratosis (Class 2)
- Non-cancerous skin growth
- Common in older adults
- Usually harmless

## ⚠️ Important Disclaimers

- **Medical Advice**: This system is for educational purposes only and should not replace professional medical diagnosis
- **Accuracy**: While the model shows high accuracy, it may not be 100% reliable
- **Consultation**: Always consult with a qualified dermatologist for proper diagnosis and treatment

## 🔮 Future Improvements

- [ ] Implement more sophisticated CNN architectures (ResNet, EfficientNet)
- [ ] Add more skin condition categories
- [ ] Implement confidence scoring
- [ ] Add data visualization for predictions
- [ ] Integrate with medical databases
- [ ] Mobile application development
- [ ] Real-time image capture and analysis

## 🛠️ Technical Details

### Data Preprocessing
- Image resizing to 64x64 pixels
- Normalization (pixel values 0-1)
- Data augmentation for training robustness

### Model Training
- Optimizer: Adam
- Loss Functions: Binary crossentropy, Categorical crossentropy
- Metrics: Accuracy
- Batch size: 32

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset providers for dermoscopic images
- TensorFlow/Keras community
- Flask framework developers
- Medical professionals for guidance on skin cancer classification

## 📞 Contact

For questions, suggestions, or collaborations, please reach out through the project repository.

---

**Note**: This system is a proof-of-concept and should be used alongside professional medical advice. Always consult healthcare professionals for medical concerns.
