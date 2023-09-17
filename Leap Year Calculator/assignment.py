def CheckLeapYear(Year):  

  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("{} is a leap Year".format(Year));  
  else:  
    print ("{} is not a leap Year".format(Year))  
 
Year = int(input("Enter the number: "))  
 
CheckLeapYear(Year)  