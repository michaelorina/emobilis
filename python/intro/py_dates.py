from datetime import date, datetime, timedelta

today = date.today()
dt = datetime.now()
print(today)
print(dt)

formatted_date = today.strftime("%a, %d %B %Y")
print(formatted_date)

ten_days_ago = timedelta(days=10)
print(ten_days_ago)

# "2012-09-01" How to convert a date string to date
# "1999-01-31 "