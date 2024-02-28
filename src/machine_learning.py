from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

def train_models(train_data, test_data, train_labels, test_labels):
    # Convert text data to TF-IDF features
    vectorizer = TfidfVectorizer()
    train_features = vectorizer.fit_transform(train_data)
    test_features = vectorizer.transform(test_data)

    # Model 1: Naive Bayes
    nb_model = MultinomialNB()
    nb_model.fit(train_features, train_labels)
    nb_predictions = nb_model.predict(test_features)
    nb_classification_report = classification_report(test_labels, nb_predictions)
    
    # Model 2: Random Forest
    rf_model = RandomForestClassifier()
    rf_model.fit(train_features, train_labels)
    rf_predictions = rf_model.predict(test_features)
    rf_classification_report = classification_report(test_labels, rf_predictions)
    
    # Model 3: Decision Tree
    dt_model = DecisionTreeClassifier()
    dt_model.fit(train_features, train_labels)
    dt_predictions = dt_model.predict(test_features)
    dt_classification_report = classification_report(test_labels, dt_predictions)
    
    print('Machine Learning Done!')
    return test_labels, nb_predictions, rf_predictions, dt_predictions, nb_classification_report, rf_classification_report, dt_classification_report
    