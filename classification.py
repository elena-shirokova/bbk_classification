from bbk_matrix import t,v,p
from sklearn.cross_validation import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm, grid_search
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.preprocessing import MultiLabelBinarizer

y = list()
for line in open('y_all_labels_code.csv'):
    labels = [int(x) for x in line.split(',')]
    y.append(labels)

y_bin = MultiLabelBinarizer().fit_transform(y)
X = t
X_train, X_test, y_train, y_test = train_test_split(X, y_bin, test_size=0.7)

params = {'n_neighbors': range(1, 200, 5)}
"""grid_searcher = grid_search.GridSearchCV(OneVsRestClassifier(KNN()),\
                             params, cv=5, scoring='roc_auc', n_jobs=3)
grid_searcher.fit(X_train, y_train)

print grid_searcher.best_score_
print grid_searcher.best_estimator_"""

clf = OneVsRestClassifier(LinearSVC())
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)

print classification_report(y_test, y_predict)
print accuracy_score(y_test,y_predict)