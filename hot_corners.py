import sys
import time
import subprocess

delay = 0.2
toggle_plank = 'python3 toggle_plank.py'
show_workspaces = 'dbus-send --session --dest=org.pantheon.gala --print-reply /org/pantheon/gala org.pantheon.gala.PerformAction int32:1'

TLcommand = ''
TRcommand = ''
BLcommand = toggle_plank
BRcommand = show_workspaces

def getPos():
    position = subprocess.check_output('xdotool getmouselocation --shell',shell=True).splitlines()
    for line in position:
        if line.startswith('X='):
            posx = int(line.strip('X='))
        elif line.startswith('Y='):
            posy = int(line.strip('Y='))
    position = [posx,posy]
    return position

position = getPos()
time.sleep(delay)

xrandr = subprocess.check_output("xrandr | fgrep '*'",shell=True).split('x')
hor = int(xrandr[0].strip(' '))
ver = int(xrandr[1].split(' ')[0])

if position == getPos():
    if position[0] > hor/2:
        if position[1] > ver/2:
            subprocess.call(BRcommand,shell=True)
        else:
            subprocess.call(TRcommand,shell=True)
    else:
        if position[1] > ver/2:
            subprocess.call(BLcommand,shell=True)
        else:
            subprocess.call(TLcommand,shell=True)
