import multiprocessing 

bind = '0.0.0.0:8000'
workers = (2 * multiprocessing.cpu_count()) + 1
threads = workers
loglevel = 'info'

