import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import kurtosis
from sklearn.linear_model import LinearRegression


def plot_dist(data: pd.DataFrame, axes: plt.Axes, bins: int, title: str) -> None:

    dist = sns.displot(data, kde=True, bins=bins)

    dist.set(xticks=np.arange(int(min(data)), int(max(data)) + 1))
    dist.set(title=title)

    # for ax in dist.axes.flat:
    #     # get y min and max
    #     ymin, ymax = ax.get_ylim()

    #     # add vertical lines
    #     ax.vlines(x=[5], ymin=ymin, ymax=ymax,
    #               colors="tab:red", ls='--', lw=2)

    return


def stats_analysis(data: pd.DataFrame) -> None:

    conc = data["Concentration (ppb)"]
    print(f"Total arsenic concentration (ppb) break down:\n {conc.describe()}")
    print(f"Kurtosis: {kurtosis(conc)}")

    above = conc[conc > 5]

    print(
        f"Percentage of observations above cutoff: {(len(above) / len(conc) * 100):.2f}%")

    log_data = data
    log_data["Concentration (ppb)"] = log_data["Concentration (ppb)"].apply(lambda x: np.log10(x))
    log_conc = log_data["Concentration (ppb)"]
    print(f"Total arsenic concentration (ppb) break down:\n {log_conc.describe()}")

    # ax = plt.subplot()
    # plot_dist(conc, ax, len(conc), "Arsenic concentration distribution (ppb)")
    # plot_dist(log_conc, ax, len(conc), "Arsenic concentration distribution (ppb) (log10)")

    years = [df for _, df in log_data.groupby(log_data["Year"])]

    _, axes = plt.subplots(1, len(years))
    years_above = []
    mean_year = {}
    for i, year in enumerate(years):
        year_date = min(year['Year'])
        year_conc = year["Concentration (ppb)"]
        mean_year[int(year_date)] = year_conc.mean()
        print(
            f"Arsenic concentration (ppb) breakdown for {year_date}:\n{year_conc.describe()}")
        print(f"Kurtosis: {kurtosis(conc)}")

        above = year_conc[year_conc > 5]

        if year_conc.median() >= 5:
            years_above.append(year_date)

        print(
            f"Percentage of observations above cutoff (): {(len(above) / len(year) * 100):.2f}%")

        plot_dist(year_conc, axes[i], len(
            year_conc), f"Arsenic concentration distribution (ppb) ({year_date})")

    print(years_above)

    _, ax = plt.subplots()
    lp = sns.regplot(x="Year", y="Concentration (ppb)", data=log_data, x_ci=0.01)
    lp.set(xticks=np.arange(2013, 2023))
    lp.set(title="Mean arsenic concentration (ppb) by year")

    model = LinearRegression().fit(np.array(list(mean_year.keys())).reshape(-1, 1), np.array(list(mean_year.values())))
    r_sq = model.score(np.array(list(mean_year.keys())).reshape(-1, 1), np.array(list(mean_year.values())))
    print(f"r-value: {r_sq}")

    print(f"Slope: {model.coef_}")

    plt.show()

    return


if __name__ == "__main__":

    data = pd.read_excel("data.xlsx", "Juice")

    stats_analysis(data)

