import numpy as np
import pandas as pd
from typing import Protocol
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from typing import Callable


class ScikitModel(Protocol):
    def fit(self, X, y, sample_weight=None): 
        ...
        
    def predict(self, X): 
        ...
        
    def score(self, X, y, sample_weight=None): 
        ...
        
    def set_params(self, **params): 
        ...


def get_ColumnTransformer_feature_names(columnTransformer:ColumnTransformer):

    output_features = []

    for name, transformer, features in columnTransformer.transformers_:
        if name!='remainder':
            trans_features = []
            if hasattr(transformer,'categories_'):
                trans_features.extend(transformer.get_feature_names_out(features))
            else:
                trans_features = features
            output_features.extend(trans_features)

    return output_features



class OutliersHandler(BaseEstimator, TransformerMixin):
    def __init__(self, strategy:Callable=np.mean, columns=None, iqr_multiply_by=1.5):
        self.iqr_multiply_by = iqr_multiply_by
        self.columns = columns
        self.strategy = strategy

    
    def fit(self, X:pd.DataFrame, y=None):
        return self

    
    def transform(self, X:pd.DataFrame, y=None):
        cols_to_transform = X.columns.to_list()

        if self.columns:
            cols_to_transform = self.columns

        transformed = X.assign(
            **{c: lambda df_, c=c: self._replace_ouliers(df_[c]) for c in cols_to_transform}
        )

        return transformed



class ReduceObjColsToOneCatCol(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None, reduced_col_name='Reduced'):
        self.columns = columns
        self.reduced_col_name = reduced_col_name

    
    def fit(self, X:pd.DataFrame, y=None):
        return self

    
    def transform(self, X:pd.DataFrame, y=None):
        cols_to_reduce = X.columns.to_list()

        if self.columns:
            cols_to_reduce = self.columns

        transformed = (
            X.assign(
                **{self.reduced_col_name: lambda df_: df_[cols_to_reduce].astype(str).agg(''.join, axis=1).astype('category')}
            )
            .pipe( lambda df_: df_.drop(cols_to_reduce, axis=1) )
        )

        self.categories_ = transformed.columns.to_list()

        return transformed

    def get_feature_names_out(self, features):
        return self.categories_



class ConvertObjColsToCat(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns

    
    def fit(self, X:pd.DataFrame, y=None):
        return self

    
    def transform(self, X:pd.DataFrame, y=None):
        cols_to_transform = X.columns.to_list()

        if self.columns:
            cols_to_transform = self.columns

        transformed = X.assign(
            **{col: lambda df_, col=col: df_[col].astype('category') for col in cols_to_transform}
    )
        self.categories_ = transformed.columns.to_list()
        return transformed

    def get_feature_names_out(self, features):
        return self.categories_