
import os
import sys
import random
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter

from pygments.lexers import guess_lexer, guess_lexer_for_filename

formatted = None
progress = 0

def load_random_file():
	global formatted, progress

	files = os.listdir("source")
	myfile = random.sample(files, 1)[0]
	with open("source/"+myfile) as thefile:
		content = thefile.read()

	lexer = guess_lexer_for_filename(myfile, content)
	formatted = highlight(content,lexer,Terminal256Formatter())
	progress = 0

load_random_file()
	 
def send_keystroke(tempo):
	global progress
	if tempo == 0:
		return
	next_chars = formatted[progress:progress+tempo]
	if len(next_chars) == 0:
		# end of file reached
		load_random_file()
		return send_keystroke(tempo)

	sys.stdout.write(next_chars)
	sys.stdout.flush()
	progress = progress + tempo

def main():
	while True:
		raw_input()
		send_keystroke(random.randint(1, 10))


if __name__ == '__main__':
	main()