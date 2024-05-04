from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Load the saved model
model = load_model("emotion_detection_model.h5")

# Load tokenizer from disk
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Function to preprocess text
def preprocess_text(text):
    # Implement your preprocessing steps here
    return text

# Function to predict emotion
@app.route('/predict-emotion', methods=['POST'])
def predict_emotion():
    text = request.json['text']
    preprocessed_text = preprocess_text(text)
    sequence = tokenizer.texts_to_sequences([preprocessed_text])
    padded_sequence = pad_sequences(sequence, maxlen=79, padding='post')
    prediction = model.predict(padded_sequence)
    predicted_label = int(prediction.argmax(axis=-1))
    emotion_labels = {0: 'sadness', 1: 'joy', 2: 'love', 3: 'anger', 4: 'fear', 5: 'surprise'}
    predicted_emotion = emotion_labels.get(predicted_label)
    return jsonify({'predicted_emotion': predicted_emotion})

if __name__ == '__main__':
    app.run(debug=True)
