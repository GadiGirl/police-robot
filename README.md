# police-robot
딥러닝 기반 방범 서비스 로봇

# Speech Emotion Recognition with RAVDESS Dataset

This project aims to develop a **speech emotion recognition system** using the **RAVDESS Emotional Speech Audio** dataset. Additionally, it includes a real-time audio recording module that uploads audio files to Google Drive. The system processes audio files to extract key features such as waveforms and spectrograms, which are later used for deep learning-based emotion classification.

---

## **Dataset**
We use the [RAVDESS Emotional Speech Audio dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio), which contains high-quality audio recordings labeled with eight emotions:
- **Neutral**
- **Calm**
- **Happy**
- **Sad**
- **Angry**
- **Fearful**
- **Disgust**
- **Surprised**

---

## **Key Features of the Project**
### 1. **Real-Time Audio Recording and Uploading**
- Records 4-second audio clips continuously using `pyaudio`.
- Captures audio at a sampling rate of 44.1 kHz in stereo format.
- Automatically saves recorded audio files (`output.wav`) to a specified Google Drive folder.
- Creates the folder automatically if it does not exist.

### 2. **Google Drive Integration**
- Audio data is loaded from or saved to Google Drive for seamless integration with Colab.

### 3. **Audio Feature Extraction**
- Uses `librosa` to extract and visualize:
  - Short-Time Fourier Transform (STFT)
  - Mel Spectrogram (in decibels)
  - MFCC

### 4. **Emotion Label Mapping**
- Extracts emotion IDs from file names and maps them to human-readable labels.
- Visualizes the distribution of audio files across different emotions.

### 5. **Deep Learning Model Architecture **
The project includes a **Simplified Convolutional Neural Network (CNN)** for speech emotion recognition. The model is designed to process 2D input features (e.g., spectrograms or MFCCs) and classify them into emotion categories.

### **Model Design**
- **Input Layer**:
  - Accepts input data of shape `(height, width, channels)` (e.g., MFCC or spectrogram features).
  - Configurable `input_shape` parameter to handle different feature dimensions.

- **Convolutional Layers**:
  - Two convolutional layers with ReLU activation:
    - **First Layer**:
      - Filters: 32
      - Kernel Size: (3, 3)
      - MaxPooling: (2, 2)
    - **Second Layer**:
      - Filters: 64
      - Kernel Size: (3, 3)
      - MaxPooling: (2, 2)

- **Flatten and Dense Layers**:
  - Flattens the 2D feature maps into a 1D vector.
  - A dense layer with 128 neurons and ReLU activation.
  - Dropout (40%) for regularization and overfitting prevention.

- **Output Layer**:
  - Fully connected layer with `softmax` activation.
  - Outputs probabilities for each emotion class (`num_labels`).
