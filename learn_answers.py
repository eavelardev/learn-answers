import argparse
import json
import curses

x = y = 0

def main():
    parser = argparse.ArgumentParser(description='Learn answers.')

    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r'),
                        help='Input file.')

    args = parser.parse_args()
    f = args.file
    data = json.load(f)
    f.close()
    win = curses.initscr()
    nlines, ncols = win.getmaxyx()

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
            win.addstr(question['question'] + '\n', curses.A_BOLD)
            answer = question['answer']
            answer_words = question['answer'].split()

            in_word, state = get_word()

            if state == '\n':
                if len(in_word) > 0:
                    continue
                else:
                    break

            correct = None
            restart_question = False
            total_chrs = 0
            last_x = 0

            for i in range(len(answer_words)):
                if in_word != answer_words[i]:
                    win.addstr('\n')
                    while True:
                        if correct is None:
                            for j in range(len(answer_words)):
                                if j == i:
                                    win.addstr(
                                        answer_words[j], curses.A_STANDOUT)
                                else:
                                    win.addstr(
                                        answer_words[j], curses.A_UNDERLINE)

                                if j != len(answer_words) - 1:
                                    win.addstr(' ', curses.A_UNDERLINE)

                            win.addstr('\n')
                            correct = False
                        else:
                            win.addstr(' ' * (total_chrs % ncols))
                            win.addstr(
                                answer_words[i] + '\n', curses.A_STANDOUT)

                        win.addstr(answer[total_chrs - last_x: total_chrs])

                        last_y, last_x = win.getyx()
                        if last_y > nlines - 3:
                            restart_question = True
                            break

                        in_word, state = get_word()
                        if state == '\n':
                            restart_question = True
                            break

                        if in_word == answer_words[i]:
                            break
                        else:
                            win.addstr('\n')

                total_chrs += len(answer_words[i])
                if i < len(answer_words) - 1:
                    total_chrs += 1

                if correct is None and i == len(answer_words) - 1:
                    correct = True
                    break

                if i == len(answer_words) - 1 or restart_question:
                    break

                last_y, last_x = win.getyx()
                if last_y > nlines - 3:
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
