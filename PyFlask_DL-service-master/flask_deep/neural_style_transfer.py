import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow import keras
import time
import os

model2 = keras.models.load_model('models/모낭홍반농포.h5')

def preprocess_image(image_path):
	img = load_img(image_path, target_size=(128, 128))
	img = img_to_array(img) / 255.0
	img = np.expand_dims(img, axis=0) 
	img_arr = np.vstack([img])
	return img_arr

def main(filename):
	path = './flask_deep/static/images/' + str(filename)
	img = preprocess_image(path)
	result2 = np.argmax(model2.predict(img))

	return result2

if __name__ == "__main__":
	main()