from datetime import date, datetime

print(date.today())
print(datetime.now())
birthday = date(year=1986, month=5, day=12)

print(birthday)
xmas = date(year=2022, month=12, day=25)

day_over = datetime(year=2022, month=1, day=25, hour=20, minute=30, second=0, microsecond=0)
print(day_over)

print(day_over - datetime.now())


def time_left():
    """
    :return: time left in hours and minutes before the day is over at 4:30 PM
    """
    current_time = datetime.now()
    current_day = date.today()
    day_over = datetime(year=current_day.year, month=current_day.month, day=current_day.day, hour=16, minute=30,
                        second=0, microsecond=0)
    time_remaining = day_over - current_time
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds - (hours * 3600))//60
    print(f'{hours} Hours and {minutes} Minutes left')


time_left()


def days_since(a_date):
    """
    returns the number of days that have passed since the given a_date
    """
    # use date.today() to get current date
    # subtract from a_date to get the days passed
    # use .days attribute to get the number of days
    pass

