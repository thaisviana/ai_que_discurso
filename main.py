from sklearn.feature_extraction.text import TfidfVectorizer
from extractor import get_corpus
from nltk import download
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from sklearn import metrics

#download('stopwords')

#nltk.stem.RSLPStemmer()
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=500, stop_words=stopwords.words('portuguese'), analyzer='word',)
X = vectorizer.fit_transform(get_corpus())

#print(vectorizer.get_feature_names())

# print(X.toarray())

labels = vectorizer.get_feature_names()[:165]
km = KMeans(n_clusters=70, init='k-means++', max_iter=100, n_init=1)

print("Clustering sparse data with %s" % km)
km.fit(X)
print([labels[i] for i in km.labels_])
print(km.cluster_centers_)
#
# print(f"Homogeneity: {metrics.homogeneity_score(labels, km.labels_)}")
# print(f"Completeness: {metrics.completeness_score(labels, km.labels_)}")
# print(f"V-measure: {metrics.v_measure_score(labels, km.labels_)}")
# print(f"Adjusted Rand-Index: {metrics.adjusted_rand_score(labels, km.labels_)}")
# print(f"Silhouette Coefficient: {metrics.silhouette_score(X, km.labels_, sample_size=1000)}")
