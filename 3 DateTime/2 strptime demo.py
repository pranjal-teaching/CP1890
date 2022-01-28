from datetime import datetime

santa_time = "25/12-21 15:20:47"
format_string = "%d/%m-%y %H:%M:%S"

my_date = datetime.strptime(santa_time, format_string)
print(f"{my_date:%A, %d %b, %Y %I:%M:%S %p}")

