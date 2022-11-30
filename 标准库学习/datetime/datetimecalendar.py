import time, datetime, calendar

# print(time.time())
# print(time.localtime())
# ct = time.time()
# lt = time.localtime()
# print(time.ctime(ct))
# print(time.asctime(lt))
#
# slt = time.strftime('%Y-%m-%d  %B  ==%I=== %p %H:%M:%S', lt)
# print(slt)
#
# # clt = time.strptime(slt, '%Y-%m-%d %H:%M:%S' )
# # print(clt)
#
# print(time.mktime(lt))
#
# # print(calendar.month(2022, 3)
# print(datetime.date.today())
#
# print(type(meet))
# history = datetime.datetime.now() - meet
# print(str(history))
# print(meet.strftime('%y--%m--%d'))
#
# print(datetime.datetime.now()-datetime.timedelta(seconds=50000000))
while True:
    # print(datetime.datetime.now())
    meet = datetime.datetime(2020,4,6,18,0,0)
    # print(datetime.datetime.now() - meet)
    history= datetime.datetime.now() - meet
    print(history.seconds)
    hours = history.seconds//3600
    minutes = history.seconds//60
    second = history.seconds%60
    print(hours,minutes,second)
    time.sleep(1)