x=int(input("How do you want to generate your band name?\n1) Based on favorite book\n2) Based on favorite song\n3)Based on favorite city\nEnter option below:"))
if(x==1):    
    book=input("Enter favorite book:")
    time=input("Enter favorite time of day:")
    print(time+" of "+book)
elif(x==2):    
    song=input("Enter favorite song:")
    stationary=input("Enter favorite stationary:")
    print(stationary+" by "+song)
elif(x==3):    
    city=input("Enter favorite city:")    
    food=input("Enter favorite food:")
    print(food+" in "+city)
else:
    print("Invalid option, please run again")

