import threading
import time

def countdown(interval, name):
	for x in xrange(10, 0, -1):
		print("Thread " + name + ": " + str(x) + "\n")
		time.sleep(interval)


t1 = threading.Thread(target = countdown, args = (1, "t1"))
t2 = threading.Thread(target = countdown, args = (2, "t2"))

t1.start()
t2.start()