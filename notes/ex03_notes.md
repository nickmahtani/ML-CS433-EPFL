### Least Squares

- it is called least squares becasue it minimizes the sum of squared erros and finds the smallest value of those squrares
- this is not iterating, you find the exact optimal w in one shot by solving the equation directly
- solve the normal equation
    - normal here means perpensicular
    - dot product tells you how much two vectors point in the same direction
        - if two vectors are perpendicular, their dot product is 0
        - the normal equation uses dot products
    - cross product only works in 3d
        - it takes two vectors and gives another vector that is perpendicular to both of them
    - we can apporach the normal eequation by:
        - caluculus: set the gradient of the MSE to 0
        - geometry: best prediction is the closest point to y in the column space of X. The shortest distance is always perpendicular so the dot product is 0 (error perpendicular ot the column space).
- no convergence, no learning rate, no iterations
- cons:
    - it involves solving a matrix equation which gets expensive if there are many features
    - cant be used for problems with millions of data points/ features


### Linear regression

- LR is the problem and everything else is the mothod to solve it
- LR: fit a linear model to the data by minimizing some cost function

### Solving linear equations with numpy

- np.linalg.inv is slower and less numerically stable than np.linalg.solve
- it solves aw=b

- VS code's IntelliSense cannot see function's type info when import * is used. The wildcard * hides where functions come from. If I want the intellisense popups, i need to import explicitly instead

### Basis Functions

- like the foundation/base of a building → minimal set of building blocks needed to construct
- it is a transformation that is applied to input data (X) to create new features
- basis is a set of building blocks that you can combine (with different weights) to express any function in a space
- something is a basis if:
    - it spans the space: any function can be built with combinations of your basis functions
    - linearly independent: no basis function can be built from the others
- the least squares doesent care about what the features are it just finds the best linear combination
- the model is still linear even if we use basis, linear in the columns of the matrix

### Root mean square error

- back to original units
- for the optimization step, it is the same to use rmse and mse. but for reporting and comparing, RMSE is better becasue it is in interpretable units
- howeverm it does depend on the scale of the data. when you switch from Kgs to grams, the RMSE increases super quickly
- statistical properties like R^2 fix this. It measures what fraction of the variance in y does the model explain (1 means perfect fit and it explains 100% of the variance in the data, 0 means teh model is no better than predicting the mean). It is scale independent
- Statistical properties:
    - scale invariance: doesnt change with units
    - interpretability: a percentage is universally meaningful
    - formal connection to statistical theory

### Vectorization

- if x is an array, x ** 2 leads to every element of the array being raised to the power of 2
- i can use np.column_stack to make a matrix directly

### To initialize or not to initialize

- if you need to fill cells one by one in a loop, initialize first
- if you are computing everything at once (with a method like column_stack for example) then it is not needed
- you need to initialize if the square brackets are involved: x[something] = : this means taht you are writing into an array

### np.random.permutation

- permute means rearranging in random order
- from mathematics, a permutation is any rearrangement of a set of elements
- the word means to change thouroughly (same root as mutation)
- :3 returns an arry of numbers upto 3

### Training and test sets

- the absolute number of training samples matters more than the ratio when you have lots of data.
- If you have lots of data, even a 10%-90% split could work well
