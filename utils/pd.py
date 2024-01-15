import pandas as pd
from typing import Literal, Optional



def display_dataframe(df: pd.DataFrame, display_mode: Literal['head', 'tail', 'sample', None]='head', 
                      n_cols: Optional[int]=None, n_rows: int=5):
    
    n_cols = df.columns.size if n_cols is None else n_cols
    
    with pd.option_context('display.max_columns', n_cols):
        if display_mode is None:
            display(df)
        elif display_mode == 'head':
            display(df.head(n_rows))
        elif display_mode == 'tail':
            display(df.tail(n_rows))
        elif display_mode == 'sample':
            display(df.sample(n_rows))
        else:
            raise ValueError('The entered display_type is not supported.')


def display_df_desc(df:pd.DataFrame, digits: Optional[int]=3):
    if digits is None:
        display(df.describe().T)
    else:
        option_context = pd.option_context( 'display.float_format', ('{:.'+str(digits)+'f}').format )
        with option_context:
            display(df.describe().T)