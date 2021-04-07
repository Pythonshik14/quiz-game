from commands import *
from GUIVoicer import *
import getpass
import os


def add_to_startup(file_path=""):
    USER_NAME = getpass.getuser()
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)



say_message("Привет дорогой друг, поздравляю с успешной установкой моей программы!")



if __name__ == '__main__':

    while True:
        func_()
        command = listen_command()
        do_this_command(command)

        if command in ("пока", "алибидерчи", "до скорого"):
            say_message(random.choice(["алибидерчи...", "гудбай", "пока-пока"]))
            exit()


add_to_startup(r"C:\Users\user\PycharmProjects\My_game_platform2D\asis.exe")