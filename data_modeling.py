import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

from data_cleaning import data
from data_splitting import X_train, X_test, y_train, y_test

ann = tf.keras.models.Sequential()

ann.add(tf.keras.layers.Dense(units = 8, activation = 'relu')) 
ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))
ann.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
ann.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])

early_stop = EarlyStopping(monitor='val_loss', patience=3)
deep_history = ann.fit(X_train, y_train, epochs=100, validation_data = (X_test, y_test), callbacks=[early_stop], verbose=1)

# save the model
ann.save('ann_model.h5')