import time
from playsound import playsound


def gettime():
    users_time = input('Введите время для таймера в формате "часы:минуты:секунды": ')
    hour_min_sec = list(map(int, users_time.split(':')))
    sec = hour_min_sec[0]*3600 + hour_min_sec[1]*60 + hour_min_sec[2] - 3
    return sec


def timer():
    sec = gettime()
    time.sleep(sec)
    playsound('D:/Matrix/z/Timer/Ludwig van Beethoven - Allegretto.mp3')


timer()
