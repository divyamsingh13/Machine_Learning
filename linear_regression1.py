import numpy
from sklearn import linear_model
x=[[4],[6],[8],[9]]
y=[[24],[36],[48],[54]]
mm=linear_model.LinearRegression()
mm.fit(x,y)
print(mm.predict([[10]]))
print(mm.coef_)
print(mm.intercept_)
