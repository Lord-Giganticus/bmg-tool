import os
import time

if os.getcwd() != os.path.dirname(__file__):
    os.chdir(os.path.dirname(__file__))

try:
    os.system('cmd /c wbmgt.exe -h > test.txt')
    os.remove('test.txt')
except:
    print("wbmgt not found. Exiting.")
    time.sleep(2)
    exit()

encoding  = int(input("Enter the number corresponding to your choice.\n[1]Encode\n[2]Decode\n"))

if encoding == 1:
    txt_files = []
    txt_names = []
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True:
            if file.endswith('.txt') == True:
                file = os.path.basename(file)
                txt_files.append(file)
                file = os.path.splitext(file)
                file = file[0]
                txt_names.append(file)
    print(txt_files[:])
    file_choice = int(input("Enter the EXACT number corresponding to the file you want to use (starts at 0):\n"))
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True:
            if file.endswith('.bmg') == True:
                bmg_file = file
                file = os.path.basename(file)
                file = os.path.splitext(file)
                file = file[0]
                if file == txt_names[file_choice]:
                    os.remove(bmg_file)
    os.system('wbmgt.exe ENC "'+txt_files[file_choice]+'"')
    print("Complete. Exiting.")
    time.sleep(5)
    exit()
elif encoding == 2:
    bmg_files = []
    bmg_names = []
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True:
            if file.endswith('.bmg') == True:
                file = os.path.basename(file)
                bmg_files.append(file)
                file = os.path.splitext(file)
                file = file[0]
                bmg_names.append(file)
    print(bmg_files[:])
    file_choice = int(input("Enter the EXACT number corresponding to the file you want to use (starts at 0):\n"))
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True:
            if file.endswith('.txt') == True:
                txt_file = file
                file = os.path.basename(file)
                file = os.path.splitext(file)
                file = file[0]
                if file == bmg_names[file_choice]:
                    os.remove(txt_file)
    os.system('wbmgt.exe DEC "'+bmg_files[file_choice]+'"')
    print("Complete. Exiting.")
    time.sleep(5)
    exit()
else:
    print("Inproper choice. Exiting.")
    time.sleep(2)
    exit()