import curses 
from curses import wrapper
import time
import random
def startscreen(stdscr):
    stdscr.erase()
    stdscr.addstr("Welcome to the typing speed test!\nPress any key to continue")
    stdscr.getkey()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(2,0,f"WPM: {wpm}")
    for i, char in enumerate(current):
        correct_char = target[i]
        if char==correct_char:
            stdscr.addstr(0,i,char,curses.color_pair(1))
        else:
            stdscr.addstr(0,i,correct_char,curses.color_pair(2))



def load_text():
    with open("text.txt","r") as t:
        lines = t.readlines()
        return random.choice(lines).strip()

def wpm(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    stdscr.nodelay(True)
    while True:
        if current_text==[]:
            start_time = time.time()

        time_elasped = max(time.time() - start_time, 1)
        wpm = round((len(current_text)/(time_elasped/60))/5)
        stdscr.erase()
        display_text(stdscr,target_text,current_text,wpm)
        try:
            k = stdscr.getkey()
        except:
            continue
        try:
            if ord(k) == 27:
                stdscr.nodelay(False)
                break
            if ord(k) == 8:
                if len(current_text) > 0:
                    current_text.pop()
            elif len(current_text) >= len(target_text):
                stdscr.erase()
                stdscr.nodelay(False)
                stdscr.addstr(0,0,"You are finished")
                stdscr.addstr(1,0,f"You WPM was: {wpm}")
                stdscr.getkey()
                break

            else:
                current_text.append(k)
        except:
            continue


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    while True:
        startscreen(stdscr)
        wpm(stdscr)
        stdscr.erase()
        stdscr.addstr("If you want to test again press any key or press ESC to exit the program:")
        try:
            k = stdscr.getkey()
            if ord(k)==27:
                break
        except:
            continue        
   
wrapper(main)

