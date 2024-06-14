import random

def display_welcome_message():
    print("Welcome to Employee Wage Computation Program")

def check_attendance():
    
    return random.choice([0, 1, 2])

def calculate_daily_wage(attendance):
    wage_per_hour = 20
    full_day_hours = 8
    part_time_hours = 4

    switch = {
        0: lambda: print("Employee is Absent. No Wage Earned."),
        1: lambda: print(f"Employee is Full-time Present. Daily Wage: Rs {wage_per_hour * full_day_hours}"),
        2: lambda: print(f"Employee is Part-time Present. Daily Wage: Rs {wage_per_hour * part_time_hours}")
    }

    
    switch.get(attendance, lambda: None)()


display_welcome_message()
attendance = check_attendance()
calculate_daily_wage(attendance)
