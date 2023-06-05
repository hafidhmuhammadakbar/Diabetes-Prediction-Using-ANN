from tensorflow.keras.models import load_model
from sklearn import preprocessing
from data_cleaning import data
from sklearn.model_selection import train_test_split

def predict_data(result):
    ann = load_model('ann_model.h5')
    result = stand.transform(result)
    # print(result)
    result = ann.predict(result)
    if result >= 0.5:
        return "Diabetes"
    else:
        return "No Diabetes"

def main():
    # print the shape of train, test, and validation sets
    print('train shape: ', X_train.shape)
    print(X_train)
    print('test shape: ', X_test.shape)
    print(X_test)

# split the data into dependent and independent variables
# x = independent
# y = dependent
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)

# scale the data
stand = preprocessing.StandardScaler()
X_train = stand.fit_transform(X_train)
X_test = stand.transform(X_test)

# print main
if __name__ == "__main__":
    # main()
    # diabetes
    person_X = [[0, 50, 1, 1, 2, 30, 10, 300]]  
    print(predict_data(person_X))