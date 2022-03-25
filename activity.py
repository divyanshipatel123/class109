import statistics
import csv 
import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv("height-weight.csv")
heightList = df["Height(Inches)"].tolist()
weightList = df["Weight(Pounds)"].tolist()
#height
mean = statistics.mean(heightList)
median = statistics.median(heightList)
mode = statistics.mode(heightList)
sd = statistics.stdev(heightList)
#weight
mean2 = statistics.mean(weightList)
median2 = statistics.median(weightList)
mode2 = statistics.mode(weightList)
sd2 = statistics.stdev(weightList)
print(mean , median , mode , sd)
print(mean2 , median2 , mode2 , sd2)

#taking the standard deviations for height
Fsdstart, firstsdend = mean - sd , mean + sd
Ssdatart , Ssdend = mean - (2*sd) , mean + (2*sd)
thirdSDstart , thirdSDend = mean - (3*sd), mean + (3*sd)
listOfdataInOneSD = [result for result in heightList if result > Fsdstart and result < firstsdend] 
listofDataInSecondSD = [result for result in heightList if result > Ssdatart and result < Ssdend] 
listofDatainThirdSD = [result for result in heightList if result > thirdSDstart and result < thirdSDend] 
print("{}% of the data lies in the first standard deviation".format(len(listOfdataInOneSD)*100/len(heightList)) )
print("{}% of the data lies in the second standard deviation".format(len(listofDataInSecondSD)*100/len(heightList)) )
print("{}% of the data lies in the third standard deviation".format(len(listofDatainThirdSD)*100/len(heightList)) )

#taking the standard deviations for weight
FsdstartWeight, firstsdendWeight = mean2 - sd2 , mean2 + sd2
SsdatartWeight , SsdendWeight = mean2 - (2*sd2) , mean2 + (2*sd2)
thirdSDstartWeight , thirdSDendWeight = mean2 - (3*sd2), mean2 + (3*sd2)
listOfdataInOneSDWeight = [result for result in weightList if result > FsdstartWeight and result < firstsdendWeight] 
listofDataInSecondSDWeight = [result for result in weightList if result > SsdatartWeight and result < SsdendWeight] 
listofDatainThirdSDWeight = [result for result in weightList if result > thirdSDstartWeight and result < thirdSDendWeight] 
print("{}% of the data lies in the first standard deviation fot the weight".format(len(listOfdataInOneSDWeight)*100/len(weightList)) )
print("{}% of the data lies in the second standard deviation for the weight".format(len(listofDataInSecondSDWeight)*100/len(weightList)) )
print("{}% of the data lies in the third standard deviation for the weight".format(len(listofDatainThirdSDWeight)*100/len(weightList)) )

# plotting graph
fig = ff.create_distplot([weightList] , ["Weight of the population"])
fig2 = ff.create_distplot([heightList] , ["Height of the population"])
fig.show()
fig2.show()
