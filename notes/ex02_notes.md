### Initialization

- Height as the input variable x
- Weight as the output variable y
- the columns of x contain the height values (the height feature)
- the first column of x is the bias/intercept term
    - it allows us to write the linear model compactly as a matrix vector product
- the rows represent 1 data point (one person)
- e is the residual, the difference between the actual weight of the person n and what the linear model predicts for that person.
- %matplotlib inline it is a magic command to tell the notebook to display plots directly inside the notebook instead of opening them in a seperate windeow
- % marks magic commands. they are special instructions for jupyter that arent regular python code.
- %load_ext autoreload loard the autoreload extension
- %autoreload 2 tells jupyter to re-import any py files everytime i run a cell
- helper is a .py filke containing utility fiucntions that you use but dont want to clutter the notebook
- datetime is a built in python library for working with dates and times. can be used to timestamp or measure how long certain compuations take.

### Euclidian Norm

- it is the length in space. like the pythagorean theorem. But it generalizes to any number of dimensions

![image.png](attachment:55f9cb37-6706-4519-b5d2-82b9eb9ccf42:image.png)

### Helper.py

- load_data:
    - sub_sample = True: takes every 50th data point to make the dataset smaller.
    - add_outlier: adds 2 fake people with realistic height but with weights still in pounds to simulate a mistake
- standardize:
    - normalizes data to have mean of 0 and sd of 1 because gradient descent works better when features are on a similar scale.
- build_model_data
    - np.c_ concatenates columns side by side
- batch_iter is for stochastic gradient descent
    - instead of computing the gradient on all data points, SGD picks a small random subset

### Compute_loss

- .dot() is numpys method for matrix multiplication
- you dont have to transpose in python, the .dot() is clever enough to do it
- in e.dot(e), but are 1D arrays of the same shape so Numpy is smart to do element-wise multiplication and sum. So no transpose is needed. However, for tx.dot(e), tx is a 2D array so the dimensions will not allign and I need to transpose it with **tx.T**

### Grid search

- it is the simplest optimization method: brute force

### Gradient Descent

- the gradient is not the same thing as the parameters
- it tells us how much the loss changes when the parameters are changed. Its a direction
- gradient is teh derivative in two directions. it is the vector of partial derivatives
- the derivative and teh gradient points in the direction of the steepest increase.
- The gradient descent step points you in the opposite direction so that you move towards the minimum
- the gradient is larger when we are farther from the minimum
- MSE in particular is a quadratic function, so it behaves like a bowl
- in theory, gradient descent converges to the optimum on convex functions

### Stochastic gradient descent

- SGD needs more iterations GD to converge but the total time is less
- yield is like return but instead of ending the function it pauses and gives you one result

### Subgradient descent

- regular gradient descent needs the function to be differentiable everywhere: smooth slope at every point
- for MAE, there is not slope at 0 (a kink)