class Class: 
          
     def sumOfNumbers(self, signal):
          print(sum(array[signal]))


     def meanOfNumbers(self, signal):
          print(statistics.mean(array[signal]))

     def time(self, times, startTime, endTime, dataPoints):
          return list(map(lambda t: (round((t-startTime)/(endTime - startTime))*dataPoints), times))

     def pairs(self, listOfTimes):
          return list(zip(listOfTimes, listOfTimes[1:]))

     def sumWithTimes(self, signal, pairsList):
          print([sum(array[signal][start:end]) for start, end in pairsList])

     def meanWithTimes(self, signal, pairsList):
          print([statistics.mean(array[signal][start:end]) for start, end in pairsList])




stats = Class()

sumTest = stats.sumOfNumbers(3)
meanTest = stats.meanOfNumbers(5)
timeTest = stats.time([-0.5, 0.0, 3.0, 4.6, 5.5], -0.5, 10.5, 2200)
pairTest = stats.pairs(timeTest)
sumWithTimeTest = stats.sumWithTimes(2, pairTest)
meanmWithTimesTest = stats.meanWithTimes(2, pairTest)