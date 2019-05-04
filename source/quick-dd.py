import subprocess


subprocess.run(['lsblk'])

target = input('What is the target disk? ')
print('/dev/' + target + ' is selected')


def selectPool():
    global pool
    pool = input('From which pool do you wish to select an image? ')
    if pool == 'os':
        print('/mnt/sdb1/OS is selected')
        print('------------------------------------------------------')
        subprocess.run(['ls', '/mnt/sdb1/OS'])
    elif pool == 'down':
        print('~/Downloads is selected')
        print('------------------------------------------------------')
        subprocess.run(['ls', '/home/dennis/Downloads'])
    else:
        print(pool + ' is not a known pool')
        selectPool()

selectPool()

image = input('Which image do you wish to flash? ')

def ddRun():
    if pool == 'os':
        subprocess.run(['sudo', 'dd', 'if=/mnt/sdb1/OS/' + image, 'of=/dev/' + target])
    elif pool == 'down':
        subprocess.run(['sudo', 'dd', 'if=/home/dennis/Downloads/' + image, 'of=/dev/' + target])

ddRun()
