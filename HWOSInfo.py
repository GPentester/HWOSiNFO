#HWOSINFO WAS MADED BY GPentester#2561. Please give credits if you use a line of code.


import platform
import subprocess
import ctypes
import os
import psutil
import winreg
# Obtener la información del sistema operativo
uname = platform.uname()
print(f"Sistema operativo: {uname.system}")
print(f"Versión: {uname.release}")
print(f"Build: {uname.version}")
print(f"Arquitectura: {uname.machine}")

#Obtener OS info
os.system("systeminfo")
def save_log(HWOSInfo):
    with open('hwosinfo.log', 'a') as log_file:
        log_file.write(f'HWOSINFO GENERADA: {HWOSInfo}\n')


# Obtener información de la GPU
try:
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    hdc = user32.GetDC(None)
    h = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
    v = ctypes.windll.gdi32.GetDeviceCaps(hdc, 12)
    user32.ReleaseDC(None, hdc)
    print(f"Resolución de pantalla: {width}x{height}")
    print(f"Tamaño de pantalla: {h}x{v} mm")

    

    display_reg_path = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}"
    displays = []
    try:
        for subkey_name in winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, display_reg_path):
            if subkey_name.isnumeric():
                subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, display_reg_path + "\\" + subkey_name)
                try:
                    displays.append((winreg.QueryValueEx(subkey, "DriverDesc")[0],
                                      winreg.QueryValueEx(subkey, "DriverVersion")[0],
                                      winreg.QueryValueEx(subkey, "MonitorManufacturer")[0]))
                except:
                    pass
                winreg.CloseKey(subkey)
    except:
        pass

    for i, display in enumerate(displays):
        print(f"GPU {i+1}: {display[0]}")
        print(f"Versión del controlador: {display[1]}")
        print(f"Fabricante del monitor: {display[2]}")
        
except:
    print("No se pudo encontrar información de la GPU")

#RAM INFO
ram = psutil.virtual_memory()
print("Memoria total: ", ram.total)
print("Memoria disponible: ", ram.available)
print("Porcentaje de memoria utilizada: ", ram.percent)

#CPU Info
print("Procesador: ", platform.processor())