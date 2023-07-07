def sumOfNumbers(signal):
     print(sum(array[signal]))


def meanOfNumbers(signal):
     print(statistics.mean(array[signal]))

def time(times):
     listOfAlteredTimes = (list(map(lambda t: (round((t+0.5)*200)), times)))
     return listOfAlteredTimes

def pairs(listOfTimes):
     try:
          listOfPairs = list(zip(listOfTimes, listOfTimes[1:]))  
     except:
          for i in range(0, len(listOfPairs)):
               if listOfPairs[i][0] > listOfPairs[i][1]:
                    listOfPairs[i] = list(listOfPairs[i])
                    listOfPairs[i] = tuple(sorted(listOfPairs[i]))
     return listOfPairs
       

def sumOfNumbersTimeN(signal, times):
     alteredTimes = time(times)
     pairsList = pairs(alteredTimes)
     sums = [sum(array[signal][start:end]) for start, end in pairsList]
     print(sums)

def meanOfNumbersTimeN(signal, times):
     alteredTimes = time(times)
     pairsList = pairs(alteredTimes)
     sums = [statistics.mean(array[signal][start:end]) for start, end in pairsList]
     print(sums)