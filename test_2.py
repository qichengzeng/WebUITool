#encoding=gbk
import os


def copy(src, target):
    dirs = os.listdir(src)
    for dir in dirs:
        if os.path.isdir(os.path.join(src, dir)):
            tar = os.path.join(target, dir)
            os.mkdir(tar)
            copy(os.path.join(src, dir), tar)

        else:
            with open(os.path.join(src, dir)) as f:
                text = f.read()
                with open(target, "w") as w:
                    w.write(text)


copy(r"C:\Users\18273\Desktop\test", r"C:\Users\18273\Desktop\test_1")