import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engine.imputation import MeanMedianImputer

sns.set_style('whitegrid')

data = np.random.randn(100)
sns.histplot(data)
plt.show()
