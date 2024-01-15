# train_test_data.py

def split_data(features):
    # Implement logic to split data into training and testing sets
    # For demonstration purposes, let's assume we're using a simple train-test split
    from sklearn.model_selection import train_test_split

    labels = preprocessed_data['label']  # Assuming 'label' is the column indicating positive or negative sentiment
    train_data, test_data, train_labels, test_labels = train_test_split(features, labels, test_size=0.25, random_state=42)

    return train_data, test_data
