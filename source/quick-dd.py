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
    imageTarget()
    ddRun()

def selectPool():
    global pool
    global homeFolder
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

def imageTarget():
    global image
    global imagePath
    image = input('Which image do you wish to flash?\n-> ')
    if image == 'q':
        selectPool()
    elif pool == 'os':
        imagePath = '/mnt/sdb1/OS/' + image
    elif pool == down:
        imagePath = homeFolder + '/Downloads/' + image
    imageTargetCheck()

def imageTargetCheck():
    imageTargetFile = Path(imagePath)
    if imageTargetFile.is_file():
        ddRun()
    else:
        print(image + ' does not exist, please select an existing file')
        imageTarget()

def ddRun():
    print('Flashing ' + image + ' to '  + str(targetPath) + '...')
    subprocess.run(['sudo', 'dd', 'if=' + imagePath, 'of=' + str(targetPath)])
    print('Flash finished!')
    exit()

qddStart()
