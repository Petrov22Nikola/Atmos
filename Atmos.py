import pandas
import numpy
import math
import statistics
import gpcharts
from gpcharts import figure

def readCsv(csv):
    result = numpy.genfromtxt(csv, delimiter=',')
    data = []
    for m in range(len(result)):
        if(result[m] > 0):
            data.append(result[m])
    return data

data = readCsv(r'C:\Users\infra\Desktop\2005.csv')
data2 = readCsv(r'C:\Users\infra\Desktop\2006.csv')
data3 = readCsv(r'C:\Users\infra\Desktop\2009.csv')
data4 = readCsv(r'C:\Users\infra\Desktop\2010.csv')
dev = statistics.stdev(data)
mean = statistics.mean(data)

def highlightData(data):
    highData = []
    for i in range(len(data)):
        if((data[i] - mean)/dev > 1 or (data[i] - mean)/dev < -1):
            highData.append(data[i])
    return(highData)

def graphData(data):
    graph = figure(title='Concentration Of CO Molecuoles In Atmosphere')
    graph.plot(data)

def regressData(data):
    y = 0
    x = 0
    xy = 0
    ySquare = 0
    xSquare = 0
    for i in range(len(data)):
        y += data[i]
        x += 1
        xy += x*y
        ySquare += y**2
        xSquare += x**2
    slope = (y*xSquare - x*xy)/(len(data)*xSquare - x**2)
    intercept = (len(data)*xy - x*y)/(len(data)*xSquare - x**2)
    determination = (len(data)*xy - x*y)/(math.sqrt((len(data)*xSquare)*(len(data)*ySquare) - y**2))
    gof = ""
    if(determination**2 < 0.33):
        gof = "Weak Correlation"
    elif(determination**2 >= 0.33 and determination**2 <= 0.66):
        gof = "Moderate Correlation"
    else:
        gof = "Strong Correlation"
    return(slope, intercept, determination, gof)

print("Discrepancies: ")
print(highlightData(data))
print(highlightData(data2))
print(highlightData(data3))
print(highlightData(data4))
print("Linear Regression: ")
print(regressData(data))
print(regressData(data2))
print(regressData(data3))
print(regressData(data4))
graphData(data)
graphData(data2)
graphData(data3)
graphData(data4)
        
