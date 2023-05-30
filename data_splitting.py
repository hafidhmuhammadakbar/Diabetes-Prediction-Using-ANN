from data_cleaning import data
from sklearn.model_selection import train_test_split

def main():
    # print the shape of train, test, and validation sets
    print('train shape: ', train.shape)
    print(train)
    print('test shape: ', test.shape)
    print(test)
    print('validation shape: ', validation.shape)
    print(validation)

# split the data into train and test sets with 70% and 30% respectively and arbitrary random_state
train, test = train_test_split(data, test_size=0.3, random_state=42)

# split the test data into test and validation sets with 50% and 50% respectively and arbitrary random_state
test, validation = train_test_split(test, test_size=0.5, random_state=42)

# print main
if __name__ == "__main__":
    main()