#### THIS IS A BAD SOLUTION
### USING A TIMESTAMP IS MUCH BETTER
from collections import deque


class Animal:
    def __init__(self, type):
        if type:
            self.type = "cat"
        else:
            self.type = "dog"
        self.timestamp = None

    def __repr__(self):
        return self.type

class AnimalQueue():
    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.time = 0

    def __repr__(self):
        return " ".join([self.cat_queue.__repr__(), self.dog_queue.__repr__()])

    def enqueue(self, animal):
        animal.timestamp = self.time
        self.time += 1
        if animal.type == "cat":
            self.cat_queue.append(animal)
        else:
            self.dog_queue.append(animal)

    def dequeue_any(self):
        if not self.cat_queue and not self.dog_queue:
            return None
        elif not self.cat_queue:
            return self.dog_queue.popleft()
        elif not self.dog_queue:
            return self.cat_queue.popleft()
        else:
            print "Comparing " + str(self.cat_queue[0].timestamp) + " and " + str(self.dog_queue[0].timestamp)
            if self.cat_queue[0].timestamp > self.dog_queue[0].timestamp:
                return self.dog_queue.popleft()
            else:
                return self.cat_queue.popleft()

    def dequeue_cat(self):
        if not self.cat_queue:
            return None
        return self.cat_queue.popleft()

    def dequeue_dog(self):
        if not self.dog_queue:
            return None
        return self.dog_queue.popleft()


if __name__ == "__main__":
    a = AnimalQueue()
    print a
    a.enqueue(Animal(1))
    print a
    a.enqueue(Animal(0))
    print a
    a.enqueue(Animal(1))
    print a
    a.enqueue(Animal(1))
    print a
    a.enqueue(Animal(0))
    print a
    a.enqueue(Animal(1))
    print a
    a.enqueue(Animal(0))
    print a
    a.enqueue(Animal(1))
    print a
    a.enqueue(Animal(1))
    print a
    a.enqueue(Animal(0))
    print a
    a.dequeue_any()
    print a
    a.dequeue_any()
    print a
    a.dequeue_any()
    print a
    a.dequeue_any()
    print a
    a.dequeue_any()
    print a
    a.dequeue_any()
    print a