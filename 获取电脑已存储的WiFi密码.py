
import locale
import subprocess
import re

loc_lang = locale.getdefaultlocale()

if loc_lang[0] == "zh_CN":
    re_pattern = [
        "所有用户配置文件 : (.*)\r",
        "安全密钥               : 不存在\r",
        "关键内容            : (.*)\r"
    ]
else:
    re_pattern = [
        "All User Profile : (.*)\r",
        "Security key           : Absent\r",
        "Key Content            : (.*)\r"
    ]

cmd_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode(loc_lang[1], errors="ignore")
wifi_names = re.findall(re_pattern[0], cmd_output)
wifi_list = []
if len(wifi_names) != 0:
    for wifi in wifi_names:
        wifi_info = {}
        wifi_info["ssid"] = wifi
        cmd_wifi_info = subprocess.run(["netsh", "wlan", "show", "profiles", wifi, "key=clear"],
                                       capture_output=True).stdout.decode(loc_lang[1], errors="ignore")
        if re.search(re_pattern[1], cmd_wifi_info):
            wifi_info["password"] = None
        else:
            password = re.findall(re_pattern[2], cmd_wifi_info)
            if password == []:
                wifi_info["password"] = None
            else:
                wifi_info["password"] = password[0]
        wifi_list.append(wifi_info)

for i in range(len(wifi_list)):
    print(wifi_list[i])