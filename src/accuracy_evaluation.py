from sklearn.metrics import accuracy_score

def evaluate_accuracy(test_labels, nb_predictions, rf_predictions, dt_predictions):
    nb_accuracy_result = accuracy_score(test_labels, nb_predictions)
    rf_accuracy_result = accuracy_score(test_labels, rf_predictions)
    dt_accuracy_result = accuracy_score(test_labels, dt_predictions)
    print("Accuracy Evaluation Done!")
    return nb_accuracy_result, rf_accuracy_result, dt_accuracy_result
