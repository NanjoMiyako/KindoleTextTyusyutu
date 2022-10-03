## function searchBluePerson
##スクリーンショットをとって指定の矩形から青の矩形領域を取得する


import pyautogui as gui
import sys

print('中断するにはCrt+Cを入力してください。')

try:
    print(sys.exec_prefix)
    while True:
       x=input("取得したい箇所にカーソルを当てEnterキー押してください\n")
       print(gui.position())

       
except KeyboardInterrupt:
    print('\n終了')
    sys.exit()