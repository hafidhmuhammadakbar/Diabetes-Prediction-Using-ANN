from tensorflow.keras.models import load_model
import numpy as np

ann = load_model('ann_model.h5')
if(ann == None):
   print("Error: Model not found")
   exit()
else:
   print("Model loaded")
   weights_layer1 = ann.layers[0].get_weights()[0]
   weights_sum = np.sum(np.abs(weights_layer1), axis=1)
   print("Weights sum: ", weights_sum)
   attribute_names = ["gender", "age", "hypertension", "heart_disease", "smoking_history", "bmi", "HbA1c_level", "blood_glucose_level"]
   max_index = np.argmax(weights_sum)
   most_influential_attribute = attribute_names[max_index]
   print("Most influential attribute: ", most_influential_attribute)