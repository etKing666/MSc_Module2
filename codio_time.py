class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time1 = 25
time2 = 30

def print_time():
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))
    #print("f{time.hour}:{time.minute}:{time.second}")

def is_after(t1, t2):
# How to do this without using if statement?
    if t1 > t2:
        return True
    else:
        return False

print_time()
is_after(time1, time2)