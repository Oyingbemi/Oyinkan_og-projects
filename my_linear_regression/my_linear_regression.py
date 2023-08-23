import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def h(x, theta):
    return np.dot(x, theta)[:, np.newaxis]

def mean_squared_error(y_predicted, y_label):
    difference = y_predicted - y_label
    point_wise_sqr_diff = np.square(difference)
    sum = np.sum(point_wise_sqr_diff)
    return sum/len(y_label)

class LeastSquaresRegression():
    def __init__(self,):
        self.theta_ = None  
        
    def fit(self, X, y):
        # Calculates the pseudoinverse and finds optimal weights
        self.theta_ = np.dot(np.linalg.pinv(X), y)
        
    def predict(self, X):
        # Make predictions for data X, i.e output y = h(X) (See equation in Introduction)
        # use h(x, theta) 
        y_pred = h(X, self.theta_)
        return y_pred

def bias_column(X):
    ones_dim = (np.shape(X)[0],1) # same num of rows,but 1 column
    return np.c_[np.ones(ones_dim), X]

def my_plot(X, y, y_new):
    plt.scatter(X, y, color='b')
    plt.plot(X,y_new, color='r', linewidth=3)
    plt.legend(['predicted' , 'true'])
    plt.savefig('true_vs_predicted.png')

class GradientDescentOptimizer():

    def __init__(self, f, fprime, start, learning_rate = 0.001):
        self.f_      = f                       # The function
        self.fprime_ = fprime                  # The gradient of f
        self.current_ = start[:,np.newaxis]                   # The current point being evaluated
        self.learning_rate_ = learning_rate    # Does this need a comment ?

        # Save history as attributes
        self.history_ = [start]
    
    def step(self):
        # Take a gradient descent step
        # 1. Compute the new value and update selt.current_
        # 2. Append the new value to history
        # Does not return anything
        diff = self.learning_rate_*self.fprime_(self.current_)
        new_val = self.current_ - diff
        self.current_ = new_val
        self.history_.append(new_val)
        
    def optimize(self, iterations = 1000):
        # Use the gradient descent to get closer to the minimum:
        # For each iteration, take a gradient step
        for i in range(iterations):
            self.step()

    def getCurrentValue(self):
      # Getter for current_
        return self.current_.flatten()
        
    def print_result(self):
        print("Best theta found is " + str(self.current_))
        print("Value of f at this theta: f(theta) = " + str(self.f_(self.current_)))
        print("Value of f prime at this theta: f'(theta) = " + str(self.fprime_(self.current_)))

def f(x):
    a = np.array([[2],[6]])
    t = lambda x: 3 + np.matmul((x - a).T,(x - a))
    return t(x)
    
def f_prime(x):
    a = np.array([[2],[6]])
    t = lambda x: 2*(x - a)
    return t(x)

