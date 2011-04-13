# http://projecteuler.net/index.php?section=problems&id=19

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_per_month_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

known_day = 1 # 1 Jan 1900 was a Monday
day = 1 + 365 % 7 # Tuesday, 1 January 1901
sundays = 0
months = days_per_month
for year in range(1901,2001):
    months = days_per_month_leap_year if year % 4 == 0 and year % 400 != 0 else days_per_month
    for month in range(12):
        if day == 0:
            sundays += 1
        day =  (day + months[month]) % 7

print sundays
