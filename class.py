##### FIRST EXERCISE FOR OOP: COUNTING THE NUMBER OF ITEMS PUSHED AND POPPED IN A STACK
# class Stack:
#     def __init__(self):
#         self.__stk = []
#
#     def push(self, val):
#         self.__stk.append(val)
#
#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__count = 0
#
#     def get_counter(self):
#         return self.__count
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__count += 1
#
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())



# #####  OOP QUEQUE EXERCISE
# class QueueError(IndexError):  # Choose base class for the new exception.
#     def __init__(self):
#         print("Queue Error.")
#
#
# class Queue:
#     def __init__(self):
#         self.__queue = []
#
#     def put(self, elem):
#         self.__queue.insert(0, elem)
#
#     def get(self): ###### YOUR GET METHOD
#         if len(self.__queue) <= 0:
#             raise QueueError
#         else:
#             val = self.__queue[-1]
#             self.__queue.pop()
#             return val
#
#     ###### BETTER GET METHOD
#     # def get(self):
#     #     if len(self.queue) > 0:
#     #         elem = self.queue[-1]
#     #         del self.queue[-1]
#     #         return elem
#     #     else:
#     #         raise QueueError
#
#
# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Queue error")



# ##### SECOND OOP QUEUE EXERCISE
# class QueueError(IndexError):
#     pass
#
#
# class Queue:
#     def __init__(self):
#         self.queue = []
#     def put(self,elem):
#         self.queue.insert(0,elem)
#     def get(self):
#         if len(self.queue) > 0:
#             elem = self.queue[-1]
#             del self.queue[-1]
#             return elem
#         else:
#             raise QueueError
#
#
# class SuperQueue(Queue):
#     def isempty(self):
#         return len(self.queue) == 0
#
#
# que = SuperQueue()
# que.put(1)
# que.put("dog")
# que.put(False)
# for i in range(4):
#     if not que.isempty():
#         print(que.get())
#     else:
#         print("Queue empty")



##### THE TIMER CLASS OOP ACTIVITY
# class Timer:
#     def __init__(self, hour, minute, second):
#         self.__hr = hour
#         self.__min = minute
#         self.__sec = second
#
#     def __str__(self):
#         return str(self.__hr) + ":" + str(self.__min) + ":" + str(self.__sec)
#
#     def next_second(self):
#         self.__sec = int(self.__sec) + 1
#         if (self.__sec == 60):
#             self.__sec = "00"
#             self.__min = int(self.__min) + 1
#
#             if (self.__min == 60):
#                 self.__min = "00"
#                 self.__hr = int(self.__hr) + 1
#
#                 if (self.__hr >= 24):
#                     self.__hr = "00"
#
#     def prev_second(self):
#         self.__sec = int(self.__sec) - 1
#         if (self.__sec == -1):
#             self.__sec = "59"
#             self.__min = int(self.__min) - 1
#
#             if (self.__min == -1):
#                 self.__min = "59"
#                 self.__hr = int(self.__hr) - 1
#
#                 if (self.__hr == -1):
#                     self.__hr = "23"
#
#
# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)



##### THE TIMER OOP ACTIVITY RIGHT ANSWER
# def two_digits(val):
#     s = str(val)
#     if len(s) == 1:
#         s = '0' + s
#     return s
#
#
# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds
#
#     def __str__(self):
#         return two_digits(self.__hours) + ":" + \
#                two_digits(self.__minutes) + ":" + \
#                two_digits(self.__seconds)
#
#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds > 59:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes > 59:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours > 23:
#                     self.__hours = 0
#
#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 0:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes < 0:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours < 0:
#                     self.__hours = 23
#
#
# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)



#####