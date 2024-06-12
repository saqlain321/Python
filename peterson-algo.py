from threading import Thread

class Peterson:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 0

    def process1(self):
        self.flag[0] = True
        self.turn = 1
        while self.flag[1] and self.turn == 1:
            pass
        # Critical section
        print("Process 1 is in critical section")
        self.flag[0] = False

    def process2(self):
        self.flag[1] = True
        self.turn = 0
        while self.flag[0] and self.turn == 0:
            pass
        # Critical section
        print("Process 2 is in critical section")
        self.flag[1] = False

if __name__ == "__main__":
    peterson = Peterson()
    thread1 = Thread(target=peterson.process1)
    thread2 = Thread(target=peterson.process2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
