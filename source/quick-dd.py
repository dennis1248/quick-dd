#!/usr/bin/env python

import subprocess
from pathlib import Path


subprocess.run(['lsblk'])

def selectTarget():
    global targetDisk
    global targetPath
    targetDisk = input('What is the target disk? ')
    targetPath = Path('/dev/' + str(targetDisk))
    targetCheck()

def targetCheck():
    if targetPath.exists():
        print(str(targetPath) + ' is selected')
    else:
        print('/dev/' + str(targetDisk) + ' does not exist, please specify an existing disk')
        selectTarget()

def selectPool():
    global pool
    pool = input('From which pool do you wish to select an image? ')
    if pool == 'os':
        print('/mnt/sdb1/OS is selected')
        subprocess.run(['ls', '/mnt/sdb1/OS'])
    elif pool == 'down':
        print('~/Downloads is selected')
        subprocess.run(['ls', '/home/dennis/Downloads'])
    else:
        print(pool + ' is not a known pool')
        selectPool()

def imageTargetCheck():
    global image
    image = input('Which image do you wish to flash? ')

def ddRun():
    if pool == 'os':
        subprocess.run(['sudo', 'dd', 'if=/mnt/sdb1/OS/' + str(image), 'of=' + str(targetPath)])
    elif pool == 'down':
        subprocess.run(['sudo', 'dd', 'if=/home/dennis/Downloads/' + str(image), 'of=' + str(targetPath)])

selectTarget()
targetCheck()
selectPool()
imageTargetCheck()
ddRun()
