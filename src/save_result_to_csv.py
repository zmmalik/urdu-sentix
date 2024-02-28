import pandas as pd
import numpy as np

def save_results(nb_confusion_result, rf_confusion_result, dt_confusion_result, nb_accuracy_result, rf_accuracy_result, dt_accuracy_result, nb_classification_report, rf_classification_report, dt_classification_report):

    accuracy_df = pd.DataFrame({'': ['Multinomial NB', 'Random Forest Classifier', 'Decision Tree Classifier'], 'Accuracy': [nb_accuracy_result, rf_accuracy_result, dt_accuracy_result]})
    accuracy_df.to_csv('data/results/accuracy.csv', index=False)

    confusion_matrices = [
        np.array(nb_confusion_result),
        np.array(rf_confusion_result),
        np.array(dt_confusion_result)
    ]

    classifier_names = ["Multinomial NB", "Random Forest Classifier", "Decision Tree Classifier"]

    data = []
    for i in range(len(confusion_matrices)):
        matrix = confusion_matrices[i]
        classifier_name = classifier_names[i]
        data.append({"Classifier": classifier_name, 
                    "True Positive": matrix[0, 0], "False Positive": matrix[0, 1],
                    "False Negative": matrix[1, 0], "True Negative": matrix[1, 1]})

    df = pd.DataFrame(data)

    df.to_csv("data/results/confusion_matrices.csv", index=False)

    nb_df = report_to_dataframe(nb_classification_report)
    rf_df = report_to_dataframe(rf_classification_report)
    dt_df = report_to_dataframe(dt_classification_report)

    # Add classifiers' names
    nb_df['Classifier'] = 'Multinomial NB'
    rf_df['Classifier'] = 'Random Forest Classifier'
    dt_df['Classifier'] = 'Decision Tree Classifier'

    # Save all data to a single CSV file
    all_data = pd.concat([nb_df, rf_df, dt_df])
    all_data.to_csv("data/results/classification_report.csv", index=False)
    print("Save Result To CSV Done!")

def report_to_dataframe(report):
    lines = report.split('\n')
    data = []
    for line in lines[2:-5]:
        row = line.split()
        data.append(row)
    df = pd.DataFrame(data, columns=['Class', 'Precision', 'Recall', 'F1-score', 'Support'])
    return df