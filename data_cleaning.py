import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import preprocessing

# function to delete all the rows with None values
def delete_null_rows(data):
    # delete rows with none values
    # remove rows or columns with missing values (NaN)
    data.dropna(inplace=True)
    return data

# function to delete duplicate rows
def delete_duplicate_rows(data):
    # delete duplicate rows
    data.drop_duplicates(inplace=True)
    return data

# delete row with value 'other' in gender column
def delete_gender_other(data):
    data = data[data['gender'] != 'Other']
    return data

# function to Label Encoding for gender column
# female = 0, male = 1
def encode_gender(data):
    label_encoder = preprocessing.LabelEncoder()
    data['gender'] = label_encoder.fit_transform(data['gender'])
    return data

# function to label encoding for smoking_history column
# 'never': 0, 'No Info': -1, 'current': 2, 'former': 1, 'ever': 2, 'not current': 0
def encode_smoking_history(data):
    data['smoking_history'] = data['smoking_history'].replace('never', 0)
    data['smoking_history'] = data['smoking_history'].replace('No Info', -1)
    data['smoking_history'] = data['smoking_history'].replace('current', 2)
    data['smoking_history'] = data['smoking_history'].replace('former', 1)
    data['smoking_history'] = data['smoking_history'].replace('ever', 2)
    data['smoking_history'] = data['smoking_history'].replace('not current', 0)
    return data

# Remove all records where age is given in decimal
def remove_decimal_age(data):
    data = data[data['age'].mod(1) == 0]
    return data

# convert age column datatype to int
def convert_age_to_int(data):
    data['age'] = data['age'].astype(int)
    return data

def main():
    df = pd.DataFrame(data)

    # Get non-null counts and data types
    non_null_counts = df.count()
    data_types = df.dtypes

    # Combine the results into a single DataFrame
    output = pd.DataFrame({'Non-Null Counts': non_null_counts, 'Data Types': data_types})
    print(output)


# read the data
data = pd.read_csv('file/diabetes_prediction_dataset.csv')

# delete rows with zero or NULL values
data = delete_null_rows(data)

# delete duplicate rows
data = delete_duplicate_rows(data)

# delete rows with gender other
data = delete_gender_other(data)

# encode gender column
data = encode_gender(data)

# encode smoking_history column
data = encode_smoking_history(data)

# remove decimal age
data = remove_decimal_age(data)

# convert age column datatype to int
data = convert_age_to_int(data)

# print main
if __name__ == "__main__":
    # print(data['gender'].value_counts())
    # print(data)
    main()