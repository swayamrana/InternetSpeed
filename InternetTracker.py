import speedtest
from time import sleep

user = speedtest.Speedtest()

num = int(input('''
Select the statistic you want to learn about your WiFi:
1) Download Speed
2) Upload Speed
3) Ping
Choice: '''))

if num < 1 or num > 3:
    sleep(1)
    print('Invalid choice. Please try again.')
else:

    sleep(1)
    print()
    print('Internet test in progress...')
    print()

    download = round(user.download()/1000000, 3)
    upload = round(user.upload()/1000000, 3)
    user.get_servers([])
    ping = user.results.ping

    if num == 1:
        print('Download Speed: ', download, 'Mbps')
    elif num == 2:
        print('Download Speed: ', upload, 'Mbps')
    elif num == 3:
        print('Ping: ', ping, 'ms')
    
