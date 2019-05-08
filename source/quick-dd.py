#!/usr/bin/env python

import subprocess
from pathlib import Path


subprocess.run(['lsblk'])

def qddStart():
    selectTarget()

def selectTarget():
    global targetDisk
    global targetPath
    targetDisk = input('What is the target disk?\n-> ')
    targetPath = Path('/dev/' + str(targetDisk))
    if targetDisk == 'q':
        targetDisk = None
        exit()
    targetCheck()

def targetCheck():
    if targetPath.exists():
        print(str(targetPath) + ' is selected')
        selectPool()
    else:
        print('/dev/' + targetDisk + ' does not exist, please specify an existing disk')
        selectTarget()

def poolSelected():
    imageTargetCheck()
    ddRun()

def selectPool():
    global pool
    pool = input('From which pool do you wish to select an image?\n-> ')
    if pool == 'os':
        print('/mnt/sdb1/OS is selected')
        subprocess.run(['ls', '/mnt/sdb1/OS'])
    elif pool == 'down':
        print('~/Downloads is selected')
        homeFolder = str(Path.home())
        subprocess.run(['ls', homeFolder + '/Downloads'])
    elif pool == 'q':
        selectTarget()
    else:
        print(pool + ' is not a known pool')
        selectPool()
    poolSelected()

def imageTargetCheck():
    global image
    image = input('Which image do you wish to flash?\n-> ')
    if image == 'q':
        selectPool()

def ddRun():
    print('Flashing ' + image + ' to '  + str(targetPath) + '...')
    if pool == 'os':
        subprocess.run(['sudo', 'dd', 'if=/mnt/sdb1/OS/' + image, 'of=' + str(targetPath)])
    elif pool == 'down':
        subprocess.run(['sudo', 'dd', 'if=' + homeFolder + '/Downloads' + image, 'of=' + str(targetPath)])
    print('Flash finished successfully')

qddStart()
