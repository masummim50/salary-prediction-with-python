import pandas as pd
import math
import json
import matplotlib.pyplot as plt

data=pd.read_csv("./datasets/salary.csv")
headers=data.columns.values
x=data[headers[0]]
y=data[headers[1]]
x=x.truncate(4900,4999)
y=y.truncate(4900,4999)

with open("./trained/trained_data.txt") as file:
    data = file.read()
    converted = json.loads(data)
m=converted["m"]
c=converted["c"]
y_mean=converted["y_mean"]
y_predicted_list=[]
r_upper=0
r_lower=0
for index in range(len(x)):
    y_predicted = (m*x[index+4900])+c
    y_predicted_list.append(y_predicted)
    r_upper+=math.pow((y[index+4900]-y_predicted),2)
    r_lower+=math.pow((y[index+4900]-y_mean),2)

r_square=1-(r_upper/r_lower)
# print(r_square)

    
# display linear regression
# print(y_predicted_list)
# plt.scatter(x,y,color="g")
# plt.plot(x,y_predicted_list,color="r")
# plt.show()

choice = 1;
while(choice != -1):
    exp=int(input("Enter year of experience(-1 to quit): "))
    choice = exp
    predicted=(m*exp)+c
    predicted = round(predicted)
    print(f"Predicted salary: {predicted}")




    