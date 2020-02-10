import argparse
import json
import curses

x = y = 0

def main():
    parser = argparse.ArgumentParser(description='Learn answers.')

    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r'),
                        help='Input file.')

    clo = '>>> '
    cli = '<<< '
    info = '--> '
    args = parser.parse_args()
    f = args.file
    data = json.load(f)
    f.close()
    curses.initscr()
    win = curses.initscr()

    def win_print(value):
        global x, y
        win.addstr(y, x, value)
        x += len(value)

    def win_println(value):
        win_print(value)
        global x, y
        x = 0
        y += 1

    def get_word():
        word = ''
        while True:
            ch = win.getkey()
            if ch == ' ' or ch == '\n':
                return word, ch
            if ch.isprintable():
                word += ch

    for question in data:
        while True:
            win.clear()
            global x, y
            x = y = 0
            win_println(clo + question['question'])
            answer = question['answer']
            answer_words = question['answer'].split()

            win_println(cli) 
            in_word, state = get_word()

            if state == '\n':
                if len(in_word) > 0:
                    continue
                else:
                    break

            correct = None
            restart_question = False
            for i in range(len(answer_words)):

                if in_word != answer_words[i]:
                    while True:
                        if correct is None:
                            win_println(info + answer)
                            win_println(info + 'Practice more!')
                            correct = False
                        else:
                            win_print(info) 
                            for j in range(i):
                                x += len(answer_words[j]) + 1
                            win_println(answer_words[i])

                        win_print(cli) 

                        for j in range(i):
                            win_print(answer_words[j] + ' ')
                        win_println('')
                        
                        in_word, state = get_word()

                        if state == '\n':
                            restart_question = True
                            break

                        if in_word == answer_words[i]:
                            break

                if correct is None and i == len(answer_words) - 1:
                    correct = True
                    break

                if restart_question:
                    break

                in_word, state = get_word()

                if state == '\n' and i < len(answer_words) - 2:
                    break

            if correct:
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

    print('\nTraining finished') 
    curses.endwin()
