def CheckLeap(Year):
  #Checking if the given year is leap year
  if((year % 400 == 0) or
    (year % 100 != 0) and
    (year % 4 ==0)):
    print("Given year is not a leap year");
    #Else it is not a leap year
  else:)
    print("Given Year is not a leap year")
    #Taking an input year from user
    Year = int(input("Enter the number:"))
    #printing result
    CheckLeap(Year)