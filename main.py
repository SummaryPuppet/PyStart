import pyautogui
import time

win = "win"
shift = "shift"
enter = "enter"

def change_window(screen_num = ""):
    pyautogui.hotkey(win, screen_num)

def create_window():
    pyautogui.hotkey(win, enter)

def write_terminal(text = ""):
    pyautogui.write(text)
    pyautogui.press(enter)

def wait():
    time.sleep(4)

def create_terminal(window = "", command = ""):
    change_window(window)
    create_window()
    wait()
    write_terminal(command + " " + "code")

def main ():
    pyautogui.press("numlock")

    create_terminal("1", "cd")

    create_terminal("3", "ranger")

    create_terminal("3", "cd")

    change_window("2")
    pyautogui.hotkey(win, "f")

if __name__ == '__main__':
    main()
