import numpy as np

# Mock data for evaluation results
mock_nb_confusion_result = np.array([[10, 2], [3, 15]])
mock_rf_confusion_result = np.array([[9, 3], [2, 16]])
mock_dt_confusion_result = np.array([[11, 1], [4, 14]])

mock_nb_accuracy_result = 0.85
mock_rf_accuracy_result = 0.82
mock_dt_accuracy_result = 0.88

mock_nb_classification_report = (
    "              precision    recall  f1-score   support\n\n"
    "    Negative       0.00      0.00      0.00        2\n"
    "    Positive       0.33      1.00      0.50        1\n\n"
)

mock_rf_classification_report = (
    "              precision    recall  f1-score   support\n\n"
    "    Negative       0.82      0.82      0.82        18\n"
    "    Positive       0.75      0.75      0.75        12\n\n"
    "    accuracy                           0.79        30\n"
    "   macro avg       0.78      0.78      0.78        30\n"
    "weighted avg       0.79      0.79      0.79        30\n"
)

mock_dt_classification_report = (
    "              precision    recall  f1-score   support\n\n"
    "    Negative       0.94      0.83      0.88        18\n"
    "    Positive       0.79      0.92      0.85        12\n\n"
    "    accuracy                           0.87        30\n"
    "   macro avg       0.86      0.87      0.86        30\n"
    "weighted avg       0.88      0.87      0.87        30\n"
)
