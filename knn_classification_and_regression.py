

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# Regression data: experience vs salary
Xr = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
yr = [35000, 37000, 40000, 43000, 50000, 52000, 56000, 60000, 65000, 70000]
Xr_train, Xr_test, yr_train, yr_test = train_test_split(Xr, yr, test_size=0.2, random_state=42)
reg = KNeighborsRegressor(n_neighbors=3).fit(Xr_train, yr_train)
yr_pred = reg.predict(Xr_test)
print('Regression MSE:', mean_squared_error(yr_test, yr_pred))
plt.scatter(yr_test, yr_pred)
plt.xlabel('Actual Salary')
plt.ylabel('Predicted Salary')
plt.title('KNN Regression')
plt.show()

# Classification data: marks vs pass/fail
Xc = [[35], [45], [50], [60], [65], [70], [80], [85], [90], [95]]
yc = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]  # 0=fail, 1=pass
Xc_train, Xc_test, yc_train, yc_test = train_test_split(Xc, yc, test_size=0.2, random_state=42)
clf = KNeighborsClassifier(n_neighbors=3).fit(Xc_train, yc_train)
yc_pred = clf.predict(Xc_test)
print('Classification Accuracy:', accuracy_score(yc_test, yc_pred))
plt.scatter([x[0] for x in Xc_test], yc_pred, c=yc_pred)
plt.xlabel('Marks')
plt.ylabel('Predicted (1=Pass, 0=Fail)')
plt.title('KNN Classification')
plt.show()
