# 🧠 Next Word Predictor

A modern web application powered by LSTM neural networks that predicts the next word in a sequence based on Shakespeare's Hamlet.

## ✨ Features

- **Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- **LSTM Neural Network**: Advanced deep learning model trained on Shakespeare's text
- **Real-time Predictions**: Instant next-word predictions with visual feedback
- **Interactive Sidebar**: Model information and usage tips
- **Error Handling**: Robust error handling with user-friendly messages
- **Mobile Responsive**: Works seamlessly on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project files**

   ```bash
   cd LSTM\ GRU
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure you have the model files**
   - `next_word_lstm.keras` (trained LSTM model)
   - `tokenizer.pickle` (vocabulary tokenizer)

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🎯 How to Use

1. **Enter Text**: Type a sequence of words in the input field
2. **Click Predict**: Hit the "🚀 Predict Next Word" button
3. **View Results**: See the predicted next word and complete sequence

### Example Inputs

- "to be or not"
- "hamlet is"
- "the king of"

## 🏗️ Model Architecture

- **Input Layer**: Embedding layer for word representations
- **Hidden Layers**: 2 LSTM layers with dropout for regularization
- **Output Layer**: Dense layer with softmax activation
- **Vocabulary Size**: 4,818 unique words from Hamlet
- **Sequence Length**: 13 words

## 📁 Project Structure

```
LSTM GRU/
├── app.py                 # Main Streamlit application
├── exp.ipynb             # Training notebook
├── requirements.txt      # Python dependencies
├── next_word_lstm.keras  # Trained model file
├── tokenizer.pickle      # Vocabulary tokenizer
├── hamlet.txt           # Training data
└── README.md            # This file
```

## 🛠️ Technical Stack

- **Backend**: Python, TensorFlow/Keras
- **Frontend**: Streamlit
- **ML Architecture**: LSTM Neural Network
- **Data**: Shakespeare's Hamlet text

## 🎨 UI Features

- **Gradient Backgrounds**: Modern visual appeal
- **Loading Animations**: Smooth user experience
- **Responsive Design**: Works on all screen sizes
- **Interactive Elements**: Hover effects and animations
- **Information Sidebar**: Model details and usage tips

## 🔧 Customization

To modify the styling, edit the CSS in the `st.markdown()` section of `app.py`. The design uses:

- CSS Grid and Flexbox for layouts
- Linear gradients for backgrounds
- Box shadows for depth
- Smooth transitions for interactions

## 📊 Performance

- **Prediction Speed**: Near-instantaneous results
- **Memory Usage**: Optimized for efficiency
- **Model Size**: ~4.65 MB
- **Vocabulary**: 4,818 unique words

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit and TensorFlow**
