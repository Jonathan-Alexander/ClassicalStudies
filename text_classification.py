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
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.svm import LinearSVC

#SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)
df = pd.read_csv('data.csv')
X = df['clean_text']
y = df.Retracted

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state = 42)


sgd = Pipeline([('vect', CountVectorizer(strip_accents='unicode', stop_words='english')),
                ('tfidf', TfidfTransformer()),
                ('clf', LinearSVC()),
               ])


sgd.fit(X_train, Y_train)



score = sgd.score(X_test, Y_test)    
print("Score: {}".format(score))
y_pred = sgd.predict(X_test)
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

