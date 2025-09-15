import numpy as np
import pickle
import streamlit as st
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import time

# Configure page
st.set_page_config(
    page_title="Next Word Predictor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .prediction-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .result-success {
        background: linear-gradient(90deg, #56ab2f 0%, #a8e6cf 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 1.2rem;
        margin: 1rem 0;
    }
    
    .result-warning {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 1.1rem;
        margin: 1rem 0;
    }
    
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        border-radius: 25px;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e1e8ed;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
</style>
""", unsafe_allow_html=True)

## load the lstm model
with st.spinner('🔄 Loading AI model...'):
    try:
        model=load_model('next_word_lstm.keras')
        if model is None:
            st.error("Failed to load the model")
            st.stop()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

# load the tokenizer
with st.spinner('📚 Loading vocabulary...'):
    try:
        with open('tokenizer.pickle','rb') as handle:
            tokenizer=pickle.load(handle)
    except Exception as e:
        st.error(f"Error loading tokenizer: {e}")
        st.stop()

## function  to predict the next word
def predict_next_word(model,tokenizer,text,max_seq_len):
    # Convert text to lowercase for better matching
    text = text.lower().strip()
    
    # Convert text to token sequence
    token_list = tokenizer.texts_to_sequences([text])
    
    # Check if tokenization was successful
    if not token_list or len(token_list[0]) == 0:
        return "Unknown words in input text"
    
    token_list = token_list[0]
    
    # Truncate if sequence is too long
    if len(token_list) >= max_seq_len:
        token_list = token_list[-(max_seq_len-1):]
    
    # Pad the sequence
    token_list = pad_sequences([token_list], maxlen=max_seq_len-1, padding='pre')
    
    # Predict next word
    predicted = model.predict(token_list, verbose=0)
    predict_word_index = np.argmax(predicted, axis=1)[0]  # Get the index as integer
    
    # Find the word corresponding to the predicted index
    for word, index in tokenizer.word_index.items():
        if index == predict_word_index:
            return word
    
    return "Unable to predict"
## streamlit app
# Header
st.markdown("""
<div class="main-header">
    <h1>🧠 Next Word Predictor</h1>
    <p>Powered by LSTM Neural Network trained on Shakespeare's Hamlet</p>
</div>
""", unsafe_allow_html=True)

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
    
    st.markdown("### 📝 Enter Your Text")
    input_text = st.text_input(
        "", 
        placeholder="Type your text here... (e.g., 'to be or not')",
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    predict_button = st.button("🚀 Predict Next Word")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.markdown("## 📊 Model Information")
    
    st.markdown("""
    <div class="info-card">
        <h4>🎯 Model Details</h4>
        <ul>
            <li><strong>Architecture:</strong> LSTM Neural Network</li>
            <li><strong>Training Data:</strong> Shakespeare's Hamlet</li>
            <li><strong>Vocabulary Size:</strong> 4,818 words</li>
            <li><strong>Sequence Length:</strong> 13 words</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h4>💡 Tips for Best Results</h4>
        <ul>
            <li>Use words from Shakespeare's era</li>
            <li>Try phrases like "to be or not"</li>
            <li>Keep input text reasonably short</li>
            <li>Use lowercase letters</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h4>🔧 Technical Stack</h4>
        <ul>
            <li>TensorFlow/Keras</li>
            <li>LSTM Layers</li>
            <li>Streamlit Frontend</li>
            <li>Python Backend</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Prediction logic
if predict_button:
    if input_text.strip():
        with st.spinner('🤖 AI is thinking...'):
            time.sleep(0.5)  # Add slight delay for better UX
            try:
                max_seq_len = model.input_shape[1] + 1
                next_word = predict_next_word(model, tokenizer, input_text, max_seq_len)
                
                # Create result container
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col2:
                    if next_word and next_word not in ["Unknown words in input text", "Unable to predict"]:
                        st.markdown(f"""
                        <div class="result-success">
                            <h3>🎉 Prediction Complete!</h3>
                            <p><strong>Next Word:</strong> <span style="font-size: 1.5em; font-weight: bold;">{next_word}</span></p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"""
                        <div style="text-align: center; font-size: 1.2rem; margin: 1rem 0; 
                                   padding: 1rem; background: #f8f9fa; border-radius: 10px;">
                            <strong>Complete Sequence:</strong><br>
                            <em>"{input_text} <span style="color: #667eea; font-weight: bold;">{next_word}</span>"</em>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Add some celebration
                        st.balloons()
                        
                    else:
                        st.markdown(f"""
                        <div class="result-warning">
                            <h3>🤔 {next_word}</h3>
                            <p>The model couldn't find a good prediction for this text.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.info("💡 **Tip:** Try using words that Shakespeare might have used in Hamlet!")
                        
            except Exception as e:
                st.error(f"🚨 **Error during prediction:** {e}")
                st.info("🔍 Make sure the model file 'next_word_lstm.keras' and tokenizer file 'tokenizer.pickle' exist in the same directory.")
    else:
        st.warning("📝 **Please enter some text to predict the next word.**")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>Built with ❤️ using Streamlit and TensorFlow | Next Word Prediction AI</p>
</div>
""", unsafe_allow_html=True)