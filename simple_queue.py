class SimpleQueue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item) ->None:
        print(f"Enqueued element is -> {item}")
        self.queue.append(item)

    def check(self) -> bool:
        return len(self.queue) == 0

    def dequeue(self) ->None:
        if self.check():
            print("empty queue")
        else:
            print(f"Dequeued elemet is -> {self.queue.pop(0)}")

    def display_queue(self)-> None:
        if self.check():
            print("empty queue")
        else:
            print(f"queue elemets are \n {self.queue}")

Q = SimpleQueue()
while True:
    print(f"Enter your choice\n 1: Enqueue \n 2: Dequeue \n 3: Display queue \n 0: Exit")
    choice = int(input())
    if choice is 1:
        item = int(input("Enter value"))
        Q.enqueue(item)
    elif choice is 2:
        Q.dequeue()
    elif choice is 3:
        Q.display_queue()
    else:
        exit(0)

