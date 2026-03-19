# Exercise 02 Notes

### Initialization

- Height as the input variable `x`
- Weight as the output variable `y`
- The columns of `x` contain the height values (the height feature)
- The first column of `x` is the bias/intercept term
    - It allows us to write the linear model compactly as a matrix-vector product
- The rows represent one data point (one person)
- `e` is the residual, the difference between the actual weight of person n and what the linear model predicts for that person
- `%matplotlib inline` is a magic command to tell the notebook to display plots directly inside the notebook instead of opening them in a separate window
- `%` marks magic commands — special instructions for Jupyter that aren't regular Python code
- `%load_ext autoreload` loads the autoreload extension
- `%autoreload 2` tells Jupyter to re-import any `.py` files every time you run a cell
- A helper is a `.py` file containing utility functions that you use but don't want to clutter the notebook
- `datetime` is a built-in Python library for working with dates and times — can be used to timestamp or measure how long certain computations take

### Euclidean Norm

- It is the length in space, like the Pythagorean theorem, but it generalizes to any number of dimensions

![image.png](attachment:55f9cb37-6706-4519-b5d2-82b9eb9ccf42:image.png)

### Helper.py

- **`load_data`**:
    - `sub_sample=True`: takes every 50th data point to make the dataset smaller
    - `add_outlier`: adds 2 fake people with realistic height but with weights still in pounds to simulate a mistake
- **`standardize`**:
    - Normalizes data to have mean of 0 and standard deviation of 1 because gradient descent works better when features are on a similar scale
- **`build_model_data`**:
    - `np.c_` concatenates columns side by side
- **`batch_iter`** is for stochastic gradient descent:
    - Instead of computing the gradient on all data points, SGD picks a small random subset

### Compute Loss

- `.dot()` is NumPy's method for matrix multiplication
- You don't have to transpose in Python — `.dot()` is clever enough to handle it
- In `e.dot(e)`, both are 1D arrays of the same shape, so NumPy does element-wise multiplication and sum — no transpose needed. However, for `tx.dot(e)`, `tx` is a 2D array so the dimensions won't align and you need to transpose it with `tx.T`

### Grid Search

- It is the simplest optimization method: brute force

### Gradient Descent

- The gradient is not the same thing as the parameters
- It tells us how much the loss changes when the parameters are changed — it's a direction
- The gradient is the derivative in two directions; it is the vector of partial derivatives
- The derivative and the gradient point in the direction of the steepest increase
- The gradient descent step points you in the opposite direction so that you move towards the minimum
- The gradient is larger when we are farther from the minimum
- MSE in particular is a quadratic function, so it behaves like a bowl
- In theory, gradient descent converges to the optimum on convex functions

### Stochastic Gradient Descent

- SGD needs more iterations than GD to converge, but the total time is less
- `yield` is like `return`, but instead of ending the function it pauses and gives you one result

### Subgradient Descent

- Regular gradient descent needs the function to be differentiable everywhere: smooth slope at every point
- For MAE, there is no slope at 0 (a kink)
