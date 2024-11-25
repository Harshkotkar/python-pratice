from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
    print(count)

def main():
    a = Process(target=counter, args=(100000000,))
    a.start()
    a.join()

if __name__ == '__main__':
    main()
