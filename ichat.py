import sys, urllib, urllib.request, json
from aip import AipOcr
from PIL import ImageGrab
import cv2
import win32clipboard as w
import xiaoiceapi
import time
import pyperclip #python实现复制粘贴
from pykeyboard import *
from pymouse import *
from pyperclip import *


xb = xiaoiceapi.xiaoiceApi()
#print(xb.chat("你爸爸是谁")['text'])

APP_ID = "23523493"
API_KEY = "zdC65GmCaXwQxYVm6aMCYWzq"
SECRET_KEY = "v8WoiMU0kxEmsiqmxzzZ7PniTZ8dOlBY"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def scrope(pic_path):
    image = get_file_content(pic_path)
    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    print("正在识别图片信息......")
    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    result=client.basicGeneral(image, options)
    src=result['words_result']
    #print(len(src))
    dicfile=open('file.txt','a+',encoding='utf-8')
    word = str()
    for key in range(len(src)):
        dicfile.write(src[key]['words'])
        dicfile.write('\n')
        word = word+src[key]['words']
        #print(src[key]['words'])
    print(word)
    dicfile.close()
    return word

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def setText(text="English testing, 中文测试"):
	# set clipboard data
	w.OpenClipboard()
	w.EmptyClipboard()
	w.SetClipboardText(text)
	w.CloseClipboard()

def getText():

	# get clipboard data
	w.OpenClipboard()
	data = w.GetClipboardData()
	w.CloseClipboard()
	return data

while True:
    im = ImageGrab.grab((488, 484, 1035, 535))
    # im.show()
    im.save("H:/python/ichat/123.jpg")





    data = scrope('H:/python/ichat/123.jpg')
    reply = "[fake·陈子文]:"+ xb.chat(data)['text']
    print(reply)
    setText(text=reply)
    #print(data)
    m = PyMouse()
    m.click(484,450)
    k = PyKeyboard()
    # 模拟键盘点击ctrl+v
    reply = str(reply)

    k.press_key(k.control_key);time.sleep(0.2);  # 按下control键
    k.tap_key('v');time.sleep(0.2);  # 点击enter键
    k.release_key(k.control_key)  # 松开control键
    #pyperclip.paste()
    k.tap_key(k.enter_key)



    time.sleep(30)






'''
#data = "你好"
data = urllib.request.quote(data)
url = 'http://api.tianapi.com/txapi/robot/index?key=f25d0c84026a861183f9ca431c3cf1bd&question=%s'%(data)
print(url)
req = urllib.request.Request(url)

resp = urllib.request.urlopen(req)
#print(resp)
content = resp.read().decode().split("\"")
if(content):
    reply = "[autoreply]:"+content[11]
    print(reply)
    setText(text=reply)
'''