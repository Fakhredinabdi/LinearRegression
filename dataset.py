from sklearn.datasets import make_regression

class dataset:
    @staticmethod
    def getData(feature):
        X, y = make_regression(n_samples=1000, n_features=feature, noise=40)
        return X,y