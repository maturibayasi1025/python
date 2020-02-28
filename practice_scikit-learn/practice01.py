import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1,np.nan,3,4,5],
    'B': [6,7,8,np.nan,10],
    'C': [11,12,13,14,np.nan]
})

print(df.isnull())

print(df)