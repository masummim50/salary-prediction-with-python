import pandas as pd
import math
import json


salary_data = pd.read_csv("./datasets/salary.csv")

headers = salary_data.head()
print(headers);

def calculate_mean(data):
    sum=0
    for val in data:
        sum+=val
    mean=sum/len(data)
    return mean

headers = salary_data.columns.values
x=salary_data[headers[0]]
y=salary_data[headers[1]]

x=x.truncate(0,4899)
y=y.truncate(0,4899)

x_mean=calculate_mean(x)
y_mean=calculate_mean(y)

upper=0
lower=0


for index in range(len(x)):
    upper+=(x[index]-x_mean)*(y[index]-y_mean)
    lower+=math.pow(x[index]-x_mean,2)


m=upper/lower
c=y_mean-(m*x_mean)
trained_data={}
trained_data["m"]=m
trained_data["c"]=c
trained_data["y_mean"]=y_mean
with open("./trained/trained_data.txt",'w') as file:
    file.write(json.dumps(trained_data))