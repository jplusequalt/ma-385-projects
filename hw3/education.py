import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def stats_analysis(data: pd.DataFrame) -> None:

    x = data.drop(["School"], axis=1, inplace=False)
    y = data["Ranking"]

    # df_log = data.copy()
    # df_log["Research"] = np.log(df_log["Research"])
    # print(data["Research"])
    # print(df_log["Research"])
    # dist1 = sns.displot(data["Research"], kde=True, bins=150)
    # dist2 = sns.displot(df_log["Research"], kde=True, bins=150)

    # plt.show()

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 100)

    mlr = LinearRegression()
    mlr.fit(x_train, y_train)

    importances = pd.DataFrame(data={
        'Attribute': x_train.columns,
        'Importance': mlr.coef_
    })

    

    print(x.transform(lambda x: np.log(x)).corr().loc["Ranking", :].sort_values(ascending=False))
    
    print(f"Intercepts: {mlr.intercept_}")

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

    df_log = data.copy()
    df_log["Research"] = np.log(df_log["Research"])
    print(data["Research"])
    print(df_log["Research"])
    dist1 = sns.displot(data["Research"], kde=True, bins=150).set(title="Before log trans.")
    dist2 = sns.displot(df_log["Research"], kde=True, bins=150).set(title="After log trans.")

    plt.show()

    return


if __name__ == "__main__":
    data = pd.read_excel("data.xlsx", "Education")

    stats_analysis(data)
