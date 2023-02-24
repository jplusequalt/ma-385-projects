import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

def stats_analysis(data: pd.DataFrame) -> None:
    data.drop(0, inplace=True)
    
    columns = {}
    for i, k in enumerate(data.keys()):
        if i % 2 == 0:
            columns[k] = k + 'A'
        else:
            split = k.split('.')[0]
            columns[k] = split + 'B'

    data.rename(columns=columns, inplace=True)

    a_data = data.loc[:, data.columns.str.contains('A')]
    b_data = data.loc[:, data.columns.str.contains('B')]

    print(a_data.describe())

    dist_a = sns.displot(a_data, kde=True, element='step', bins=100).set(title='Distributions for measurement A')
    dist_b = sns.displot(b_data, kde=True, element='step', bins=100).set(title='Distributions for measurement B')
    
    dist_a.figure.savefig('./outputs/dist_a.png')
    dist_b.figure.savefig('./outputs/dist_b.png')

    return

if __name__ == '__main__':
    data = pd.read_excel('data.xlsx', 'Defense Contracting')
    stats_analysis(data)
