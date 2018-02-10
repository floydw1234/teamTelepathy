from TwoPictureDisplay import Window
import time


def thing():
	temp_time = time.time()

	while(time.time() - temp_time < 10):
		time.sleep(1)	
		print "asdf"
	exit()

app = Window("black.jpg","smeadly.jpg",thing)


# above is the usage of the TwoPictureDisplay class is above




