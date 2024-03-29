def is_leap(check_year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(user_year, user_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] += 1

    return year, month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
n_year, n_month = days_in_month(year, month)
print(n_year)