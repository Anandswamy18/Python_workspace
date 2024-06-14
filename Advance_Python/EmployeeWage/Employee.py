import random

def display_welcome_message():
    print("Welcome to Employee Wage Computation Program ")

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

def calculate_monthly_wage():
    total_working_days = 20
    total_wage = 0

    for day in range(1, total_working_days + 1):
        attendance = check_attendance()
        daily_wage = calculate_daily_wage(attendance)
        total_wage += daily_wage
        print(f"Day {day}: Daily Wage: Rs {daily_wage}")

    print(f"\nTotal Monthly Wage: Rs{total_wage}")


display_welcome_message()
calculate_monthly_wage()

