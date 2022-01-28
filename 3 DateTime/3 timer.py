from datetime import datetime

input('Hit Enter to START the timer:\t')
start_time = datetime.now()
print(start_time)

input('Hit Enter to STOP the timer:\t')
end_time = datetime.now()
print(end_time)

time_diff = end_time - start_time
print(f'Time passed = {time_diff.seconds} seconds')
