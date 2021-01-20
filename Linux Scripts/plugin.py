import subprocess
import time

date = "2021-01-18 22:33:59.197"

#result = subprocess.run([sys.executable, "-c", "print('ocean')"])
# while True:

#com.example.jamakapp/com.example.jamakapp.MainActivity

#adb shell am start -n com.example.jamakapp/com.example.jamakapp.MainActivity


# result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True).stdout
# result = result.splitlines()
# print(result[1])
# print(len(result[1]))
#adb install app-debug.apk

while True:
    devices = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True).stdout
    devices = devices.splitlines()
    if len(devices[1]) > 0:
        print ("Device Found: ", devices[1].split()[0])
        break
    else:
        print ("Searching...")
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

while True:
    get_logs = subprocess.run(["adb", "logcat", "-d", "-v", "tag,time,year", "-t", date, "JamakApp:D", "*:S"], stdout=subprocess.PIPE, text=True).stdout
    last_log = get_logs.splitlines()[-1]
    index = last_log.find("D/JamakApp")
    if (index > -1):
        date = last_log[0:index-1]
        # increase timestamp by 1 millisecond
        next_millisecond = int(date[-3:]) + 1
        # if
        print(date[-3:])
        print(str(next_millisecond))
        # date[-3:] = str(next_millisecond)
    if "unformat" in last_log:
        print("unformat")
    elif "format" in last_log:
        print("format")
