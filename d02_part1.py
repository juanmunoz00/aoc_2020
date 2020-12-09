theInputFile = "d02.txt"
sliceMinOcurr = 0
sliceMaxOcurr = 2
sliceLetterOcurr = 4
sliceStartOfPwd = 7
howManyValidPasswords = 0
minOcurr = 0
maxOcurr = 0

flgPrintTestText = False
flagOverrideForTest = False

def GetMinAndMaxOccur(passWord):
  """
  ##One or two digits?
  2-4 p: vpkpp
  6-16 b: bbbbbbbbbbbbbbbpb
  16-18 h: vhhhhhhhhhhhhphhrnh
  8-10 h: vphrhhmhhz
  """
  if( flagOverrideForTest ):
    ##override for test
    passWord = "1-8 d: vhhhhhhhhhhhhphhrnh"
    print(passWord)
  
  ##Assert case
  n1 = passWord[0:2]
  if( n1.isdigit() ):
    ##Case 1 or 2
    if( flgPrintTestText ): print(n1 + " is digit")
    m1 = passWord[3:5]
    if( m1.isdigit() ):
      ##Case 1
      if( flgPrintTestText ): print(m1 + " is digit")
      #n1 = passWord[3:4]
      sliceLetterOcurr = 6
    else:
      m1 = passWord[3]
      if( m1.isdigit() ):
        ##Case 2
        if( flgPrintTestText ): print(m1 + " is digit")
        sliceLetterOcurr = 5
      else:
        if( flgPrintTestText ): print(m1 + " IS NOT digit")
  else:
    if( flgPrintTestText ): print(n1 + " IS NOT digit")
    n1 = passWord[0:1]
    ##Assert
    if( n1.isdigit() ):
      ##Case 3 or 4
      if( flgPrintTestText ): print(n1 + " is digit")
      m1 = passWord[2:4]
      if( m1.isdigit() ):
        ##Case 4
        if( flgPrintTestText ): print(m1 + " is digit")
        sliceLetterOcurr = 5
      else:
        if( flgPrintTestText ): print(m1 + " IS NOT digit")
        m1 = passWord[2]
        if( m1.isdigit() ):
          ##Case 3
          if( flgPrintTestText ): print(m1 + " is digit")
          sliceLetterOcurr = 4
        else:
          if( flgPrintTestText ): print(m1 + " IS NOT digit")        
  
  """
  if( flgPrintTestText ): 
    print(str(minOcurr))
    print(str(maxOcurr))
    print("letter: " + passWord[sliceLetterOcurr])
  """

  return n1, m1, sliceLetterOcurr

def IsAValidPassword(minOcurr, maxOcurr, letterOcurr, passWord):
  flgValid = False

  if(flgPrintTestText): print("----------------")
  if(flgPrintTestText): print("minOcurr: " + str(minOcurr))
  if(flgPrintTestText): print("maxOcurr: " + str(maxOcurr))
  if(flgPrintTestText): print("letterOcurr: " + str(letterOcurr))

  countOccur = int(passWord.count(letterOcurr)) - 1
  if(flgPrintTestText): print("countOccur: " + str(countOccur))
  if( (countOccur >= minOcurr) and (countOccur <= maxOcurr) ): flgValid = True
  
  if(flgPrintTestText): print("----------------")

  return flgValid

f = open(theInputFile, "r")
for x in f:  
  ##Init
  letterOcurr = 0
  startOfPwd = 0

  print(x)
  minOcurr, maxOcurr, sliceLetterOcurr = GetMinAndMaxOccur(x) 
  ##Taking into account the specification of the letter (letterOcurr)
  letterOcurr = x[sliceLetterOcurr]
  """
  if( flgPrintTestText ): 
    print(str(minOcurr))
    print(str(maxOcurr))
    print(str(letterOcurr))
  """

  if( IsAValidPassword(int(minOcurr), int(maxOcurr), letterOcurr, x) ): 
    howManyValidPasswords += 1
    if(flgPrintTestText): print("Valid Password")  

  if(flgPrintTestText): 
    y = input("Press any key")
    print("Valid Passwords: " + str(howManyValidPasswords))
    print("############")

print("Amount of valid passwords: " + str(howManyValidPasswords))

f.close()