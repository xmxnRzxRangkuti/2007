
import os, platform
os.system("rm -rf 2007")
os.system('git pull')
os.system("git clone https://github.com/C4LLM3D3V1L/2007")
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from old import menu
    menu()
elif bit == '32bit':
    from old import menu
    menu()
