import time

from autosklearn.classification import AutoSklearnClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report

print('[INFO] Loading digits dataset.')
X, y = load_digits(return_X_y=True)

print('[INFO] Splitting.')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, train_size=0.8)

print('[INFO] Train shape: {}'.format(X_train.shape))
print('[INFO] Test shape: {}'.format(X_test.shape))

print('[INFO] Finding best model...')
classifier = AutoSklearnClassifier(per_run_time_limit=120, ml_memory_limit=1024 * 2, time_left_for_this_task=3600)
start = time.time()

X_train = X_train.astype('float')
classifier.fit(X_train, y_train)
print('[INFO] Elapsed time finding best model: {} seconds.'.format(time.time() - start))

predictions = classifier.predict(X_test)
print('--- CLASSIFICATION REPORT: ---')
print(classification_report(y_test, predictions))
print('\n\n--- MODELS: ---')
print(classifier.show_models())
print('\n\n--- STATISTICS: ---')
print(classifier.sprint_statistics())
