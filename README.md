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

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/next-word-predictor.git
   cd next-word-predictor
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download additional required files** (if not included in repository)
   - If model files are not included due to size limitations, you'll need to train the model using `exp.ipynb`
   - Ensure you have `hamlet.txt` in the project directory for training

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🔧 Training the Model (if model files are not included)

If the trained model files are not available in the repository, you can train your own model:

1. **Open the training notebook**

   ```bash
   jupyter notebook exp.ipynb
   ```

   _or if using VS Code, open `exp.ipynb` directly_

2. **Run all cells in sequence** to:

   - Download and preprocess the Hamlet text
   - Create input sequences and tokenizer
   - Build and train the LSTM model
   - Save the model and tokenizer files

3. **Training will generate**:

   - `next_word_lstm.keras` - The trained LSTM model
   - `tokenizer.pickle` - The vocabulary tokenizer

4. **After training**, you can run the Streamlit app as described above

**Note**: Training may take several minutes depending on your hardware.

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
next-word-predictor/
├── app.py                # Main Streamlit application
├── exp.ipynb            # Training notebook (Jupyter)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
├── next_word_lstm.keras # Trained model file (if included)
├── tokenizer.pickle    # Vocabulary tokenizer (if included)
└── hamlet.txt          # Training data (Shakespeare's Hamlet)
```

**Note**: Large model files (`next_word_lstm.keras`, `tokenizer.pickle`) may not be included in the repository due to GitHub file size limitations. In this case, you'll need to train the model yourself using the provided notebook.

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

## 🛠️ Troubleshooting

### Common Issues

**1. "Error loading model" message**

- Ensure `next_word_lstm.keras` exists in the project directory
- If missing, train the model using `exp.ipynb`

**2. "Error loading tokenizer" message**

- Ensure `tokenizer.pickle` exists in the project directory
- If missing, train the model using `exp.ipynb`

**3. "ModuleNotFoundError" for TensorFlow/Keras**

- Make sure you've activated your virtual environment
- Run `pip install -r requirements.txt`

**4. Jupyter notebook won't open**

- Install Jupyter: `pip install jupyter`
- Or use VS Code with Python extension

### File Size Considerations

GitHub has a 100MB file limit. If model files exceed this:

- Use Git LFS (Large File Storage) for large files
- Or train the model locally using the provided notebook

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit and TensorFlow**
