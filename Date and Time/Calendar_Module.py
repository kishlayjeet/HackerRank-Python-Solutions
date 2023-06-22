import calendar
month, day, year = map(int, input().split())
day_of_week = calendar.day_name[calendar.weekday(year, month, day)]
print(day_of_week.upper())