from sklearn.metrics import confusion_matrix

def evaluate_models(test_labels, nb_predictions, rf_predictions, dt_predictions):
    nb_confusion_result = confusion_matrix(test_labels, nb_predictions)
    rf_confusion_result = confusion_matrix(test_labels, rf_predictions)
    dt_confusion_result = confusion_matrix(test_labels, dt_predictions)
    print('Confusion Matrix Done!')
    return nb_confusion_result, rf_confusion_result, dt_confusion_result
