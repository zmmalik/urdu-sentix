import pandas as pd

def analysis(vectorizer, nb_model, rf_model, dt_model, comments, preprocessed_comments):
  sentiment_mapping = {0: "Negative", 1: "Positive"}
  vectorized_comments = vectorizer.transform(preprocessed_comments)
  
  nb_sentiments = [sentiment_mapping[pred] for pred in nb_predictions]
  rf_sentiments = [sentiment_mapping[pred] for pred in rf_predictions]
  dt_sentiments = [sentiment_mapping[pred] for pred in dt_predictions]
  
  nb_predictions = nb_model.predict(vectorized_comments)
  rf_predictions = rf_model.predict(vectorized_comments)
  dt_predictions = dt_model.predict(vectorized_comments)
  
  df = pd.DataFrame({'comments': comments, 
                    'nb_sentiments': nb_sentiments,
                    'rf_sentiments': rf_sentiments,
                    'dt_sentiments': dt_sentiments})

  df.to_csv('sentiment_predictions.csv', index=False)
  print({'comments': comments, 
                    'nb_sentiments': nb_sentiments,
                    'rf_sentiments': rf_sentiments,
                    'dt_sentiments': dt_sentiments})
