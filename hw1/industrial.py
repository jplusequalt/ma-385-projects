import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from scipy.stats import kurtosis

def stats_analysis(data: pd.DataFrame) -> None:

    on_time = data['Delivery Time'][data['Delivery Time'] < 30.0]
    total_on_time = len(on_time)
    late = data['Delivery Time'][data['Delivery Time'] > 30.0]
    total_late = len(late)

    print(f'Number of on time deliveries: {total_on_time}')
    print(f'Number of late deliveries: {total_late}')
    print(f'Percentage of on time deliveries: {(total_on_time / len(data["Delivery Time"]))*100:.2f}%')
    print(f'Percentage of on time deliveries w/ max data point removed: {(total_on_time / (len(data["Delivery Time"]) - 1))*100:.2f}%')
    print(f'Stats table:\n {data.describe()}')
    
    sorted_data = data['Delivery Time'].sort_values().to_list()
    iqr = sorted_data[89] - sorted_data[29]

    print(f'Interquartile range: {sorted_data[89]} - {sorted_data[29]} = {iqr:.2f}')

    times = data['Delivery Time']

    print(f'Kurtosis: { kurtosis(times) }')

    fig, ax = plt.subplots(constrained_layout=True)
    n, _, patches = ax.hist(data['Delivery Time'], bins=[n for n in range(0, 60, 1)], color='green')
    ax.set_ylabel('Delivery time (min)')
    ax.set_xlabel('Delivery count')
    ax.set_title('Delivery time distribution')

    for i, _ in enumerate(n):
        if i > 29:
            patches[i].set_facecolor('red')

    #create legend
    handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in ['green', 'red']]
    labels = ['On time', 'Late']
    ax.legend(handles, labels)

    fig.savefig('./outputs/deliveries_hist.png')

    fig2, ax2 = plt.subplots(constrained_layout=True)
    bp = ax2.boxplot(data['Delivery Time'])
    ax2.set_ylabel('Delivery time (min)')
    ax2.set_xticks([])
    ax2.set_title('Delivery time boxplot')
    ax2.grid()
    bp['fliers'][0].set_markeredgecolor('green')
    bp['fliers'][0].set_markerfacecolor('green')
    bp['fliers'][0].set_label('On time outliers')

    late_outliers = []
    for x, y in zip(bp['fliers'][0].get_xdata(), bp['fliers'][0].get_ydata()):
        if y > 30.0:
            late_outliers.append([x, y])


    ax2.plot([x[0] for x in late_outliers], [x[1] for x in late_outliers], marker='o', markerfacecolor='r', markeredgecolor='r', linestyle='', label='Late Outliers')
    ax2.legend()

    fig2.savefig('./outputs/deliveries_bp.png')

    return


if __name__ == '__main__':
    data = pd.read_excel('data.xlsx', 'Industrial Engineering')
    stats_analysis(data)
