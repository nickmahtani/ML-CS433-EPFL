# Exercise 03 Notes

### Least Squares

- It is called least squares because it minimizes the sum of squared errors and finds the smallest value of those squares
- This is not iterating — you find the exact optimal `w` in one shot by solving the equation directly
- Solve the **normal equation**:
    - "Normal" here means perpendicular
    - Dot product tells you how much two vectors point in the same direction
        - If two vectors are perpendicular, their dot product is 0
        - The normal equation uses dot products
    - Cross product only works in 3D
        - It takes two vectors and gives another vector that is perpendicular to both of them
    - We can approach the normal equation by:
        - **Calculus**: set the gradient of the MSE to 0
        - **Geometry**: the best prediction is the closest point to `y` in the column space of `X`. The shortest distance is always perpendicular, so the dot product is 0 (error perpendicular to the column space).
- No convergence, no learning rate, no iterations
- Cons:
    - It involves solving a matrix equation which gets expensive if there are many features
    - Can't be used for problems with millions of data points/features

### Linear Regression

- Linear regression is the **problem** and everything else is the **method** to solve it
- Linear regression: fit a linear model to the data by minimizing some cost function

### Solving Linear Equations with NumPy

- `np.linalg.inv` is slower and less numerically stable than `np.linalg.solve`
- It solves `Aw = b`
- VS Code's IntelliSense cannot see a function's type info when `import *` is used. The wildcard `*` hides where functions come from. If you want the IntelliSense popups, import explicitly instead

### Basis Functions

- Like the foundation/base of a building — a minimal set of building blocks needed to construct
- It is a transformation applied to input data (`X`) to create new features
- A basis is a set of building blocks that you can combine (with different weights) to express any function in a space
- Something is a basis if:
    - It **spans the space**: any function can be built with combinations of your basis functions
    - **Linearly independent**: no basis function can be built from the others
- Least squares doesn't care about what the features are — it just finds the best linear combination
- The model is still linear even if we use basis functions — linear in the columns of the matrix

### Root Mean Square Error

- Back to original units
- For the optimization step, it is the same to use RMSE and MSE. But for reporting and comparing, RMSE is better because it is in interpretable units
- However, it does depend on the scale of the data — when you switch from kg to grams, the RMSE increases dramatically
- Statistical properties like R² fix this. It measures what fraction of the variance in `y` the model explains (1 means perfect fit explaining 100% of the variance, 0 means the model is no better than predicting the mean). It is scale-independent
- Statistical properties:
    - **Scale invariance**: doesn't change with units
    - **Interpretability**: a percentage is universally meaningful
    - **Formal connection** to statistical theory

### Vectorization

- If `x` is an array, `x ** 2` raises every element of the array to the power of 2
- You can use `np.column_stack` to make a matrix directly

### To Initialize or Not to Initialize

- If you need to fill cells one by one in a loop, initialize first
- If you are computing everything at once (with a method like `column_stack` for example), then it is not needed
- You need to initialize if square brackets are involved: `x[something] = ...` means you are writing into an array

### `np.random.permutation`

- Permute means rearranging in random order
- From mathematics, a permutation is any rearrangement of a set of elements
- The word means to change thoroughly (same root as mutation)
- `[:3]` returns an array of numbers up to index 3

### Training and Test Sets

- The absolute number of training samples matters more than the ratio when you have lots of data
- If you have lots of data, even a 10%–90% split could work well
