import matplotlib.pyplot as plt
def line_plot():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]

    # Create a line plot
    plt.plot(x, y)
    plt.title("Simple Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

def bar_chart():
    # Sample data
    names = ['Alice', 'Bob', 'Charlie']
    scores = [85, 90, 78]

    plt.bar(names, scores, color='skyblue')
    plt.title("Student Scores")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.show()

def pie_chart():
    # Sample data
    activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
    hours = [8, 2, 8, 6]

    plt.pie(hours, labels=activities, autopct='%1.1f%%')
    plt.title("Daily Activities")
    plt.show()

def histogram():
    # Example: showing frequency of values
    ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

    plt.hist(ages, bins=5, color='purple')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

histogram()  


import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Year': [2021, 2022, 2023],
    'Users': [1500, 3000, 5000]
}

df = pd.DataFrame(data)

# Plot using pandas + matplotlib
plt.plot(df['Year'], df['Users'], marker='o')
plt.title("User Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()