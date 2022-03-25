# print("This is a program to evaluate a leap or not a leap year")
# year=int(input("Enter a year\n"))

#check wheather the year is divisible by 4
def is_a_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True # print(f"{year}:  a leap year")
            else:
                return False # print("This is not a leap year")
        else:
            return True # print("leap year")
    else:
        return False # print("That is not a leap year, thanks try another year one")

def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_a_leap_year(year) and month==2:
        return 29
    return month_days[month-1]

year=int(input("Enter a year"))
month=int(input("Enter a month"))
days=days_in_month(year,month)
print(days)