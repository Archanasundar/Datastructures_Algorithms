class Stack:
    def __init__(self):
        self.top = -1
        self.stack_list = []

    def check(self):
        return len(self.stack_list) == 0

    def display_stack(self) -> None:
        if self.check():
            print("stack is empty")
        else:
            print(f"stack elements are\n{self.stack_list}")

    def push_element(self, item:int) -> None:
        print(f"Pushed element is -> {item}")
        self.stack_list.append(item)
        self.top += 1

    def pop_element(self)-> None:
        if self.check():
            print("stack is empty nothing to pop")
        else:
            print(f"Popped element is -> {self.stack_list.pop()}")
            self.top -= 1


S = Stack()

while True:
    print(f"Enter your choice\n 1: PUSH \n 2: POP \n 3: DISPLAY STACK \n 0: EXIT")
    choice = int(input())
    if choice is 1:
        item = int(input("Enter value"))
        S.push_element(item)
    elif choice is 2:
        S.pop_element()
    elif choice is 3:
        S.display_stack()
    else:
        exit(0)

