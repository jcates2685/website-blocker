import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    # The current time is between 8AM and 4PM
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            print(content)

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours...")
    time.sleep(5)
