from readkey import getch
from inter import send_keystroke


def demo1(DEBUG):
    keygen = getch(0.1)
    charge = 0
    inc = 0.1
    while 1:
        the_input = keygen.next()
        if the_input:
            # print the_input
            charge = inc + (1 - inc) * charge
            tempo = int(charge  *100)
            if DEBUG:
                print tempo * 'X'
            send_keystroke(tempo)
        else:
            charge = (1 - inc) * charge

if __name__ == '__main__':
    demo1(DEBUG=False)
