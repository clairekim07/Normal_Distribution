import csv
import random
import statistics
import plotly.figure_factory as ff
result = []

for total in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)


#using statitics module to calculate the mean and stdev for result
mean = sum(result)/len(result)
print("Mean: "+str(mean))

sd = statistics.stdev(result)
print("Standard Deviation: "+str(mean))

median = statistics.median(result)
print("Median: "+str(median))

mode = statistics.mode(result)
print("Mode: "+str(mode))

#finding the range
#stdevStart is -1 and stdevEnd is +1
firstStdevStart, firstStdevEnd = mean-sd,mean+sd

secondStdevStart, secondStdevEnd = mean-(2*sd),mean+(2*sd)

thirdStdevStart, thirdStdevEnd = mean-(3*sd),mean+(3*sd)
#calculating the datapoint's distance falling between the standard deviations

#this is the length of the -2sd to 2sd
number = 0
for i in range(0,len(result)):
    if result[i] >= secondStdevStart and result[i]<=secondStdevEnd:
        number += 1
    
print("Total amount of dice from -2sd to 2sd is: " + str(number))
'''
dataFallingInFirstSd

print(format(len(dataFallingInFirstSd)*100.0/len(result)))

dataFallingInSecondSd

print(format(len(dataFallingInSecondSd)*100.0/len(result)))
'''
nCurve = ff.create_distplot([result],["result"], show_hist=False)
nCurve.show()






