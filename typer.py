from readkey import getch
from inter import send_keystroke


def demo1():
    keygen = getch(0.1)
    tempo = 0
    inc = 0.1
    while 1:
        the_input = keygen.next()
        if the_input:
            # print the_input
            tempo = inc + (1 - inc) * tempo
            print int(tempo*100) * 'X'
        else:
            tempo = (1 - inc) * tempo

if __name__ == '__main__':
    demo1()
