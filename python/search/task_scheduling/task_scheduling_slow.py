#!/bin/python3

from pprint import pprint
import bisect

#
# Complete the taskScheduling function below.
#
tasks = []
def taskScheduling(d, m):
    global tasks
    task = (d, m)
    # Sort task by deadline and then minutes.
    #tasks.append(task)
    #tasks.sort(key=lambda item: (item[0], item[1]))

    bisect.insort(tasks, task)
    time = 0
    max_overshoot_time = 0
    for task in tasks:
        time += task[1]
        overshoot_time = task[0] - time
        if overshoot_time < 0 and abs(overshoot_time) > max_overshoot_time:
            max_overshoot_time = abs(overshoot_time)

    return max_overshoot_time


if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')
    task_count = int(rows[0])

    for task_index in range(1, task_count + 1):
        dm = rows[task_index].split()
        d = int(dm[0])
        m = int(dm[1])
        result = taskScheduling(d, m)
        print(result)
