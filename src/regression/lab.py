#%%[markdown]
# # Lab: Prostate Cancer
# - Linear Regression with Least Square
# - Subset Selection
# - Shrinkage Methods
# - Principal Component Regression
# - Partial Least Square Regression

#%%
import math
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt

#%%[markdown]
# ## Data spec.
# The data for this example come from a study by Stamey et al. (1989). They examined the correlation between the level of prostate-specific antigen and a number of clinical measures in men who were about to receive a radical prostatectomy.
#%%
data = pd.read_csv('./data/prostate/prostate.data', delimiter='\t', index_col=0)
data.head(5)

#%%[markdown]
# A random vector $\mathrm{x}=(\mathrm{x}_1,...,\mathrm{x}_M)$ with a set of features $x \in \mathcal{X} \subset \mathbb{R}^M$ (with model size $M=8$)
# - `lcavol`: log cancer volumn ($x_1$)
# - `lweight`: log prostate weight ($x_2$)
# - `age`: age ($x_3$)
# - `lbph`: log of the amount of benign prostatic prostatic hyperplasia ($x_4$)
# - `svi`: seminal vesicle invasion ($x_5$)
# - `lcp`: log of capsular penetration ($x_6$)
# - `gleason`: Gleason score ($x_7$)
# - `pgg45`: percent of Geason score 4 or 5 ($x_8$)
#%%
x = data[['lcavol', 'lweight', 'age', 'lbph', 'svi', 'lcp', 'gleason', 'pgg45']]
x.head(5)

#%%[markdown]
# A target random variable $\mathrm{y}$ with the value $y \in \mathcal{Y} \subset \mathbb{R}$
# - `lpsa`: the level of prostate-specific antigen ($y$)
#%%
y = data[['lpsa']]
y.head(5)

#%%[markdown]
# Given dataset is denoted by $S=((x_1,y_1),...,(x_N,y_N))$ (with size $N=97$).

#%%[markdown]
# ## 


