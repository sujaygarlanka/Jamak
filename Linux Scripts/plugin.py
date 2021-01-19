import subprocess

date = "2021-01-18 22:33:59.197"
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