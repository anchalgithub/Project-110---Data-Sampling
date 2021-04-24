print("Hello!\nToday, we are taking 30 random samples from a population and we are repeating it 100 times then we are finding the mean & SD of pop and mean & SD of the samples.")
import csv
import statistics
import random
import pandas as pd
import plotly.figure_factory as ff


df=pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
print("Population mean: ", statistics.mean(data))
print("Population standard deviation: ", statistics.stdev(data))


#finding the mean of 30 random sample data
#sample is a portion of the population and population is how much data there is.
def random30means(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data))
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean


#after printing the 30 random samples, 100 times and storing it in a list. we are creating a graph to display everything. 
def show_fig(mean_list):
    df=mean_list
#taking the mean_list(df) out of the data(temp)
    fig=ff.create_distplot([df], ["reading_time"], show_hist=False)
#showing the graph
    fig.show()


#repeating the process for 100 times and then storing it in a list named mean_list.
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random30means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    
    print("Sampling data mean: ", statistics.mean(mean_list))

    SD=statistics.stdev(mean_list)
    print("Sampling data standard deviation: ", statistics.stdev(mean_list))
setup()

