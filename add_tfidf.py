import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.compose import ColumnTransformer as CT
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin


class DenseTransformer(TransformerMixin):
    
    def transform(self, X, y=None, **fit_params):
        return X.todense()

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X, y, **fit_params)
        return self.transform(X)

    def fit(self, X, y=None, **fit_params):
        return self




h = .02  # step size in the mesh

names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA", "Linear SVC", "SGD"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    LinearSVC(),
    SGDClassifier(max_iter=1000,shuffle=True)]

df = pd.read_csv('data.csv')
ct_cv = CT([('vect', CountVectorizer(strip_accents='unicode', stop_words='english'), 21)], remainder='passthrough')
ct_tfidf = CT([('tfidf', TfidfTransformer(), 21)], remainder='passthrough')

features = ['gunning_fog','pos','neg','neu','Citations','Times Cited','Number Authors','Journal Impact Factor','wc','sc','wps','dic','sixltr','insight','cause','discrep','tentat','certain','quant','numbers','jargon', 'clean_text']
#features = ['pos', 'dic', 'discrep', 'numbers', 'jargon']
target = ['Retracted']
X = df[features]
y = df[target]

X_train, X_test, Y_train, Y_test = train_test_split(X, y, random_state=41)

'''
X_train_count = cv.fit_transform(X_train['clean_text'])
X_train_tfidf = tfidf_transformer.fit_transform(X_train_count)
X_train['clean_text'] = list(X_train_tfidf.toarray())

X_test_count = cv.fit_transform(X_test['clean_text'])
X_test_tfidf = tfidf_transformer.fit_transform(X_test_count)
X_test['clean_text'] = list(X_test_tfidf.toarray())
'''


for name, clf in zip(names, classifiers):
    clf = Pipeline([('vect', ct_cv),
                ('tfidf', ct_tfidf),
                ('df', DenseTransformer()),
                ('clf', clf)
               ])
    print(name)
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)    
    print("Score -- {}".format(score))
    y_pred = clf.predict(X_test)
    '''
    con_matrix = confusion_matrix(Y_test, y_pred)
    plt.matshow(con_matrix)
    plt.title('Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    '''
