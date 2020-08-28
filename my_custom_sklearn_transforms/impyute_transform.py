import numpy
import scipy
from impyute.imputation.cs import mice
from sklearn.base import BaseEstimator, TransformerMixin

class MiceImputation(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        data = mice(data)
        return data   
