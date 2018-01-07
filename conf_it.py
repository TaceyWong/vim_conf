# coding:utf-8

import os
import shutil




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
        pass
    try:
        os.makedirs(conf_dir)
    except Exception as e:
        print "Mkdir:",e
    return conf_dir


def copy_conf(color_dir,conf_dir):
    color_sc = "molokai.vim"
    color_path = os.path.join(color_dir,color_sc)
    conf_sc = "vimrc"
    conf_path = os.path.join(conf_dir,conf_sc)
    print color_path
    print conf_path
    shutil.copyfile(color_sc,color_path)
    shutil.copyfile(conf_sc,conf_path)



if __name__ == "__main__":
    color_dir = get_color_dir()
    conf_dir = creat_conf_dir()
    copy_conf(color_dir,conf_dir)
