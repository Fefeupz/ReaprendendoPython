import pandas as pd
import numpy as np

df1 = pd.DataFrame({'id':[1,2,3],
                    'cor':['branco','preto','verde']})
df2 = pd.DataFrame({'times':['time1', 'time2', 'time3', 'time4', 'time5'],
                    'id_cor':[1,1,2,3,2]})

df = pd.merge(df1, df2, left_on='id', right_on='id_cor')
print(df)