import random

def display_welcome_message():
    print("Welcome to Employee Wage Computation ")
def check_attendance():
    
    return random.choice([0, 1])

def calculate_daily_wage():
    wage_per_hour = 20
    full_day_hours = 8

    attendance = check_attendance()
    if attendance == 1:
        daily_wage = wage_per_hour * full_day_hours
        print(f"Employee is Present. Daily Wage: Rs:=> {daily_wage}")
    else:
        print("Employee is Absent. No Wage Earned.")


display_welcome_message()
calculate_daily_wage()

