from datetime import datetime

test_day = '2024-12-31'

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d').date()      
    except ValueError:
        print(f"Format of the date is not correct. Must be YYYY-MM-DD.")
    else:
        today_day = datetime.today().date()
        diff_day = today_day - user_date
        return diff_day.days

request = get_days_from_today(test_day)
if request != None:
    print(request)