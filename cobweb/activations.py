import math

def sigmoid(x):
        return 1/(1+math.exp(-x))

def dsigmoid(y):
    return y * (1 - y)

def relu(x):
    return max(x, 0)

def drelu(x):
    return 1 if x >= 0 else 0

def tanh(x):
    return math.tanh(x)

def dtanh(y):
    return 1 - (y * y)

class Activation:
    def __init__(self, func, dfunc):
        self.func = func
        self.dfunc = dfunc

activations = {
    "sigmoid": Activation(sigmoid, dsigmoid),
    "relu": Activation(relu, drelu),
    "tanh": Activation(tanh, dtanh),
}

def get(name):
    return activations[name]
