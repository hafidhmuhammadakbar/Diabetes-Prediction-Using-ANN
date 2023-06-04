from data_cleaning import data
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# function to scale the data
def scale_data(X_data):
    stand = preprocessing.StandardScaler()
    temp = stand.fit_transform(X_data)
    return temp


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
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

# scaling data
stand = preprocessing.StandardScaler()
X_train = scale_data(X_train)
X_test = scale_data(X_test)

# print main
if __name__ == "__main__":
    main()