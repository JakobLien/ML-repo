import tensorflow as tf
import pandas as pd
import numpy as np 

dataset_path = './Testicular Cancer Dataset.csv'
df  = pd.read_csv(dataset_path)

 # print(df.head())

# print(df.describe())

# print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(x_train)
print(y_train)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

predictions = model(x_train[:1]).numpy()

print(loss_fn(y_train[:1], predictions).numpy())

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

print(loss_fn(y_train[:1], predictions).numpy())


test_x = x_train[0]
test_y = y_train[0]

print(x_train) 

text_x = np.expand_dims(test_x, axis=0) 

predictions_single = model.predict(test_x)

probabilities = tf.nn.softmax(predictions_single[0])

predicted_class = np.argmax(probabilities)


print(predicted_class)