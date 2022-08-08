class MyCircularQueue:
    def __init__(self, size: int):
        self.cir_queue = [None]*size
        self.size = 0
        self.capacity = size
        self.rear = -1
        self.front = -1

    def enqueue(self, value: int) -> bool:
        if not(self.is_full()):
          self.rear = (self.rear+1)%self.capacity
          self.cir_queue[self.rear] = value
          self.size = self.size + 1
          return True
        else:
          return False

    def dequeue(self) -> bool:
        if not(self.is_empty()):
          del self.cir_queue[0]
          self.front = (self.front+1)%self.capacity
          self.size = self.size - 1
          print(self.cir_queue)
          return True
        else:
          return False

    def get_front(self) -> int:
        if self.is_empty():
          return(-1)
        else:
          return(self.cir_queue[0])

    def get_rear(self):
        if self.is_empty():
          return(-1)
        else:
          return(self.cir_queue[0])


    def is_empty(self):
        return(self.size == 0)

    def is_full(self):
        return (self.size == self.capacity)


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
