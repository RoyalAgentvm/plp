import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests as rq

def numpy_mean():
    my_array =np.array([1,2,3,4,5,6,7,8,9,10])
    print(f'the mean of the array:',np.mean(my_array))

numpy_mean()

def panda_dataset():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    iris_df = pd.read_csv(url)
    print(iris_df.describe())
    print("\n")

panda_dataset()

def public_api():
    api_url = "https://jsonplaceholder.typicode.com/users/1"
    response = rq.get(api_url)
    user_data = response.json()
    print(f"User Name: {user_data['name']}")
    print(f"Email: {user_data['email']}")
    print(f"Company: {user_data['company']['name']}")
    print("\n")

public_api()

def line_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title("Simple Line Graph")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)
    plt.show() 

line_plot()