# Implementation of Linear Regression from scratch using python


### [<u>Simple Linear Regression</u>](./SimpleLinearRegression.py):

Based on this [article](https://v1shwa.github.io/blog/understanding-the-math-of-linear-regression/) from [v1shwa.github.io](https://v1shwa.github.io/)

##### Usage

```python
# Let's take some random sample data
X = [20,16,19,18,17,15]
y = [88,71,93,84,80,75]
X_test = 14 # to test

from SimpleLinearRegression import SimpleLinearRegression
slr = SimpleLinearRegression()
clf = slr.fit(X,y)
## Now, we can predict using clf.predict()
y_pred = clf.predict(X_test)
```
