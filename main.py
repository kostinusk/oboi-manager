from datetime import datetime
import ctypes
import time
import os
import winsound

SPI_SETDESKWALLPAPER = 20
SPI_GETDESKWALLPAPER2 = 0x0073
MAX_PATH = 260

def GetCurrentOboi():
    path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER2, MAX_PATH, path, 0)
    return str(path.value)

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


folder_path = 'I:\\projects\\oboi project\\math lore\\'
files = os.listdir(folder_path)
print(type(files[1]))
N_of_files = len(files)

while True:
    now = datetime.now()
    minutes = (now.minute + now.hour*60) % (60 * 24 // 5)
    print(f"{minutes} {now.hour} {now.minute}")
    k = int(N_of_files * minutes / (60 * 24 / 5) // 1)
    print(k)
    if GetCurrentOboi() != folder_path + files[k]:
        set_wallpaper(folder_path+files[k])
#         print('обои поменяны')
#          winsound.Beep(440, 100)
    else:
#         print('пасс')

    time.sleep(60)
