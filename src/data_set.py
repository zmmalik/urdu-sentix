import csv

def data_set():
    processed_data = []
    with open("data/raw_data/train_and_test_data.csv", encoding="utf8") as file:
        csvreader = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csvreader:
            if len(row) > 1:
                comment = row[0]
                sentiment = row[1]
                processed_data.append([comment, sentiment])
            else:
                processed_data.append(row)
    print('Data Collection Done!')
    return processed_data