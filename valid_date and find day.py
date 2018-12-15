import datetime

inputDate = input("Enter the date in format 'dd/mm/yy' : ")
day,month,year = inputDate.split('/')
isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False
if(isValidDate) :
   
    d=int(day)
    m=int(month)
    y=int(year)

    dayofweek = datetime.date(y, m, d).strftime("%A")
    x = datetime.date(y, m, d).weekday()
   

    if(x==0):
        print("MONDAY")
    elif(x==1):
        print("TUESDAY")
    elif(x==2):
        print("WEDNESDAY")
    elif(x==3):
        print("THURSDAY")
    elif(x==4):
        print("FRIDAY")
    elif(x==5):
        print("SATURDAY")
    elif(x==6):
        print("SUNDAY")


    

else :
    print ("Input date is not valid..")










