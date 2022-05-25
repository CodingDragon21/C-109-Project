import csv
import pandas as pd 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('StudentsPerformance.csv')
data = df['reading score'].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)

print('The mean is: ',mean)
print('The median is: ', median)
print('The mode is: ', mode)
print('The standard deviation is: ', std_dev)


firstStandardDeviationStart, firstStandardDeviationEnd = mean - std_dev, mean + std_dev
secondStandardDeviationStart, secondStandardDeviationEnd = mean - (2*std_dev), mean + (2*std_dev)
thirdStandardDeviationStart, thirdStandardDeviationEnd = mean - (3*std_dev), mean + (3*std_dev)

firstListStdDev = [result for result in data if result > firstStandardDeviationStart and result < firstStandardDeviationEnd]
secondListStdDev = [result for result in data if result > secondStandardDeviationStart and result < secondStandardDeviationEnd]
thirdListStdDev = [result for result in data if result > thirdStandardDeviationStart and result < thirdStandardDeviationEnd]

print('% of data within 1st standard deviaton', len(firstListStdDev) *100/ len(data))
print('% of data within 2nd standard deviaton', len(secondListStdDev) *100/ len(data))
print('% of data within 3rd standard deviaton', len(thirdListStdDev) *100/ len(data))


fig = ff.create_distplot([data] , ["Reading Scores"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [firstStandardDeviationStart,firstStandardDeviationStart], y = [0, 0.5], mode = 'lines', name = 'std_dev_1start'))
fig.add_trace(go.Scatter(x = [firstStandardDeviationEnd,firstStandardDeviationEnd], y = [0, 0.5], mode = 'lines', name = 'std_dev_1end'))
fig.add_trace(go.Scatter(x = [secondStandardDeviationStart, secondStandardDeviationStart], y = [0, 0.5], mode = 'lines', name = 'std_dev_2start'))
fig.add_trace(go.Scatter(x = [secondStandardDeviationEnd, secondStandardDeviationEnd], y = [0, 0.5], mode = 'lines', name = 'std_dev_2end'))
fig.add_trace(go.Scatter(x = [thirdStandardDeviationStart, thirdStandardDeviationStart], y = [0, 0.5], mode = 'lines', name = 'std_dev_3start'))
fig.add_trace(go.Scatter(x = [thirdStandardDeviationEnd, thirdStandardDeviationEnd], y = [0, 0.5], mode = 'lines', name = 'std_dev_3end'))
fig.show()