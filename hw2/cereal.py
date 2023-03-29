import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def stats_analysis(data: pd.DataFrame) -> None:
    
    favorite = np.array(data.loc[9, :].values.flatten().tolist()[1:-1])

    d = {}
    for i in range(21):
        if i == 9: continue
        row = data.loc[i, :].values.flatten().tolist()
        vector = np.array(row[1:-1])
        d[np.linalg.norm(vector - favorite)] = row[0]

    print(d)
    print(d[min(d.keys())])

    for k in sorted(d.keys()):
        print(d[k])

    print(data.corr().loc["rating", :])
        
    x = data[["protein", "fiber", "calories", "sodium"]]
    y = data["rating"]


    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 100)

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

    return

if __name__ == '__main__':
    data = pd.read_excel('data.xlsx', 'Cereals')

    stats_analysis(data)
    