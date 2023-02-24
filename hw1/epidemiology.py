import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def stats_analysis(data: pd.DataFrame) -> None:

    sample_size = len(data['Treatment Outcome'])
    successes = len(data['Treatment Outcome'][data['Treatment Outcome'] == 1])
    failures = sample_size - successes
    efficacy = successes / sample_size

    print(f'Sample size: {sample_size}')
    print(f'Number of patients who did not get infected: {successes}')
    print(f'Number of patients who did get infected: {failures}')
    print(f'Efficacy rate: {(efficacy * 100):.2f}%')
    
    # given a 90% confidence level
    critical_val = 1.645

    # margin of error
    moe = critical_val * ((efficacy * (1 - efficacy)) / sample_size)**.5

    print(f'Margin of error: {moe * 100:.2f}%')

    # confidence interval for sample proportion is p_hat +- moe
    lower_bound = efficacy - moe
    upper_bound = efficacy + moe
    print(f'Confidence interval: {(lower_bound * 100):.2f}% < {(efficacy * 100):.2f}% < {(upper_bound * 100):.2f}%')

    
    fig, ax = plt.subplots(constrained_layout=True)
    groups = ('Immune', 'Infected')
    freqs = {
        'observed': [successes, failures],
        'expected': [round(sample_size * .9), round(sample_size * .1)]
    }
    x = np.arange(len(groups))
    width = 0.25
    mult = .5

    for attribute, measurement in freqs.items():
        offset = width * mult
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        mult += 1

    ax.set_ylabel('# of occurences')
    ax.set_title('Immunity frequency bar chart')
    ax.set_xticks(x + width, groups)
    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 35)

    fig.savefig('./outputs/immunity_bar.png')

    return

if __name__ == '__main__':
    data = pd.read_excel('data.xlsx', 'Epidemiology')

    stats_analysis(data)
    