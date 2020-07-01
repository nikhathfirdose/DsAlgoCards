# Queue Implementation
class MyCircularQueue:
    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True
        

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1) % self.max_size
            # self.queue[self.front]=0
            self.size -= 1
            return True
        

    def Front(self):
        return self.queue[self.front] if self.size else -1
        

    def Rear(self):
        return self.queue[self.rear] if self.size else -1
        

    def isEmpty(self) :
        return self.size == 0
        

    def isFull(self) :
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
param_1 = obj.enQueue(3)

param_2 = obj.deQueue()

param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
print(obj.queue)


# checkingg repl
