import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
df = pd.read_csv (r'RCBD.csv')
print (df)
print (df.describe())
data = pd.melt(df.reset_index(), id_vars=['index'],value_vars=['A','B','C'])
data.columns = ['Block', 'Treatment', 'value']

model=ols('value ~ C(Block)+ C(Treatment)',data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
anova_table
print(anova_table)
