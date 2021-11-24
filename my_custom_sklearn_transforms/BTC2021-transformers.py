from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class DropColumnsAndFillUnknownEntries(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        # Drop colunmas indeseadas
        data = data.drop(labels=self.columns, axis='columns')
        #Fill
        data.loc[data['CHECKING_BALANCE'] == "NO_CHECKING", 'CHECKING_BALANCE'] = 0
        data.loc[data['EXISTING_SAVINGS'] == "UNKNOWN", 'EXISTING_SAVINGS'] = 0
        #Convert Object type to float
        data['CHECKING_BALANCE'] = data['CHECKING_BALANCE'].astype(float, errors = 'raise')
        data['EXISTING_SAVINGS'] = data['EXISTING_SAVINGS'].astype(float, errors = 'raise')
        
class EncodingCategoricalVariablesOfColumn(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        # Columnas One-hot-encoding del dataset usando get_dummies
        data = pd.get_dummies(data, columns=self.columns)   
        return data
