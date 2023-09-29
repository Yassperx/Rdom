import numpy as np
import json
from sklearn.metrics import accuracy_score, log_loss
from tqdm import tqdm
import matplotlib.pyplot as plt


class DeepNeuralNetwork:
    """A deeplearning model"""
    def __init__(self, dimensions):
        """Initialisation"""
        self.dimensions = dimensions
        self.parameters = self._initialize_parameters()

    def _initialize_parameters(self):
        """Paramters initialisations"""
        parameters = {}
        C = len(self.dimensions)
        np.random.seed(1)
        for c in range(1, C):
            parameters['W' + str(c)] = np.random.randn(self.dimensions[c],
                                                       self.dimensions[c-1]) * 0.01
            parameters['b' + str(c)] = np.zeros((self.dimensions[c], 1))
        return parameters

    def forward_propagation(self, X):
        """Forward Propagation"""
        activations = {'A0': X}
        C = len(self.parameters) // 2

        for c in range(1, C + 1):
            Z = self.parameters['W' + str(c)].dot(
                activations['A' + str(c - 1)]) + self.parameters['b' + str(c)]
            activations['A' + str(c)] = 1 / (1 + np.exp(-Z))

        return activations

    def back_propagation(self, y, activations):
        """Back Propagation"""
        m = y.shape[1]
        C = len(self.parameters) // 2

        dZ = activations['A' + str(C)] - y
        gradients = {}

        for c in reversed(range(1, C + 1)):
            gradients['dW' + str(c)] = 1/m * np.dot(dZ,
                                                    activations['A' + str(c - 1)].T)
            gradients['db' + str(c)] = 1/m * np.sum(dZ, axis=1, keepdims=True)
            if c > 1:
                dZ = np.dot(self.parameters['W' + str(c)].T, dZ) * activations['A' + str(
                    c - 1)] * (1 - activations['A' + str(c - 1)])

        return gradients

    def update(self, gradients, learning_rate):
        """Updating parameters with gradients"""
        C = len(self.parameters) // 2

        for c in range(1, C + 1):
            self.parameters['W' + str(c)] = self.parameters['W' +
                                                            str(c)] - learning_rate * gradients['dW' + str(c)]
            self.parameters['b' + str(c)] = self.parameters['b' +
                                                            str(c)] - learning_rate * gradients['db' + str(c)]

    def predict(self, X):
        """Predict a value"""
        activations = self.forward_propagation(X)
        C = len(self.parameters) // 2
        Af = activations['A' + str(C)]
        return Af >= 0.5

    def train(self, X, y, learning_rate=0.001, n_iter=3000):
        """Train Function"""
        training_history = np.zeros((int(n_iter), 2))
        C = len(self.parameters) // 2

        # gradient descent
        for i in tqdm(range(n_iter)):
            activations = self.forward_propagation(X)
            gradients = self.back_propagation(y, activations)
            self.update(gradients, learning_rate)
            Af = activations['A' + str(C)]

            # calculating log_loss and accuracy
            training_history[i, 0] = (log_loss(y.flatten(), Af.flatten()))
            y_pred = self.predict(X)
            training_history[i, 1] = (accuracy_score(y.flatten(), y_pred.flatten()))

        # Plot training curve
        self._plot_training_curve(training_history)
        
    def _plot_training_curve(self, training_history):
        """Ploting the curve"""
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(training_history[:, 0], label='train loss')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(training_history[:, 1], label='train acc')
        plt.legend()
        plt.show()

    def save_parameters(self, file_name="data.json"):
        """Saving in a data.json file"""
        params_dict = {}
        for key, value in self.parameters.items():
            params_dict[key] = value.tolist()

        with open(file_name, "w") as f:
            json.dump(params_dict, f, indent=4)

    def load_parameters(self, file_name="data.json"):
        """Loading from a data.json file"""
        with open(file_name, "r") as f:
            loaded_params = json.load(f)

        for key, value in loaded_params.items():
            self.parameters[key] = np.array(value)
