from sklearn.model_selection import train_test_split

def split_data(df):
    train_data, test_data, train_labels, test_labels = train_test_split(
        df["Comment"], df["Sentiment"], test_size=0.25, random_state=42)

    print(df["Comment"], df["Sentiment"], "Data Splitting Done!")
    return train_data, test_data, train_labels, test_labels