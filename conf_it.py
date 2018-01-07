# coding:utf-8

import os
import sys
import shutil
import signal

logo_text = """__      ___                  _____             __
\ \    / (_)                / ____|           / _|
 \ \  / / _ _ __ ___ ______| |     ___  _ __ | |_
  \ \/ / | | '_ ` _ \______| |    / _ \| '_ \|  _|
   \  /  | | | | | | |     | |___| (_) | | | | |
    \/   |_|_| |_| |_|      \_____\___/|_| |_|_|  v0.01

"""

def get_color_dir():
    path_template = "/usr/share/vim/vim{version}/colors"
    color_path = ""
    for num in range(71,81):
        color_path = path_template.format(version=str(num))
        is_exist = os.path.exists(color_path)
        if is_exist:
            return color_path
    return None


def creat_conf_dir():
    home_dir =  os.path.expanduser('~')
    conf_dir = os.path.join(home_dir,".vim")
    try:
        shutil.rmtree(conf_dir)
    except Exception as e:
        print e
    try:
        os.makedirs(conf_dir)
    except Exception as e:
        print "Mkdir:",e
        return None
    return conf_dir


def copy_conf(color_dir,conf_dir):
    color_sc = "molokai.vim"
    color_path = os.path.join(color_dir,color_sc)
    conf_sc = "vimrc"
    conf_path = os.path.join(conf_dir,conf_sc)
    print color_path
    print conf_path
    try:
        shutil.copyfile(color_sc,color_path)
        shutil.copyfile(conf_sc,conf_path)
    except Exception as e:
        print e
        sys.exit(3)


def rake():
    print logo_text
    ask = raw_input("This Will Remove all Your Configs for vim\n"
                    "Enter->Continue\n"
                    "Ctr-C->Exit\n:")
    print("-Start-")
    print("-To Get Color Dir")
    color_dir = get_color_dir()
    if not color_dir:
        print("-Sorry,Cannot Find Vim-")
        sys.exit(1)
    print(color_dir)
    print("-To Creat .vim Dir-")
    conf_dir = creat_conf_dir()
    if not conf_dir:
        print("-Sorry,Failed to Create .vim Dir-")
        sys.exit(2)
    copy_conf(color_dir,conf_dir)
    print("-Done-")

def sig_service(func):
    def handle_sig(sig,frame):
        if int(sig) == 2:
            print("Bye Bye!")
            sys.exit(0)
    signal.signal(signal.SIGTERM, handle_sig)
    signal.signal(signal.SIGINT, handle_sig)
    func()

if __name__ == "__main__":
    sig_service(rake)
