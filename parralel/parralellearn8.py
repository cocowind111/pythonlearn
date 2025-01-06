from multiprocessing import Process, Queue
 
def sender(queue):
    queue.put("Hello from sender")
 
def receiver(queue):
    message = queue.get()
    print(f"Received message: {message}")
 
if __name__ == "__main__":
    queue = Queue()
 
    p1 = Process(target=sender, args=(queue,))
    p2 = Process(target=receiver, args=(queue,))
 
    p1.start()
    p2.start()
 
    p1.join()
    p2.join()