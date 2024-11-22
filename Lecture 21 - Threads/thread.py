###############################################################
# Threads
###############################################################

import time
from datetime import datetime
import threading


def planning_project():
    time.sleep(3)
    print("Planning project")


def starting_project():
    time.sleep(4)
    print('Starting project')


def get_ready():
    time.sleep(5)
    print('Ready project')


start_time = datetime.now()

# planning_project()
# starting_project()
# get_ready()

planning = threading.Thread(target=planning_project)
starting = threading.Thread(target=starting_project)
ready = threading.Thread(target=get_ready)

planning.start()
starting.start()
ready.start()

print(threading.enumerate())

planning.join()
starting.join()
ready.join()

end_time = datetime.now()

print(f'Finished in {end_time - start_time}')






###############################################################
# Thread Attributes
###############################################################

import threading
import time
from random import randint


def worker(task_id):
    compute_time = randint(1, 5)
    print(f'Task {task_id} started, Computing time: {compute_time}')
    time.sleep(compute_time)
    print(f'Task {task_id} finished')


tasks = ['1', '2', '3', '4', '5']

threads = []

for task in tasks:
    thread = threading.Thread(target=worker, args=(task,))
    thread.start()
    threads.append(thread)

print(threading.enumerate())
print(threading.active_count())

for thread in threads:
    thread.join()



###############################################################
# Thread Task Queue
###############################################################

import threading
import time
from queue import Queue

def worker(task_queue):
    while True:

        task = task_queue.get()

        if task is None:
            break

        print(f'Task {task} started')
        time.sleep(1)
        print(f'Task {task} finished')

        task_queue.task_done()


task_queue = Queue()


num_workers = 3
threads = []

for _ in range(num_workers):
    thread = threading.Thread(target=worker, args=(task_queue,))
    thread.start()
    threads.append(thread)


tasks = ['1', '2', '3', '4', '5']

for task in tasks:
    task_queue.put(task)

task_queue.join()

for _ in range(num_workers):
    task_queue.put(None)


for thread in threads:
    thread.join()

print("All tasks finished")

###############################################################
# Multiprocessing
###############################################################
import multiprocessing
import threading
from datetime import datetime

def worker(task_id):
    print(f'Started Processing Task {task_id}')
    result = sum(i * i for i in range(10000000))
    print(f'Finished Processing Task {task_id}')
    return result

start = datetime.now()

# for i in range(5):
#     worker(i)


processes = []
for i in range(5):
    process = multiprocessing.Process(target=worker, args=(i,))
    # process = threading.Thread(target=worker, args=(i,))
    process.start()
    processes.append(process)

for process in processes:
    process.join()

end = datetime.now()

print(f'Finished in time: {end - start}')
