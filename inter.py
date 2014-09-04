
import os
import sys
import random
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter

from pygments.lexers import guess_lexer, guess_lexer_for_filename

formatted = None
progress = 0
have_matrix = False

def load_random_file(fname= None):
	global formatted, progress

	if fname is None:
		files = os.listdir("source")
		fname = random.sample(files, 1)[0]
	with open("source/"+fname) as thefile:
		content = thefile.read()

	lexer = guess_lexer_for_filename(fname, content)
	formatted = highlight(content,lexer,Terminal256Formatter())
	progress = 0

load_random_file()
	 
def send_keystroke(tempo):
	if tempo == 99 and not have_matrix:
		sys.stdout.write("\n")
		load_random_file("../matrix.txt")
		have_matrix = True
	global progress, have_matrix
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