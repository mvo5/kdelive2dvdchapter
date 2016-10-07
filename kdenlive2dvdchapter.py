#!/usr/bin/python3

import os
import re
import sys
import locale


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '') 
    
    if len(sys.argv) < 1:
        print("need kdenlive file as first argument")
        os.exit(1)

    sec2title = {}
    with open(sys.argv[1]) as fp:
        for line in fp:
            m = re.search(r'<property name\="kdenlive\:guide\.([0-9.,]+)">(.*)</property>', line)
            if not m:
                continue
            sec = locale.atof(m.group(1))
            title = m.group(2)
            sec2title[sec] = title

    fps=25
    print('<chapters ftp="%s">' % fps)
    print(' <chapter title="Start" time="0" />')
    for sec in sorted(sec2title):
        title = sec2title[sec]
        frame = int(sec * fps)
        print(' <chapter title="%s" time="%s" />' % (title, frame))
    print('</chapters>')
