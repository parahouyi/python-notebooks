import math
import pandas_datareader as web
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import tushare as ts

# ts.set_token('828005039aef100a8745faffc3173a21fe03dcb4ec0cbabde2411bacb')
# pro = ts.pro_api()
# df = web.DataReader('^DJI', data_source='stooq', start='2012-01-01', end='2022-03-02')
code ='000727'
period = 100
df = ts.get_hist_data('000727', start='2018-01-01', end='2022-03-03')
df = df.reindex(index=df.index[::-1])
print(df)

# plt.figure(figsize=(16, 8))
# plt.title('stock price history')
# plt.plot(df['close'])
# plt.xlabel('Date', fontsize=18)
# plt.ylabel('Closing Price', fontsize=18)
# plt.show()

data = df.filter(['close'])

dataset = data.values
training_data_len = math.ceil(len(dataset)*0.8)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)
# scaled_data


train_data = scaled_data[0:training_data_len, :]
x_train = []
y_train = []

for i in range(100, len(train_data)):
    x_train.append(train_data[i-100: i, 0])
    y_train.append(train_data[i, 0])
    if i <= 100:
        print(x_train)
        print(y_train)
        print()

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# x_train.shape

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')


model.fit(x_train, y_train, batch_size=1, epochs=1)

test_data = scaled_data[training_data_len - 100:, :]
x_test = []
y_test = dataset[training_data_len:, :]
for i in range(100, len(test_data)):
    x_test.append(test_data[i - 100: i, 0])

x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
rmse = np.sqrt(np.mean(predictions - y_test)**2)

train = data[:training_data_len]
valid = data[training_data_len:]
valid['predictions'] = predictions
plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Closing Price', fontsize=18)
plt.plot(train['close'])
plt.plot(valid[['close', 'predictions']])
plt.legend(['Train', 'Val', 'predictions'], loc = 'lower right')
plt.show()