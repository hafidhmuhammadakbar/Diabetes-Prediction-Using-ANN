import numpy as np # linear algebra
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

# function to Label Encoding for gender column
# female = 0, male = 1, other = 2
def encode_gender(data):
    label_encoder = preprocessing.LabelEncoder()
    data['gender'] = label_encoder.fit_transform(data['gender'])
    return data

# function to label encoding for smoking_history column
# never = 0, no info = 1, former = 2, current = 3, not current = 4, ever = 5
def encode_smoking_history(data):
    label_encoder = preprocessing.LabelEncoder()
    data['smoking_history'] = label_encoder.fit_transform(data['smoking_history'])
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

# encode gender column
data = encode_gender(data)

# encode smoking_history column
data = encode_smoking_history(data)

# print main
if __name__ == "__main__":
    main()