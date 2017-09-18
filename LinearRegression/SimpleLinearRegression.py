
class SimpleLinearRegression(object):
    """Least Squares Linear Regression
    
    Linear Regression from scratch based on:
    https://v1shwa.github.io/blog/understanding-the-math-of-linear-regression/
    """
    def __init__(self):
        self.coef = None
        self.intercept = None

    def fit(self, X,y):
        """Fit a linear model 
        
        Arguments:
            X {list} -- List of features
            y {list} -- List of outcomes
        """

        # Find, Σx
        X_sum = sum(X)

        # Find, Σy
        y_sum = sum(y)

        # Σx²
        Xsq_sum = sum([cx**2 for cx in X])

        # Find, Σxy
        Xy_sum = sum([cx*cy for cx,cy in zip(X,y)])

        # Find, n (no. of features)
        n = len(X)

        # We know, 
        ## Co-eff = b1 = nΣxy-ΣxΣy / nΣx² - (Σx)²
        self.coef = (n*Xy_sum - X_sum*y_sum) / (n*Xsq_sum - (X_sum**2))

        ## Intercept = b0 = (Σy-(b1*Σx)) / n
        self.intercept = (y_sum - (b1*X_sum)) / n

        return self

    def predict(self, X_test):
        """Predict the response for given input
        
        Arguments:
            X_test {int} -- Input X
        """
        if self.coef is None:
            raise ValueError("Please run .fit() to predict anything..")

        y_test =  self.intercept + (self.coef*X_test)
        return y_test

if __name__ == '__main__':
    print("Simple Linear Regression based on https://v1shwa.github.io/blog/understanding-the-math-of-linear-regression/")