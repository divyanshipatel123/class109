import random
import statistics
import plotly.figure_factory as ff

diceResult=[]
for i in range(0,1000):
    dice = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice + dice2)
#print(diceResult)
mean = sum(diceResult)/len(diceResult)
sd = statistics.stdev(diceResult)
print(mean , sd)
mode = statistics.mode(diceResult)
median = statistics.median(diceResult)
print(mode , median)

fig = ff.create_distplot([diceResult], ["Dice results"] , show_hist=False)
fig.show()
#taking sigma 1 or the first standard deviation
Fsdstart, firstsdend = mean - sd , mean + sd
Ssdatart , Ssdend = mean - (2*sd) , mean + (2*sd)
thirdSDstart , thirdSDend = mean - (3*sd), mean + (3*sd)
listOfdataInOneSD = [result for result in diceResult if result > Fsdstart and result < firstsdend] 
listofDataInSecondSD = [result for result in diceResult if result > Ssdatart and result < Ssdend] 
listofDatainThirdSD = [result for result in diceResult if result > thirdSDstart and result < thirdSDend] 
print("{}% of the data lies in the first standard deviation".format(len(listOfdataInOneSD)*100/len(diceResult)) )
print("{}% of the data lies in the second standard deviation".format(len(listofDataInSecondSD)*100/len(diceResult)) )
print("{}% of the data lies in the third standard deviation".format(len(listofDatainThirdSD)*100/len(diceResult)) )