# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import pyautogui
import pygetwindow as pw
import win32gui # part of pywin32
import win32ui  # part of pywin32
import win32con # part of pywin32
from ctypes import windll
import numpy as np
import cv2 # prt of opencv-python
from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    win = pw.getAllTitles()
    print(win)
    #ica = 'ICA - Google Chrome'
    #my = pw.getWindowsWithTitle(ica)
    #print(my)
    #my.activate()
    #p = pyautogui.screenshot(imageFilename="test.png")
    # im = pyautogui.screenshot(region=(0, 0, 300, 400))


def background_screenshot(hwnd, width, height):
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (0, 0), win32con.SRCCOPY)

    result = windll.user32.PrintWindow(hwnd, cDC.GetSafeHdc(), 2)
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    #bmInfo = dataBitMap.GetInfo()
    #im = np.frombuffer(dataBitMap.GetBitmapBits(True), dtype=np.uint8)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    #return im # return PIL image object
    return cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR) # return cv2 image object

if __name__ == '__main__':
    #print_hi('PyCharm')
    wName = 'ICA - Google Chrome'
    #wName = 'python - Convert image from PIL to openCV format - Stack Overflow - Google Chrome'
    hwnd = win32gui.FindWindow(None, wName)
    img = background_screenshot(hwnd, 1280, 780)
    #cvImg = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('name', img)
    cv2.waitKey(0)
    #cv2.imwrite('screen.png', img)