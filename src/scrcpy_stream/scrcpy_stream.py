import cv2
import numpy as np
import subprocess
from ppadb.client import Client
import io
import os


MAXFRAMERATE = 2
SCRCPY_PATH = '"C:/Users/Martin/Desktop/Python Projects/scrcpy/scrcpy.exe"'
DEVICE_INDEX = 0

def run_scrcpy():
    return subprocess.Popen(SCRCPY_PATH, stdout=subprocess.PIPE)

def connect_adb():
    adb = Client(host='127.0.0.1',port=5037)
    devices = adb.devices()
    if len(devices) == 0:
        print("No Devices Attached")
        return None
    return devices[DEVICE_INDEX]

def getScreenshot(device):
    res = device.screencap()
    res = io.BytesIO(res)
    file_bytes = np.asarray(bytearray(res.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return img

def check_alive(p, device):
    poll = p.poll()
    if poll is None:
        p.kill()
    if device is None:
        p.kill()
        quit()

def show_img(img):
    cv2.imshow("derp", img)
    if cv2.waitKey(int(1000/MAXFRAMERATE)) & 0xFF == ord('q'):
        return False
    return True

if __name__ == "__main__":
    p = run_scrcpy()
    device = connect_adb()
    while True:
        check_alive(p, device)
        img = getScreenshot(device)
        keep_alive = show_img(img)
        if not keep_alive:
            p.kill()
            quit()
