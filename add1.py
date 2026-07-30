import pandas as pd


data={
    "name":["name1","name2","name3"],
    "age":[22,23,24]

}
df=pd.DataFrame(data)
print(df)



#example
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[6,7,8,9,10]
plt.scatter(x,y)
plt.title("student marks")
plt.show()
