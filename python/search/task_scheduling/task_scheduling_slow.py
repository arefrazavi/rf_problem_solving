#!/bin/python3

from pprint import pprint

#
# Complete the taskScheduling function below.
#
tasks = []
def taskScheduling(d, m):
    global tasks
    task = [d, m]
    tasks.append(task)
    # tasks = sorted(tasks, key=lambda item: (item[0], item[1]))
    tasks.sort(key=lambda item: (item[0], item[1]))

    time = 0
    max_overshoot_time = 0
    for task in tasks:
        time += task[1]
        overshoot_time = task[0] - time
        if overshoot_time < 0 and abs(overshoot_time) > max_overshoot_time:
            max_overshoot_time = abs(overshoot_time)

    return max_overshoot_time


if __name__ == '__main__':
    file_path = '/home/aref/Code/practice_python/problems/search/task_scheduling/input.txt'
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
