"""Activation Functions"""
import math

#  thanks to: https://stackoverflow.com/a/29863846
#  and https://timvieira.github.io/blog/post/2014/02/11/exp-normalize-trick/
def sigmoid(x):
    "Numerically-stable sigmoid function."
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    else:
        z = math.exp(x)
        return z / (1 + z)

def relu(x):
    "ReLU implementation"
    return x if x > 0 else 0

def tanh(x):
    "hyperbolic tan of x"
    return math.tanh(x)
