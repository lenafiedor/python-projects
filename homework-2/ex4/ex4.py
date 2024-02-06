import sys
from datetime import datetime

def get_days_difference(first_date, second_date):
    date_format = "%d-%m-%Y"
    date1 = datetime.strptime(first_date, date_format)
    date2 = datetime.strptime(second_date, date_format)

    difference = date2 - date1
    return difference.days


if __name__ == '__main__':
    args = sys.argv
    try:
        diff = get_days_difference(args[1], args[2])
        print(f'Difference between given dates: {diff} days')
    except IndexError:
        print('Usage: python3 ex4.py <DD-MM-YYYY> <DD-MM-YYYY')
