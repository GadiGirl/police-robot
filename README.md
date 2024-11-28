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
  - Waveform
  - Short-Time Fourier Transform (STFT)
  - Spectrogram (in decibels)

### 4. **Emotion Label Mapping**
- Extracts emotion IDs from file names and maps them to human-readable labels.
- Visualizes the distribution of audio files across different emotions.

### 5. **Deep Learning Preparation**
- Prepares data for training by normalizing audio samples and encoding emotion labels.

---

## **Installation**
To run the project, you need to install the following dependencies:
```bash
pip install tensorflow tensorflow-datasets librosa soundfile resampy pyaudio
