import curses

x = 0
y = 0

prompt = '<<< '

win = curses.initscr()

def win_println(value):
    global y
    win.addstr(y, x, value)
    y += 1

def main():
    # win.keypad(True)
    # win.clear()
    win_println('1')
    win_println('2')
    win_println('3')

    print(y, x)
    # win.move(y+1, x+1)
    # print(y, x)
    win.getch()
    # win = curses.initscr()  # create the curses screen
    # win.keypad(True)  # enable the keypad
    # win.clear()  # clear the screen
    # win.addstr(1, 5, ':)')  # add a smiley face at 1 down, 5 right
    # win.addstr(5, 1, '&:O->-<')  # add a surprised face at 5 down, 1 right
    # win.getkey()  # let the user enter a key
    # curses.endwin()  # close curses

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    # except UnboundLocalError:
    #     print('UnboundLocalError')

    print('\nTraining finished1') 
    curses.endwin()
