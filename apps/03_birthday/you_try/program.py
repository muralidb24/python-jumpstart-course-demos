import datetime

print("-------------------------------------")
print("           Birthday app")
print("-------------------------------------")

year = input("What year were you born in ? ")
month = input("What month were you born in ? ")
day  = input ("What date were you born in ? ")


birthdate = datetime.date(int(year),int(month),int(day))
currentbirthdate = datetime.date(2018, int(month), int(day))
currentdate = datetime.date.today()
delta =  currentdate - currentbirthdate
if (delta.days < 0) :
    days = abs(delta.days)
    print ("Your birthday is coming up in {} days".format(days))
elif (delta.days == 0) :
    print ("It IS your birthday! Happy Birthday to you!!")
else :
    print ("You had your birthday {} days ago. Hope you had fun".format(delta.days))
