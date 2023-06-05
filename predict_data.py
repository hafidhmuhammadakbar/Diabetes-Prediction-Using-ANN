from tensorflow.keras.models import load_model

# function to predict
def predict_data(result):
    if result >= 0.5:
        return "Diabetes"
    else:
        return "No Diabetes"

def main():
    person_X = [[0,80, 1, 0, -1, 27.32, 8, 200]]
    result = ann.predict(person_X)
    print(predict_data(result))

# load the model
ann = load_model('ann_model.h5')

# print main
if __name__ == "__main__":
    main()