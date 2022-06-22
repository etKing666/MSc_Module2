def increment(time, seconds):
    time.second += seconds

    add_minute = int(time.second / 60)
    time.second = time.second % 60
    time.minute += add_minute

    add_hour = int(time.minute / 60)
    time.minute = time.minute % 60
    time.hour += add_hour
    