import argparse
import shlex
import subprocess
import time

import psutil


def check_cpu(cpu_threshold, time_threshold):
    alert_counter_time = 0
    while True:
        time.sleep(1)
        cpu_percentage = psutil.cpu_percent()
        print(cpu_percentage)
        if cpu_percentage >= cpu_threshold:
            if alert_counter_time < time_threshold:
                alert_counter_time += 1
            else:
                message = 'Your cpu is more than {cpu_threshold} for {time_threshold}'.format(cpu_threshold=cpu_threshold, time_threshold=time_threshold)
                send_notify(message)
                alert_counter_time = 0
        else:
            alert_counter_time = 0

def send_notify(msg):
    command = 'notify-send -u normal -i face-worried -t 5000 "{message}"'.format(message=msg)
    print(command)
    shell_command = shlex.split(command)
    print(shell_command)
    subprocess.run(shell_command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Notify your cpu given threshold and duration')
    parser.add_argument('threshold', type=float, help='CPU Percentage threshold')
    parser.add_argument('time', type=int, help='Time in seconds')

    args = parser.parse_args()

    check_cpu(args.threshold, args.time)
