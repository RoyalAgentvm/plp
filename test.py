import matplotlib.pyplot as plt

def bar_chart():
    #sample data
    countries =['kenya','nigeria', 'china']
    population =[20000,40000,600000]

    plt.bar(countries,population)
    plt.title('countries population')
    plt.xlabel('countries')
    plt.ylabel('population')
    plt.show()

def pie_chart():
    #sample data
    activities =['sleeping', 'studying', 'eating','school','labs','sports']
    hours =[8,2,2,8,1,3]

    plt.pie(hours,labels=activities)
    plt.title('student hours')
    plt.show()

pie_chart()