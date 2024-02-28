import pandas as pd
import string
import re
import sys
sys.path.append('../')
from data.stop_words import roman_urdu_stopwords

def preprocess_data(raw_data):
    stop_words = set(roman_urdu_stopwords)
    df = pd.DataFrame(raw_data, columns=["Comment", "Sentiment"])
    df["Comment"] = df["Comment"].apply(lambda x: normalize_text(x))
    df["Comment"] = df["Comment"].apply(lambda x: remove_emojis(x))
    df["Comment"] = df["Comment"].apply(lambda x: remove_stopwords(x, stop_words))
    df["Comment"] = df["Comment"].str.split()
    df = df.explode("Comment")
    df = df.drop_duplicates()
    df = df.dropna()
    print("Preprocessing Data Done!")
    return df

def normalize_text(text):
    if text is not None and isinstance(text, str):
        text = text.strip().lower().translate(str.maketrans('', '', string.punctuation))
    return text

def remove_stopwords(text, stop_words):
    if text is not None and isinstance(text, str):
        tokens = text.split()
        tokens = [token for token in tokens if token not in stop_words]
        return ' '.join(tokens)
    else:
        return ''

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251" 
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)