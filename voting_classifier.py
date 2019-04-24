#Trying out Voting Classifier

import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import nltk
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier, VotingClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import TransformerMixin
from sklearn.compose import ColumnTransformer as CT


class DenseTransformer(TransformerMixin):
    
    def transform(self, X, y=None, **fit_params):
        return X.todense()

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X, y, **fit_params)
        return self.transform(X)

    def fit(self, X, y=None, **fit_params):
        return self

class DropTextTransformer(TransformerMixin):
    def transform(self, X, y=None, **fit_params):
        return X.drop('clean_text', axis=1)
        #return X[:, :-1]
    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X,y, **fit_params)
        return self.transform(X)
    def fit(self, X, y=None, **fit_params):
        return self

   



#SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)
df = pd.read_csv('data.csv')
#Add article type and apply one hot encoding
features = ['gunning_fog','pos','neg','neu','Citations','Times Cited','Number Authors','Journal Impact Factor','wc','sc','wps','dic','sixltr','insight','cause','discrep','tentat','certain','quant','numbers','jargon', 'clean_text']
target = ['Retracted']
X = df[features]
y = df[target]

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

ct_cv = CT([('vect', CountVectorizer(strip_accents='unicode', stop_words='english'), 21)], remainder='drop')
#ct_tfidf = CT([('tfidf', TfidfTransformer(), 21)], remainder='passthrough')

linsvc= Pipeline([('ct_cv', ct_cv),
                ('tfidf', TfidfTransformer()),
                ('clf', SVC(kernel='linear', probability=True)),
               ])

ct_cv_sgd = CT([('vect', CountVectorizer(strip_accents='unicode', stop_words='english'), 21)], remainder='passthrough')
ct_tfidf_sgd = CT([('tfidf', TfidfTransformer(), 21)], remainder='passthrough')
sgd_clf = Pipeline([('vect', ct_cv_sgd),
                ('tfidf', ct_tfidf_sgd),
                ('df', DenseTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None))
               ])

ada_clf = Pipeline([('drop_text', DropTextTransformer()),
                ('clf', AdaBoostClassifier())
                ])


vclf = VotingClassifier([('lin', linsvc),('sgd', sgd_clf), ('ada', ada_clf)])

vclf.fit(X_train, Y_train)
score = vclf.score(X_test, Y_test)    
print("Score: {}".format(score))
y_pred = vclf.predict(X_test)
prec = precision_score(Y_test, y_pred)
print("Precision: {}".format(prec))
report = classification_report(Y_test, y_pred)
print(report)
'''
con_matrix = confusion_matrix(Y_test, y_pred)
plt.matshow(con_matrix)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
#plt.show()
'''

