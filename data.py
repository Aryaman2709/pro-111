import statistics
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].to_list()

mean = statistics.mean(data)

print('the mean is ', mean)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print(" Mean of the sampling distribution- ",mean)
    fig=ff.create_distplot([df],["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean], y = [0,1], mode = "lines", name = "MEAN"))
    fig.show()

def setup():
    mean_list =[]
    for i in range(0,100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

stddev = statistics.stdev(data)

first_std_deviation_start, first_std_deviation_end = mean-stddev, mean+stddev
second_std_deviation_start, second_std_deviation_end = mean-(2*stddev), mean+(2*stddev) 
third_std_deviation_start, third_std_deviation_end = mean-(3*stddev), mean+(3*stddev)

print("std1",first_std_deviation_start, first_std_deviation_end) 
print("std2",second_std_deviation_start, second_std_deviation_end) 
print("std3",third_std_deviation_start,third_std_deviation_end)

mean_list =[]
for i in range(0,100):
    set_of_mean = random_set_of_mean(30)
    mean_list.append(set_of_mean)
mean= statistics.mean(mean_list)

fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

data2 = df["responses"].tolist() 
mean_of_sample2 = statistics.mean(data2) 
print("mean of sample :- ",mean_of_sample2) 
fig = ff.create_distplot([mean_list], ["reading time"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF responses")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

Z_SCORE = (mean-mean_of_sample2)/stddev
print(Z_SCORE)