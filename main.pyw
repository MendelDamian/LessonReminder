from vulcan import Vulcan
from LessonReminder.login import login
from LessonReminder.register import register
from LessonReminder.message import message
from LessonReminder.log import logs, write_log
import vulcan
from datetime import datetime
from time import sleep

MW = 2743
class_ = {
        'JA1': ('@pupil1', '@pupil2'),
        'JA2': ('@pupil1', '@pupil2')
         }

while True:
    try:
        client = login()
    except FileNotFoundError:
        register()
        client = login()

    for lesson in client.get_lessons():
        if lesson.teacher.login_id == MW:
            lesson_date = lesson.date
            start_time = lesson.time.from_
            end_time = lesson.time.to
            group = lesson.group
            time = datetime.now().time()
            date = datetime.now().date()
            text = ' '.join(class_[group])
            text += ' lekcja angielskiego'
            send = logs(lesson_date, group)

            if time > start_time and time < end_time and date == lesson_date and send:
                write_log(lesson_date, group)
                message(text)

    sleep(60)
            