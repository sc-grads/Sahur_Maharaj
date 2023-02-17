import multiprocessing as mp
import time
import threading as th


def namr_time(name):
    print(f'Hello processing: {name} time is {time.time()}')
    print('pause for 2 sec')
    time.sleep(2)
    print('Awake and moving on')


if __name__ == '__main__':
    process_lst = []
    for i in range(10):
        proces = mp.Process(target=namr_time, args=('Shay',))
        process_lst.append(proces)

    for p in process_lst:
        p.start()
        # p.join()  <-- waits for all 10 calls to finish

    for p in process_lst:
        p.join()

    print('Other funcs')
    print('end of processing')


# =================================================================================================================
# multi threading

def namr_time_th(name):
    print(f'Hello threading: {name} time is {time.time()}')
    print('pause for 2 sec')
    time.sleep(2)
    print('Awake and moving on')


if __name__ == '__main__':
    thread_lst = []
    for i in range(10):
        thread = th.Thread(target=namr_time_th, args=('threading_test',))
        thread_lst.append(thread)
    for t in thread_lst:
        t.start()
    for t in thread_lst:
        t.join()
print('end of threading')


# counter
def increment(counter):
    counter.value += 1


def my_increment(my_counter):
    my_counter += 1


if __name__ == '__main__':
    my_counter = 1
    counter = mp.Value('i', 1)

    for i in range(10):
        process = mp.Process(target=increment, args=(counter,))
        process.start()
        process.join()
    print(f'counter of type multiprocessing.Value is {counter.value}')

    for i in range(10):
        process = mp.Process(target=my_increment, args=(my_counter,))
        process.start()
        process.join()

    print(f'my_counter of type integer is {my_counter}')


# parsing arrays to processes
def squares(numbers, squares_list):
    for n in numbers:
        squares_list.append(n ** 2)
    print(f'square_list inside process {squares_list}')


def cubes(numbers, result):
    i = 0
    for num in numbers:
        result[i] = num ** 3
        i += 1
    print(f'result Array inside process/function: {result[::]}')


if __name__ == '__main__':
    numbers = [1, 2, 3]
    squares_list = list()
    p = mp.Process(target=squares, args=(numbers, squares_list))
    p.start()
    p.join()
    print(f'squares_list outsite process {squares_list}')

    result = mp.Array('i', len(numbers))

    p1 = mp.Process(target=cubes, args=(numbers, result))
    p1.start()
    p1.join()
    print(f'result Array outside process {result[::]}')


# locks

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 2
        lock.release()


if __name__ == '__main__':
    balance = mp.Value('i', 500)  # starting balance
    print(f'Balance BEFORE running processes: {balance.value}')

    lock = mp.Lock()  # lock Object
    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f'Balance AFTER running processes: {balance.value}')
