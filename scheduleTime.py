#每天早上8點半播放鬧鐘

import schedule
import time
import pygame 

def job():
    pygame.mixer.init()
    pygame.mixer.music.load("./起來現在也才3點.mp3")
    pygame.mixer.music.play()

    time.sleep(5)
    print("Time's up! Time to wake up!")

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("08:00").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":40").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)