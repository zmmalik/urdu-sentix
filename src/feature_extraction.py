from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

def extract_features(preprocessed_data):
    feature_extraction_methods = [
        'tfidf',
        {'unigram': {'x': 1, 'y': 1}},
        {'bigram': {'x': 2, 'y': 2}},
        {'trigram': {'x': 3, 'y': 3}},
        {'ngram': {'x': 1, 'y': 3}}
    ]
    features = {}
    df = pd.DataFrame(preprocessed_data, columns=["Comment", "Sentiment"])
    for index, method in enumerate(feature_extraction_methods):
        if method == 'tfidf':
            vector = TfidfVectorizer()
            features[method] = vectorization(vector, df)

        if isinstance(method, dict):
            for key, value in method.items():
                if isinstance(value, dict):
                    vector = CountVectorizer(ngram_range=(value['x'], value['y']), max_features=5000)
                    features[key] = vectorization(vector, df)
    print("Feature Extraction Done!")
    return features

def vectorization(vectorizer, df):
    features = vectorizer.fit_transform(df['Comment']).toarray()
    return features