import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def stats_analysis(data: pd.DataFrame) -> None:
    success = data[data.fail == 0]
    num_success = len(success)
    fail = data[data.fail == 1]
    num_fail = len(fail)
    total = len(data)
    fail_ratio = num_fail / total

    print(num_fail)

    print(f"Number of successful runs: {((num_success / total) * 100):.2f}")
    print(f"Number of failed runs: {((num_fail / total) * 100):.2f}")

    temp_success = data["Temperature"][data.fail == 0]
    temp_fail = data["Temperature"][data.fail == 1]

    print(f"Stats table for success:\n {temp_success.describe()}")
    print(f"Stats table for fail:\n {temp_fail.describe()}")

    p_val = 0.05

    # given a 95% confidence level
    critical_val = 1.645

    # margin of error
    moe = critical_val * ((fail_ratio * (1 - fail_ratio)) / total)**.5

    print(f'Margin of error: {(moe * 100):.2f}%')

    # data.loc[data.Assistant == "hot", "Assistant"] = 1
    # data.loc[data.Assistant == "cold", "Assistant"] = 0

    data.loc[data.fail == 0, "fail"] = "Success"
    data.loc[data.fail == 1, "fail"] = "Fail"

    dates = {
        "jan": 0,
        "feb": 0,
        "march": 0,
        "april": 0,
        "may": 0,
        "june": 0,
        "july": 0,
        "aug.": 0,
        "sept.": 0,
        "oct.": 0,
        "nov.": 0,
        "dec.": 0
    }

    keys = list(dates.keys())

    for date in data[data.fail == "Fail"].Date:
        dates[keys[int(str(date)[5:7]) - 1]] += 1

    month_data = pd.DataFrame({
        "month": dates.keys(),
        "numOcc": dates.values()
    })

    sns.boxplot(data=data, x="Temperature", y="fail").set(title="Temperature (F) dist. by test result")
    # # sns.boxplot(data=data, x="Temperature", y="Assistant")
    #sns.barplot(month_data, x="month", y="numOcc").set(title="Number of failures by month")

    plt.show()

    return

if __name__ == "__main__":
    data = pd.read_excel("data.xlsx", "ProductTesting")
    stats_analysis(data)
