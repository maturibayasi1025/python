import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    'A': [1,np.nan,3,4,5],
    'B': [6,7,8,np.nan,10],
    'C': [11,12,13,14,np.nan]
})

imp = SimpleImputer(strategy="mean")

imp.fit(df)

print(imp.transform(df))
