import tensorflow as tf

from data_splitting import X_train, X_test, y_train, y_test

ann = tf.keras.models.Sequential()

ann.add(tf.keras.layers.Dense(units = 8, activation = 'relu')) 
ann.add(tf.keras.layers.Dense(units = 15, activation = 'relu'))
ann.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))

ann.compile(optimizer = 'adam', loss = 'binary_crossentropy')

ann.fit(X_train, y_train, batch_size = 128, epochs = 800)

ann.save('ann_model.h5')