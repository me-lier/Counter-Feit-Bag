import numpy as np
from keras.models import load_model
from skimage.transform import resize
import pylab as pl
import os

# Function to load and preprocess a single image
def load_and_preprocess_image(img_path, rescale_size=(100, 100)):
    img = pl.imread(img_path)
    img_resized = resize(img, rescale_size, mode='reflect')
    img_resized = np.resize(img_resized, (1,) + rescale_size + (3,))  # Resize to match input shape
    return img_resized

# Load the saved model
model = load_model('/model/my_model.h5')

# Path to the single image file
image_path = './original.png'  # Update the path to your image file

# Preprocess the image
img = load_and_preprocess_image(image_path)

# Make prediction using the loaded model
prediction = model.predict(img)

# Get the predicted class and confidence
predicted_class = np.argmax(prediction)  # Class with the highest probability
confidence = np.max(prediction)  # Confidence (highest probability)

result = ""
if predicted_class == 0:
    result += "Fake"
else:
    result += "Original"

# Display the result
print(f"Image '{os.path.basename(image_path)}' predicted as class {result} with confidence {confidence:.2f}")
