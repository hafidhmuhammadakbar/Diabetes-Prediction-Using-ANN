from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from data_splitting import scale_data

# function to predict
def predict_data(result):
    if result >= 0.5:
        return "Diabetes"
    else:
        return "No Diabetes"

def main():
    person_X = scale_data([[0,80, 1, 0, -1, 27.32, 7.5, 160]])
    result = ann.predict(person_X)
    print(predict_data(result))

# load the model
ann = load_model('ann_model.h5')

stand = StandardScaler()

# print main
if __name__ == "__main__":
    main()