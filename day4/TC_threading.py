import threading
def task():
    print("Threading is running")
t=threading.Thread(target=task)
t.start()
t.join()
print("main thread")