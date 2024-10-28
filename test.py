import datetime

def get_start_date():
    while True:
        try:
            date_str = input("Enter start date (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return start_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

start_date = get_start_date()
print("Start date:", start_date)