from data_splitting import predict_data

def main():
    # non-diabetes
    person_X1 = [[0, 50, 0, 0, 2, 25, 5, 100]]
    # diabetes
    person_X2 = [[0, 50, 1, 1, 2, 30, 10, 300]]
    print(predict_data(person_X1))
    print(predict_data(person_X2))

# print main
if __name__ == "__main__":
    main()