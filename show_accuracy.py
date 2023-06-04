import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.metrics import confusion_matrix, accuracy_score

from data_splitting import y_test, X_test

# load the model
from tensorflow.keras.models import load_model

ann = load_model('ann_model.h5')

y_pred_ann = ann.predict(X_test)
y_pred_ann = (y_pred_ann > 0.5)

df = pd.DataFrame({'Model': ['ANN'], 'True Negative' : [confusion_matrix(y_test, y_pred_ann).ravel()[0]], 'False Negative' : [confusion_matrix(y_test, y_pred_ann).ravel()[1]], 'True Positive' : [confusion_matrix(y_test, y_pred_ann).ravel()[2]], 'False Positive' : [confusion_matrix(y_test, y_pred_ann).ravel()[3]], 'Accuracy' : [accuracy_score(y_test, y_pred_ann)]})
print(df)