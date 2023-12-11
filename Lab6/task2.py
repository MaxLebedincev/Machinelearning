import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow import keras
import numpy as np
import PIL


path = input("Please enter path to file.jpg: ")


model = keras.models.load_model('CNN.keras')

image_input = PIL.Image.open(f'Data\\{path}').convert("L")
array_input = np.array(image_input)

array_empty = np.zeros((28, 28), 'uint8')
array_empty += 255

array_input = np.subtract(array_empty, array_input)

array_input = array_input / 255
array_input = np.expand_dims(array_input, axis=0)
array_input = np.expand_dims(array_input, axis=3)

print(f'Answer: {np.argmax(model.predict(array_input))}')
