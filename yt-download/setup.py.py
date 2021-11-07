from time import sleep
from os import remove
from sys import argv
from subprocess import run

run(['python', 'get-pip.py'])
print('Pip installed...')

fp = open('requirements.txt', 'w+')
fp.write('pytube==11.0.1\neyed3==0.9.6')
fp.close()
print('Generated requirements....')

run(['pip', 'install', '-r', 'requirements.txt'])
run(['cls'])
print('Downloaded and Installed necessary modules...')

remove('get-pip.py')
remove('requirements.txt')
remove('readme.txt')

input("Setup completed, press enter to end.")

remove(argv[0])
