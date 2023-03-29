import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import mannwhitneyu
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def stats_analysis(data: pd.DataFrame) -> None:
    
    m_enrollment = data["PrimarySchoolEnrollmentMale"]
    f_enrollment = data["PrimarySchoolEnrollmentFemale"]

    print(f"Male enrollment stats:\n{m_enrollment.describe()}")
    print(f"Female enrollment stats:\n{f_enrollment.describe()}")

    U, p = mannwhitneyu(m_enrollment, f_enrollment, alternative="two-sided")

    print(f"U stat: {U}")
    print(f"p-val: {p}")

    alpha = 0.05

    if p >= alpha:
        print("Fail to reject null hypothesis")
    else:
        print("Null hypothesis rejected")

    # sns.displot(m_enrollment, bins=100).set(xlabel="Male enrollment (%)")
    # sns.displot(f_enrollment, bins=100).set(xlabel="Female enrollment (%)")

    data["Enrollment"] = [(i + j) / 2 for i, j in zip(m_enrollment, f_enrollment)]

    # fig, ax = plt.subplots()
    # ax.scatter(data["Enrollment"], data["LifeExpectancy"])

    print(data["GNI"].describe())

    x = data[["Enrollment", "GNI", "ChildMortality", "Over60", "FertilityRate"]]
    y = data["LifeExpectancy"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

    mlr = LinearRegression()
    mlr.fit(x_train, y_train)

    print(f"Intercepts: {mlr.intercept_}")
    print(f"Coefficients:\n{list(zip(x, mlr.coef_))}")

    y_pred = mlr.predict(x_test)
    mlr_diff = pd.DataFrame({
        "Actual": y_test,
        "Predicted": y_pred,
        "Diff": [p - a for a, p in zip(y_test, y_pred)]
    })

    print(mlr_diff)

    meanAbErr = metrics.mean_absolute_error(y_test, y_pred)
    meanSqErr = metrics.mean_squared_error(y_test, y_pred)
    rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    
    print('R squared: {:.2f}'.format(mlr.score(x,y)*100))
    print('Mean Absolute Error:', meanAbErr)
    print('Mean Square Error:', meanSqErr)
    print('Root Mean Square Error:', rootMeanSqErr)

    plt.show()

    return

if __name__ == '__main__':
    data = pd.read_excel('data.xlsx', 'Countries')

    stats_analysis(data)
    