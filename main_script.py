from bs4 import BeautifulSoup
import requests
import os

def cmdline():
    with open('/home/pi/jojo/Raspberry-pi-linux-update/linux-cmd.txt', 'r' , encoding='utf-8') as txtfile:
        cmd_ls = txtfile.read().split(';')
    return cmd_ls

res = requests.get('https://pythonk122.blogspot.com/2019/07/blog-post_17.html').content
soup = BeautifulSoup(res, 'html.parser')
signal = soup.find("div", attrs={"class": "post-body entry-content float-container"}).text.strip()

if signal == '0':
    # python系統更新 ##
    os.system('cd /home/pi/jojo')
    os.system('git clone https://github.com/jeff3388/Raspberry-pi-python-system-update.git')
    os.system('pip install -r /home/pi/jojo/Raspberry-pi-python-system-update/requirements.txt')

elif signal == '1':
    ## Linux 系統更新 ##
    os.system('cd /home/pi/jojo')
    os.system('git clone https://github.com/jeff3388/Raspberry-pi-linux-update.git')
    cmd_ls = cmdline()
    
    for cmd in cmd_ls:
        os.system(cmd)

elif signal == '2':
    ## python主程式更新 ## 
    os.system('cd /home/pi/jojo')
    os.system('git clone https://github.com/jeff3388/Raspberry-pi-python-main.git')

elif signal == '3':
    ## 執行主程式 ##
    os.system('python3 /home/pi/jojo/Raspberry-pi-python-main/main.py')
