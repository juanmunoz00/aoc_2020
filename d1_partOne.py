##Open file
#File
theInputFile = "d01.txt"
needToSum = 2020
inputfilelst = []

f = open(theInputFile, "r")
for x in f:
  ##print(x)
  inputfilelst.append(int(x))

f.close()

def partOne():
  indeX = 0
  nextIndex = 0
  e1Val = 0
  e2Val = 0
  lastElement = len(inputfilelst) - 1
  flagBreak = False

  while( indeX <= lastElement ):
    ##print("indeX: " + str(indeX))
    e1Val = inputfilelst[indeX]
    nextIndex = 1
    while( nextIndex <= lastElement ):
      ##print("indeX: " + str(indeX))
      ##print("nextIndex: " + str(nextIndex))
      
      if( nextIndex == lastElement ): nextIndex = lastElement

      e2Val = inputfilelst[nextIndex]
      
      if( (e1Val + e2Val) == needToSum ):
        print("Found!")
        print(str(e1Val))
        print(str(e2Val))
        print("Result: " + str(e1Val * e2Val))
        flagBreak = True
        break
      else:
        nextIndex += 1

    if( flagBreak ): 
      break
    else:
      indeX += 1
      ##print("*******************")

partOne()