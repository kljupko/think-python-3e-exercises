# EXERCISE 1
# Ask a chatbot some questions.
# Have it rewrite the following function as a method of the Time class.

def subtract_time(t1, t2):
    return time_to_int(t1) - time_to_int(t2)

# ------------

def subtract(self, other):
    return self.time_to_int() - other.time_to_int()





# EXERCISE 2
# Rewrite the Date class from the previous chapter to use methods.
# -----------

class Date:
    """Represents a year, month, and day."""

    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        s = f"{self.year}-{self.month:02d}-{self.day:02d}"
        return s
    
    def to_tuple(self):
        return (self.year, self.month, self.day)

    def is_after(self, other):
        return self.to_tuple() > other.to_tuple()

d1 = Date(1933, 6, 22)
print(d1)

d2 = Date(1933, 9, 17)
print(d2.is_after(d1))
