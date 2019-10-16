from sklearn.feature_extraction.text import TfidfVectorizer
from extractor import get_corpus
from nltk import download
from nltk.corpus import stopwords


#download('stopwords')

#nltk.stem.RSLPStemmer()
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=500, stop_words=stopwords.words('portuguese'), analyzer='word',)
X = vectorizer.fit_transform(get_corpus())
print(vectorizer.get_feature_names())
print(X)
