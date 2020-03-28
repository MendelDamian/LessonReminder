from datetime import datetime

log_file = 'logs.txt'


def logs(lesson_date, group):
    with open(log_file, 'r') as f:
        for line in f:
            log_date, log_group = line.split()
            if datetime.strptime(log_date, '%Y-%m-%d').date() == lesson_date and log_group == group:
                return False
    return True


def write_log(lesson_date, group):
    with open(log_file, 'a') as f:
        f.write(f'{lesson_date} {group}\n')
