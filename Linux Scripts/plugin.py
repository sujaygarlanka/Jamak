import subprocess
import time


print ("Searching for phone...")
while True:
    devices = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True).stdout
    devices = devices.splitlines()
    if len(devices[1]) > 0:
        print ("Device Found: ", devices[1].split()[0])
        break
    else:
        time.sleep(.500)
        continue

print("\n")

app = subprocess.run(["adb", "shell", "pm", "list", "packages", "|", "grep", "com.example.jamakapp"], stdout=subprocess.PIPE, text=True).stdout

if len(app) == 0:
    print("App not found. Downloading Jamak app...")
    out = subprocess.run(["adb", "install", "app-debug.apk"], stdout=subprocess.PIPE, text=True).stdout
    print(out)
else:
    print("App found")
print("\nOpening app")
openApp = subprocess.run(["adb", "shell", "am", "start", "-n", "com.example.jamakapp/com.example.jamakapp.MainActivity"], stdout=subprocess.PIPE, text=True).stdout
print(openApp)


#date = "2021-01-18 22:33:59.197"
#Wed Jan 20 21:48:35 EST 2021
currDate = subprocess.run(["adb", "logcat","-d","-v","tag,time,year", "-t", "1"], stdout=subprocess.PIPE, text=True).stdout
print (currDate)
currDate = currDate.splitlines()[1].split()

# print (currDate[0])
# print (currDate[1])
date = currDate[0] + " " + currDate[1]


print("Searching...")
while True:
    #print("*****")
    get_logs = subprocess.run(["adb", "logcat", "-d", "-v", "tag,time,year", "-t", date, "JamakApp:D", "*:S"], stdout=subprocess.PIPE, text=True).stdout

    #print("log " + get_logs + " " + date)
    time.sleep(.500)
    indexLogs = get_logs.splitlines()
    #print (len(indexLogs))
    if len(indexLogs) > 1:
        # print("beg")
        if indexLogs[-1][0] == '-':
            continue
        else:
            # print(indexLogs[-1][0])
            # print(indexLogs)
            action = indexLogs[-1].split()[-1]
            newDate = indexLogs[-1]
            newDate = newDate.split()
            #print(newDate)
            date = newDate[0] + " " + newDate[1]
            date = date[:-3] + str(int(date[-3:]) + 1)

            if action == "format":
                print("format")
                subprocess.run(["adb", "shell", "wm", "density", "180"], stdout=subprocess.PIPE, text=True).stdout
                subprocess.run(["adb", "shell", "wm", "size", "1280x800"], stdout=subprocess.PIPE, text=True).stdout
                subprocess.run(["adb", "shell", "content", "insert", "--uri","content://settings/system","--bind","name:s:user_rotation", "--bind value:i:1"], stdout=subprocess.PIPE, text=True).stdout
                subprocess.run(["adb", "shell", "content", "insert", "--uri","content://settings/system","--bind","name:s:accelerometer_rotation", "--bind value:i:0"], stdout=subprocess.PIPE, text=True).stdout

            if action == "unformat":
                print("unformat")
                subprocess.run(["adb", "shell", "wm", "density", "reset"], stdout=subprocess.PIPE, text=True).stdout
                subprocess.run(["adb", "shell", "wm", "size", "reset"], stdout=subprocess.PIPE, text=True).stdout
                subprocess.run(["adb", "shell", "content", "insert", "--uri","content://settings/system","--bind","name:s:accelerometer_rotation", "--bind value:i:1"], stdout=subprocess.PIPE, text=True).stdout


#
# while True:
#     get_logs = subprocess.run(["adb", "logcat", "-d", "-v", "tag,time,year", "-t", date, "JamakApp:D", "*:S"], stdout=subprocess.PIPE, text=True).stdout
#     last_log = get_logs.splitlines()[-1]
#     index = last_log.find("D/JamakApp")
#     if (index > -1):
#         date = last_log[0:index-1]
#         # increase timestamp by 1 millisecond
#         next_millisecond = int(date[-3:]) + 1
#         # if
#         print(date[-3:])
#         print(str(next_millisecond))
#         # date[-3:] = str(next_millisecond)
#     if "unformat" in last_log:
#         print("unformat")
#     elif "format" in last_log:
#         print("format")
