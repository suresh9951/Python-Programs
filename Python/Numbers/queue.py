class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def insert(self, index, data):
        if index < 0 or index > len(self.queue):
            return "Index out of range"
        self.queue.insert(index, data)

    def delete(self, index):
        if index < 0 or index >= len(self.queue):
            return "Index out of range"
        return self.queue.pop(index)

    def extend(self, iterable):
        self.queue.extend(iterable)

    def __str__(self):
        return str(self.queue)

# Example usage
q = Queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(55)
print(q)

q.insert(1, 3)
print(q)

q.delete(2)
print(q)

q.extend([7, 8, 9])
print(q)

q.enqueue(19)
print(q)

q.dequeue()
print(q)
#type:ignore