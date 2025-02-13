from datetime import datetime

def format_date(dateSTR):
    date_obj = datetime.strptime(dateSTR, "%m/%d/%Y")
    formatted_date = date_obj.strftime("%B %d, %Y")
    return formatted_date

dateInput = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", format_date(dateInput))