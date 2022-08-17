year1 = int(input("Which year you were born? "))
year2 = int(input("Provide the current year: "))
if year1 == year2:
    month1 = int(input("Provide the month you were born(in number): "))
    month2 = int(input("Provide the current month(in number): "))
    if month1 == month2:
        day1 = int(input("Provide the day you were born in that month: "))
        day2 = int(input("Provide current day of this month: "))
        if day1 > day2:
            print("You haven't born yet")
        elif day1 == day2:
            print("you're born today")
        else:
            age = int(day2 - day1)
            print("You just born ",age," days ago")
    if month1 < month2:
        print("You're born ", month2 - month1 , " month ago")
    else:
        print("You haven't born yet")
elif year1 < year2 and year2 - year1 <= 99:
    month1 = int(input("Provide the month you were born(in number): "))
    month2 = int(input("Provide the current month(in number): "))
    if month1 == month2:
        day1 = int(input("Provide the day you were born in that month: "))
        day2 = int(input("Provide current day of this month: "))
        if day1 == day2:
            age = int(year2 - year1)
            print(" congratulations you are "+str(age)+ "years old today")
        elif day1 < day2:
            if day2 - day1 :
                print("you are ",year2 - (year1+1),"but you will be ", year2 - year1 ," in few days" )
            else:
                print("you are ",year2 - (year1+1),"but you will be ", year2 - year1 ," in few weeks" )
        else:
            print("you are ", year2 - year1 , " years old ")
    elif month1 > month2:
        print("you are ", year2 - (year1+1)," years old")
    else:
        print("you are", year2 - year1," years old")
elif year1 < year2 and 99 < year2 - year1 <= 119 :
    print("you are ", year2 - year1, " years old, hmmm really???")
elif year1 < year2 and 120 <= year2 - year1 <= 150:
            print("bruh you are ", year2 - year1, " years old, you broke the guinness world record")
elif year1 < year2 and year2 - year1 > 150:
    print("Are you even Human, you are ",year2 - year1," years old,")
else:
    print("You haven't born yet")        
