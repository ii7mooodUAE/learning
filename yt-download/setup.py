import subprocess, os, requests


with open('get-pip.py', 'wb+') as fp:
    fp.write(requests.get('https://bootstrap.pypa.io/get-pip.py').content)

subprocess.run(['python',
                'get-pip.py'])

subprocess.run(['pip',
                'install',
                '-r',
                'requirements.txt'])

os.remove('get-pip.py')
os.remove('requirements.txt')
os.system('cls')

input('You can now delete setup.py, press any button to continue')
