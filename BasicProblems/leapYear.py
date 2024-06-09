def is_leap_year(year):
   
    if year < 1000 or year > 9999:
        print("Year must be a 4-digit number.")
        return
    
   
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")


year = int(input("Enter a 4-digit year: "))
is_leap_year(year)
1