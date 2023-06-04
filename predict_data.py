from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

# function to predict
def predict_data(person):
    result = ann.predict(person)
    if result > 0.5:
        return True
    else:
        return False

# load the model
ann = load_model('ann_model.h5')

stand = StandardScaler()
person_X = stand.fit_transform([[1,23.0, 0,0,0,22.9,5.4, 108]])

print(predict_data(person_X))