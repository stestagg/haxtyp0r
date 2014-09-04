
import os
import sys
import random
location = os.listdir("source")
myfile = random.sample(location, 1)[0]

with open("source/"+myfile) as thefile:
	content = thefile.read()

progress = 0
	 
def send_keystroke(tempo):
	global progress
	sys.stdout.write(content[progress:progress+tempo])
	sys.stdout.flush()
	progress = progress + tempo

def main():
	while True:
		raw_input()
		send_keystroke(random.randint(1, 10))


if __name__ == '__main__':
	main()