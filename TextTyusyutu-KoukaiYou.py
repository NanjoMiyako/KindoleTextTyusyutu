import pyautogui as gui
import time
import pyperclip

#(x, y)
kindle_UpCenter = [1072, 12]
kindle_Center = [1031, 394]
paint_center = [349, 426]
paint_left=[677,397]

paint_RightDown=[585, 720]
paint_LeftUp=[73, 163]

moveUpCount=120
moveLeftCount=70


positionCount = 3



#この間にpaintとkindleをセットする
time.sleep(10)

for idx in range(positionCount):
    gui.click(kindle_UpCenter[0], kindle_UpCenter[1])
    gui.hotkey('alt','printscreen')
    
    gui.click(paint_center[0], paint_center[1])
    gui.hotkey('ctrl', 'v')
    
    for idx2 in range(moveUpCount):
        gui.press('up')
        
    
    for idx3 in range(moveLeftCount):
        gui.press('left')
    
    gui.click(paint_left[0], paint_left[1])
    gui.click(paint_RightDown[0], paint_RightDown[1])
    gui.dragTo(paint_LeftUp[0], paint_LeftUp[1])    
    gui.hotkey('ctrl', 'shift', 'x')
    

    idx2 = idx+1    
    path1 = str(idx2) +".png"
    gui.press('f12')
    gui.write(path1, interval=0.1)
    gui.press('enter')
    
    time.sleep(1.0)
    gui.click(kindle_UpCenter[0], kindle_UpCenter[1])
    time.sleep(1.0)
    gui.click(kindle_Center[0], kindle_Center[1])
    time.sleep(1.0)
    gui.press('pagedown')
    time.sleep(1.0)