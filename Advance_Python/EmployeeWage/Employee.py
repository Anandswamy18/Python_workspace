import random

def display_welcome_message():
    print("Welcome to Employee Wage Computation Program")

def check_attendance():
   
    return random.choice([0, 1, 2])

def calculate_daily_wage(attendance):
    wage_per_hour = 20
    full_day_hours = 8
    part_time_hours = 4

    if attendance == 0:
        return 0  
    elif attendance == 1:
        return wage_per_hour * full_day_hours  
    elif attendance == 2:
        return wage_per_hour * part_time_hours  

def calculate_monthly_wage(max_days=20, max_hours=100):
    total_days = 0
    total_hours = 0
    total_wage = 0

    while total_days < max_days and total_hours < max_hours:
        attendance = check_attendance()
        daily_wage = calculate_daily_wage(attendance)
        total_wage += daily_wage
        total_days += 1
        total_hours += 8 if attendance == 1 else 4  
        print(f"Day {total_days}: Daily Wage: Rs {daily_wage}")

    print(f"\nTotal Monthly Wage: Rs {total_wage}")
    print(f"Total Days Worked: Rs {total_days}")
    print(f"Total Hours Worked: Rs {total_hours}")


display_welcome_message()
calculate_monthly_wage(max_days=20, max_hours=100)

