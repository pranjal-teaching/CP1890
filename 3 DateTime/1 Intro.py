# from datetime import date, datetime, time, timedelta
#
# print(date.today())
# print(datetime.now())
# birthday = date(year=1986, month=5, day=12)
#
# noon = time(hour=12,minute=0,second=0)
# print(noon)
#
# print(birthday)
# xmas = date(year=2022, month=12, day=25)
#
# day_over = datetime(year=2021, month=2, day=10)
# print(day_over)
#
# print(day_over - datetime.now())  # -352 days, 10:16:08.811060
#
#
# def time_left():
#     """
#     :return: time left in hours and minutes before the day is over at 4:30 PM
#     """
#     current_time = datetime.now()
#     current_day = date.today()
#     day_over = datetime(year=current_day.year, month=current_day.month, day=current_day.day, hour=16, minute=30,
#                         second=0, microsecond=0)
#     time_remaining = day_over - current_time
#     hours = time_remaining.seconds // 3600
#     minutes = (time_remaining.seconds - (hours * 3600)) // 60
#     print(f'{hours} Hours and {minutes} Minutes left')
#
#
# time_left()
#
#
# def days_since(a_date: datetime):
#     """
#     returns the number of days that have passed since the given a_date
#     """
#     # use date.today() to get current date
#     # subtract from a_date to get the days passed
#     # use .days attribute to get the number of days
#     current_date = date.today()
#     difference = a_date - current_date
#     return difference.days
#
#
# xmas = date(year=2022, month=12, day=25)
# print(days_since(xmas))


from datetime import date, datetime, time, timedelta

cur_date = date.today()
bday = date(year=2022, month=1, day=1)
random_time = time(hour=12, minute=34, second=56)

time_alive = cur_date - bday
print(time_alive.days)
