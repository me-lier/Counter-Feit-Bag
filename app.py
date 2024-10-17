import numpy as np
from keras.models import load_model
from skimage.transform import resize
import streamlit as st
from PIL import Image

# Function to load and preprocess a single image
def load_and_preprocess_image(uploaded_file, rescale_size=(100, 100)):
    # Open the image using PIL
    img = Image.open(uploaded_file)
    
    # Convert the image to a numpy array
    img = np.array(img)
    
    # Resize the image to the required size
    img_resized = resize(img, rescale_size, mode='reflect', anti_aliasing=True)
    
    # Ensure the image has the correct shape (1, height, width, channels)
    img_resized = np.expand_dims(img_resized, axis=0)  # Use expand_dims instead of resize
    return img_resized

# Load the saved model using st.cache_resource
@st.cache_resource
def load_trained_model():
    return load_model('./Model/my_model.h5')

model = load_trained_model()

# Streamlit interface
st.title("Bag Authenticity Classifier")

# Image upload widget
uploaded_file = st.file_uploader("Upload an image of the bag", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    img = load_and_preprocess_image(uploaded_file)

    # Make prediction using the loaded model
    prediction = model.predict(img)

    # Get the predicted class and confidence
    predicted_class = np.argmax(prediction)  # Class with the highest probability
    confidence = np.max(prediction)  # Confidence (highest probability)

    result = "Original" if predicted_class == 1 else "Fake"

    # Display the prediction
    st.write(f"Prediction: **{result}**")
    st.write(f"Confidence: **{confidence:.2f}**")
