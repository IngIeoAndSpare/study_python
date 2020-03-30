from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
import nn

def plot_history(history):
    n = history['epochs']
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    n = 4000
    plt.plot(range(history['epochs'])[:n], history['train_loss'][:n], label='train_loss')
    plt.plot(range(history['epochs'])[:n], history['test_loss'][:n], label='test_loss')
    plt.title('train & test loss')
    plt.grid(1)
    plt.xlabel('epochs')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(history['epochs'])[:n], history['train_acc'][:n], label='train_acc')
    plt.plot(range(history['epochs'])[:n], history['test_acc'][:n], label='test_acc')
    plt.title('train & test accuracy')
    plt.grid(1)
    plt.xlabel('epochs')
    plt.legend()

    
data = datasets.make_blobs(n_samples=1000, centers=2, random_state=2)
X = data[0].T
y = np.expand_dims(data[1], 1).T

neural_net = nn.NeuralNetwork([2, 4, 4, 1], seed=0)
history = neural_net.train(X=X, y=y, batch_size=16, epochs=100, learning_rate=0.4, print_every=200, validation_split=0.2,
                          tqdm_=False, plot_every=10)


data = datasets.make_moons(n_samples=1000, noise=0.1)
X = data[0].T
y = np.expand_dims(data[1], 1).T

neural_net = nn.NeuralNetwork([2, 4, 4, 1], seed=2)
history = neural_net.train(X=X, y=y, batch_size=32, epochs=500, learning_rate=0.4, print_every=200, validation_split=0.2,
                          tqdm_=False, plot_every=15)
