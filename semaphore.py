import threading

class Semaphore:
    def __init__(self, initial_units=1):
        self.lock = threading.Lock()
        self.units = initial_units

    def acquire(self):
        with self.lock:
            while self.units == 0:
                self.lock.release()
                self.lock.acquire()
            self.units -= 1

    def release(self):
        with self.lock:
            self.units += 1

    def __enter__(self):
        self.acquire()

    def __exit__(self, type, value, traceback):
        self.release()

if __name__ == "__main__":
    semaphore = Semaphore(2)

    def worker(id):
        with semaphore:
            print(f"Worker {id} acquired semaphore")
            # Simulate some work
            threading.currentThread().name = f"Worker {id}"
            print(threading.currentThread().name)

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
