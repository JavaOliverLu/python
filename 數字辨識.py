{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "「mlp_winter」的副本",
      "private_outputs": true,
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JavaOliverLu/-2020haoruo-example/blob/master/%E6%95%B8%E5%AD%97%E4%BE%BF%E8%AD%98.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "27bMACun5GZI"
      },
      "source": [
        "# mnist:手寫數字資料\n",
        "from tensorflow.keras.datasets.mnist import load_data\n",
        "# 輸入: x 輸出: y \n",
        "# 訓練(帶回家的): train 測試(小考): test\n",
        "# ((訓練圖片 訓練答案), (測試圖片 測試答案))\n",
        "(x_train, y_train), (x_test, y_test) = load_data()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7PdbNJQO6x6I"
      },
      "source": [
        "print(x_train.shape)\n",
        "print(y_train.shape)\n",
        "print(x_test.shape)\n",
        "print(y_test.shape)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G80t8GFp7I9i"
      },
      "source": [
        "import pandas as pd\n",
        "print(y_train[0])\n",
        "# pandas(pd):表格工具 pd.DataFrame: 把東西轉換成表格\n",
        "pd.DataFrame(x_train[0])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hZ8Sg6Qm7iLL"
      },
      "source": [
        "# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html\n",
        "import matplotlib.pyplot as plt\n",
        "plt.imshow(x_train[0], cmap=\"gray\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QMiX5Caz_ypO"
      },
      "source": [
        "# 創造我們模型: 完整模型model 一層一層layer\n",
        "# Sequential: layer一定會堆在前一層的上面\n",
        "from tensorflow.keras.models import Sequential\n",
        "# Dense: 稠密層/全連接層\n",
        "from tensorflow.keras.layers import Dense\n",
        "layers = [\n",
        "    # 128:128根神經, input_dim:784(28*28)\n",
        "    Dense(128, activation=\"sigmoid\", input_dim=784),\n",
        "    Dense(10, activation=\"sigmoid\")\n",
        "]\n",
        "model = Sequential(layers)\n",
        "model.summary()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "peEfKoe5R34Z"
      },
      "source": [
        "# 確定損失函式(跟正確答案比到底差了多少) mse loss = (predict - answer) ^ 2\n",
        "# 目標是最小!!\n",
        "model.compile(loss=\"mse\",\n",
        "       metrics=[\"accuracy\"])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A76YjbzUc78h"
      },
      "source": [
        "# 預處理\n",
        "# x: 1.reshape 2.scaling\n",
        "# y: one-hot\n",
        "from tensorflow.keras.utils import to_categorical\n",
        "# 60000 * 28 * 28 -> 60000 * 784   \n",
        "# /255:tensorflow規定 0:black 1.0:white\n",
        "x_train_r = x_train.reshape(-1, 784) / 255\n",
        "x_test_r = x_test.reshape(-1, 784) / 255\n",
        "# !!!: 正確答案是十個機率\n",
        "y_train_cat = to_categorical(y_train, num_classes=10)\n",
        "y_test_cat = to_categorical(y_test, num_classes=10)\n",
        "print(x_train_r.shape)\n",
        "print(y_train_cat[0])\n",
        "print(y_train[0])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XRE8_CvlhEM3"
      },
      "source": [
        "# fit: 訓練\n",
        "from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping\n",
        "callbacks = [\n",
        "    EarlyStopping(patience=5, restore_best_weights=True),\n",
        "    ModelCheckpoint(\"mlp.h5\", save_best_only=True)\n",
        "]\n",
        "# validation_split: 切出一部分資料驗證\n",
        "# batch_size: 看多少筆才做一次調整(梯度下降)\n",
        "# epochs: 訓練次數(60000-6000筆/epoch)\n",
        "# 1 epoch 多少次梯度下降: 54000 / 200 -> 270\n",
        "# verbose: 印出多少log(1:default 0:quiet 2:)\n",
        "model.fit(x_train_r, \n",
        "     y_train_cat,\n",
        "     validation_split=0.1,\n",
        "     batch_size=200,\n",
        "     epochs=50,\n",
        "     verbose=2,\n",
        "     callbacks=callbacks)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f-MoMhG2oRYv"
      },
      "source": [
        "model.evaluate(x_test_r, y_test_cat)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K66G2sMDYrVu"
      },
      "source": [
        "# sklearn: predict_proba/predict\n",
        "# keras: predict/predict_classes\n",
        "from sklearn.metrics import confusion_matrix\n",
        "pre = model.predict_classes(x_test_r)\n",
        "mat = confusion_matrix(y_test, pre)\n",
        "pd.DataFrame(mat,\n",
        "       index=[\"{}(真實)\".format(i) for i in range(10)],\n",
        "       columns=[\"{}(預測)\".format(i) for i in range(10)])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k1V4hVmE8keV"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wlO3lVsKaVvW"
      },
      "source": [
        "import numpy as np\n",
        "idx = np.nonzero(pre != y_test)[0][:200]\n",
        "false_pre = pre[idx]\n",
        "false_ori = y_test[idx]\n",
        "false_img = x_test[idx]\n",
        "\n",
        "plt.figure(figsize=(14, 42))\n",
        "width = 10\n",
        "height = len(idx) // width + 1\n",
        "for i in range(len(idx)):\n",
        "    plt.subplot(height, width, i+1)\n",
        "    t = \"[O]:{}\\n[P]:{}\".format(false_ori[i], false_pre[i])\n",
        "    plt.title(t)\n",
        "    plt.axis(\"off\")\n",
        "    plt.imshow(false_img[i])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qmYIDjwued_l"
      },
      "source": [
        "# PIL(pillow)\n",
        "from tensorflow.keras.preprocessing.image import load_img\n",
        "from PIL import Image\n",
        "fn = input(\"檔名\")\n",
        "# img = Image.open(fn).resize((28, 28)).convert(\"L\")\n",
        "img = load_img(fn, target_size=(28, 28)).convert(\"L\")\n",
        "img = np.array(img)\n",
        "img_r = img.reshape(1, 784) / 255\n",
        "proba = model.predict(img_r)[0]\n",
        "for i in range(10):\n",
        "    print(i, \"的機率:\", round(proba[i], 3))\n",
        "ans = model.predict_classes(img_r)[0]\n",
        "print(\"答案:\", ans)\n",
        "plt.imshow(img)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yo34CpGQsvGa"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
