# The exercises require the code below.

class Time:
    """Represents a time of day."""

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return make_time(hour, minute, second)





# EXERCISE 1
# Ask a chatbot. No code.
# -----------





# EXERCISE 2
# Write a "subtract_time" function that takes two Time objects and returns the interval between them in seconds.
# It is assumed both times are during the same day.
# ------------

def subtract_time(time1, time2):
    sec1 = time_to_int(time1)
    sec2 = time_to_int(time2)
    return sec1 - sec2 # assuming it does not need to be an absolute value

start = make_time(10, 30, 0)
end = make_time(12, 0, 0)
print(subtract_time(end, start))





# EXERCISE 3
# Write an "is_after" function that takes two Time objets and returns if the second time is later in the day than the first.
# -----------

def is_after(time1, time2):
    return time_to_int(time1) > time_to_int(time2)

print(is_after(make_time(3, 2, 1), make_time(3, 2, 0)))
print(is_after(make_time(3, 2, 1), make_time(3, 2, 1)))





# EXERCISE 4
# Write functions for a Date object: make_date, print_date, and is_after, along with a date_to_tuple function.
# -----------

class Date:
    """Represents a year, month, and day."""

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    s = f"{date.year}-{date.month:02d}-{date.day:02d}"
    print(s)

def date_to_tuple(date):
    return (date.year, date.month, date.day)

def is_after(date1, date2):
    return date_to_tuple(date1) > date_to_tuple(date2)

date1 = make_date(1933, 6, 22)
print_date(date1)

date2 = make_date(1933, 9, 17)
print(is_after(date2, date1))
