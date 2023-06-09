import ctypes
from ctypes import wintypes
import time
import winsound
import threading

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

def play_sound():
    winsound.Beep(666, 4000)
        
while True:
    SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    MessageBox = ctypes.windll.user32.MessageBoxExW
    if not GetSystemPowerStatus(ctypes.pointer(status)):
        raise ctypes.WinError()
    if status.BatteryLifePercent < 30 and status.ACLineStatus == 0:
        threading.Thread(target=play_sound).start()
        MessageBox(None, 'Please Connect Charger!\nBattery is less than 30%', 'Battery Alert - YDRGZM', 0x40000)
    elif status.BatteryLifePercent > 90 and status.ACLineStatus == 1:
        threading.Thread(target=play_sound).start()
        MessageBox(None, 'Please Disconnect Charger!\nBattery is more than 90%', 'Battery Alert - YDRGZM', 0x40000)
    time.sleep(30)