from src import data_collection, pre_processing, feature_extraction, train_test_data, machine_learning, confusion_matrix, save_result_to_csv, user_interface

def main():
    # Main orchestration of the workflow
    raw_data = data_collection.collect_data()
    processed_data = pre_processing.process_data(raw_data)
    extracted_features = feature_extraction.extract_features(processed_data)
    train_data, test_data = train_test_data.split_data(extracted_features)
    models = machine_learning.train_models(train_data)
    evaluation_results = confusion_matrix.evaluate_models(models, test_data)
    save_result_to_csv.save_results(evaluation_results)
    user_interface.display_results(evaluation_results)

if __name__ == "__main__":
    main()
