from src import data_set, pre_processing, feature_extraction, train_test_data, machine_learning, confusion_matrix, accuracy_evaluation, save_result_to_csv, user_interface

def main():
    raw_data = data_set.data_set()
    processed_data = pre_processing.preprocess_data(raw_data)
    feature_extraction.extract_features(processed_data)
    train_data, test_data, train_labels, test_labels = train_test_data.split_data(processed_data)
    test_labels, nb_predictions, rf_predictions, dt_predictions, nb_classification_report, rf_classification_report, dt_classification_report = machine_learning.train_models(train_data, test_data, train_labels, test_labels)
    nb_confusion_result, rf_confusion_result, dt_confusion_result = confusion_matrix.evaluate_models(test_labels, nb_predictions, rf_predictions, dt_predictions)
    nb_accuracy_result, rf_accuracy_result, dt_accuracy_result = accuracy_evaluation.evaluate_accuracy(test_labels, nb_predictions, rf_predictions, dt_predictions)
    save_result_to_csv.save_results(nb_confusion_result, rf_confusion_result, dt_confusion_result, nb_accuracy_result, rf_accuracy_result, dt_accuracy_result, nb_classification_report, rf_classification_report, dt_classification_report)
    user_interface.display_results(evaluation_results)
main()
