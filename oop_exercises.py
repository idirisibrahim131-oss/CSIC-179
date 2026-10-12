# Exercise 1: CountingStack

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        value = super().pop()
        self.__counter += 1
        return value


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print("Exercise 1:", stk.get_counter())


# Exercise 2a: Queue

class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if not self.__queue:
            raise QueueError
        return self.__queue.pop()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)

print("Exercise 2a:")
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")


# Exercise 2b: SuperQueue
# This subclass checks whether the queue is empty by safely trying to
# access the queue's private list through a helper method added to Queue.

class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

print("Exercise 2b:")
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")


# Exercise 3: Timer

def format_time(hours, minutes, seconds):
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return format_time(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        self.__seconds += 1

        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1

        if self.__minutes == 60:
            self.__minutes = 0
            self.__hours += 1

        if self.__hours == 24:
            self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1

        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1

        if self.__minutes < 0:
            self.__minutes = 59
            self.__hours -= 1

        if self.__hours < 0:
            self.__hours = 23


timer = Timer(23, 59, 59)
print("Exercise 3:")
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)


# Exercise 4: Weeker

class WeekDayError(Exception):
    pass


class Weeker:
    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError
        self.__day = Weeker.__days.index(day)

    def __str__(self):
        return Weeker.__days[self.__day]

    def add_days(self, n):
        self.__day = (self.__day + n) % 7

    def subtract_days(self, n):
        self.__day = (self.__day - n) % 7


print("Exercise 4:")
try:
    weekday = Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker("Monday")
except WeekDayError:
    print("Sorry, I can't serve your request.")
