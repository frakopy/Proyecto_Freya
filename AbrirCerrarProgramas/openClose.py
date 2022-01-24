import os, time,webbrowser
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

programas = [
        r'D:\Soporte_Core_CA\Piedras.txt',
        r'D:\Soporte_Core_CA\Comandos para Alarmas.txt',
        r'D:\Soporte_Core_CA\COMANDOS_APG40 Y LINUX APG43L.txt',
        r'D:\Soporte_Core_CA\Comandos-Huawei.txt',
        r'D:\Soporte_Core_CA\Comandos-STP-Oracle.txt',
        r'D:\Soporte_Core_CA\MOSHELL_Comandos operacionales.txt',
        r'D:\A_PYTHON\Documentacion_Python\Apuntes_Python.txt',
        r'D:\Soporte_Core_CA\CCN\CCN_Comandos_Alarmas.txt',
        r'D:\Soporte_Core_CA',
        r'D:\A_PYTHON\ProgramasPython',
        r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE',
        r'C:\Program Files (x86)\Ericsson\Element Management\WinFIOL\winfiol.exe',
        r'D:\Soporte_Core_CA\ACCESO NODOS CORE\IPBase_Millicom_Tlf_2020.xls',
        r'D:\Soporte_Core_CA\PENDIENTES_SOPORTE CORE C.A.xlsx'
        ]


total_programas = len(programas)
ejecutor = ThreadPoolExecutor(max_workers = total_programas)
futuros= []


def open_programs():

    for programa in programas:
        try:
            futuros.append(ejecutor.submit(os.startfile, programa))
        except:
            print(f'No pude abir el archivo ubicado en: {programa}')
    
    #A continuacion se abren las paginas web que uso diario en el explorador, para esto se utilizo el modulo
    #webbrowser el cual forma parte de la libreria estandar de python
    url2 = 'https://web.whatsapp.com/'
    ejecutor.submit(webbrowser.open, url2, new=0, autoraise=True)

    for futuro in concurrent.futures.as_completed(futuros):
        print(f'Archivo {programa} abierto con éxito!!!')


def close_programs():

    cmd_cerrarPrograma = [
    'taskkill /IM notepad.exe',
    'taskkill /IM winfiol.exe',
    'taskkill /IM EXCEL.EXE',
    'taskkill /IM OUTLOOK.EXE',
    'taskkill /IM firefox.exe',
    'taskkill /IM explorer.exe',
    'taskkill /IM brave.exe',
    # 'taskkill /F /IM Code.exe'
    ]

    for cmd in cmd_cerrarPrograma:
        try:
            futuros.append(ejecutor.submit(os.system, cmd))
        except Exception as e:
            print('No se puedo finalizar el proceso ---->', cmd ,'por el siguiente motivo:\n' )
            print(e)
    
    for futuro in concurrent.futures.as_completed(futuros):
        print(f'Comando {cmd} ejecutado con éxito!!!')

