from pynput.keyboard import HotKey, Key, KeyCode, Listener
import pyperclip
counter = 0

isWork = False
lastThing = pyperclip.paste()


def pasting():
    global counter
    if isWork:
        counter += 1
        pyperclip.copy("\nprint(\"Here I'm: " + str(counter) + "\")")


def reseting():
    global counter
    if isWork:
        counter = 0
        pyperclip.copy("\nprint(\"Here I'm: " + str(counter) + "\")")


def turnOnOff():
    global isWork
    reseting()
    if isWork:
        isWork = False
        pyperclip.copy(lastThing)
    else:
        isWork = True
        pyperclip.copy("\nprint(\"Here I'm: " + str(counter) + "\")")


hotkey1 = HotKey(
    [Key.ctrl, KeyCode(char='v')],
    pasting
)

hotkey2 = HotKey(
    [Key.ctrl, KeyCode(char='r')],
    reseting
)

hotkey3 = HotKey(
    [Key.ctrl, KeyCode(char='t')],
    turnOnOff
)

hotkeys = [hotkey1, hotkey2, hotkey3]


def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()

##########################
# Done in Febr 13th
# Paulo Emil
# busy.paulo@hotmail.com
##########################
