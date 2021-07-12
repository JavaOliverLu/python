from tensorflow.keras.datasets.mnist import load_data
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
import pandas as pd
print(y_train[0])
pd.DataFrame(x_train[0])
import matplotlib.pyplot as plt
plt.imshow(x_train[0], cmap="gray")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
layers = [
    Dense(128, activation="sigmoid", input_dim=784),
    Dense(10, activation="sigmoid")
]
model = Sequential(layers)
model.summary()
model.compile(loss="mse",metrics=["accuracy"])
from tensorflow.keras.utils import to_categorical
x_train_r = x_train.reshape(-1, 784) / 255
x_test_r = x_test.reshape(-1, 784) / 255
y_train_cat = to_categorical(y_train, num_classes=10)
y_test_cat = to_categorical(y_test, num_classes=10)
print(x_train_r.shape)
print(y_train_cat[0])
print(y_train[0])
from tensorflow.keras.utils import to_categorical
x_train_r = x_train.reshape(-1, 784) / 255
x_test_r = x_test.reshape(-1, 784) / 255
y_train_cat = to_categorical(y_train, num_classes=10)
y_test_cat = to_categorical(y_test, num_classes=10)
print(x_train_r.shape)
print(y_train_cat[0])
print(y_train[0])
model.evaluate(x_test_r, y_test_cat)
from sklearn.metrics import confusion_matrix
pre = model.predict_classes(x_test_r)
mat = confusion_matrix(y_test, pre)
pd.DataFrame(mat,
       index=["{}(真實)".format(i) for i in range(10)],
       columns=["{}(預測)".format(i) for i in range(10)])
import numpy as np
idx = np.nonzero(pre != y_test)[0][:200]
false_pre = pre[idx]
false_ori = y_test[idx]
false_img = x_test[idx]
plt.figure(figsize=(14, 42))
width = 10
height = len(idx) // width + 1
for i in range(len(idx)):
    plt.subplot(height, width, i+1)
    t = "[O]:{}\n[P]:{}".format(false_ori[i], false_pre[i])
    plt.title(t)
    plt.axis("off")
    plt.imshow(false_img[i])
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image
fn = input("檔名")
img = load_img(fn, target_size=(28, 28)).convert("L")
img = np.array(img)
img_r = img.reshape(1, 784) / 255
proba = model.predict(img_r)[0]
for i in range(10):
    print(i, "的機率:", round(proba[i], 3))
ans = model.predict_classes(img_r)[0]
print("答案:", ans)
plt.imshow(img)
#這是數字辨識實作程式與說明
#這個程式使用python語言，並搭TENSORFLOW神經網路，建構出一個為128條神經的模型並且去網路尋找數字訓練集訓練他的精確度（讓他的誤差達到最小），再輸入一張灰階照片，使用圖形處理--池化法及sigmoid 函數來對這個測試資料進行機率評估，並且將10個數字裡面機率最高的數字作為答案並且輸出給使用者
