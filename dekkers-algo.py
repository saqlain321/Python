from threading import Thread

class Dekker:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 0

    def process1(self):
        while True:
            self.flag[0] = True
            while self.flag[1]:
                if self.turn != 0:
                    self.flag[0] = False
                    while self.turn != 0:
                        pass
                    self.flag[0] = True
            # Critical section
            print("Process 1 is in critical section")
            self.turn = 1
            self.flag[0] = False

    def process2(self):
        while True:
            self.flag[1] = True
            while self.flag[0]:
                if self.turn != 1:
                    self.flag[1] = False
                    while self.turn != 1:
                        pass
                    self.flag[1] = True
            # Critical section
            print("Process 2 is in critical section")
            self.turn = 0
            self.flag[1] = False

if __name__ == "__main__":
    dekker = Dekker()
    thread1 = Thread(target=dekker.process1)
    thread2 = Thread(target=dekker.process2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
