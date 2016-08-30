#### THIS IS A BAD SOLUTION
### USING A TIMESTAMP IS MUCH BETTER
from collections import deque


class Animal:
    def __init__(self, type):
        if type:
            self.type = "cat"
        else:
            self.type = "dog"

    def __repr__(self):
        return self.type

class AnimalQueue():
    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.cat_dog_q = deque()
        self.cats_given = 0
        self.dogs_given = 0

    def __repr__(self):
        return " ".join([self.cat_queue.__repr__(), self.dog_queue.__repr__(), self.cat_dog_q.__repr__()])

    def enqueue(self, animal):
        if animal.type == "cat":
            self.cat_queue.append(animal)
            self.cat_dog_q.append(animal)
        else:
            self.dog_queue.append(animal)
            self.cat_dog_q.append(animal)

    def helper_clean(self):
        while self.cats_given > 0 and self.cat_dog_q[0].type == "cat":
            self.cat_dog_q.popleft()
            self.cats_given -= 1
        while self.dogs_given > 0 and self.cat_dog_q[0].type == "dog":
            self.cat_dog_q.popleft()
            self.dogs_given -= 1

    def dequeue_any(self):
        self.helper_clean()
        if not self.cat_dog_q:
            return None
        if self.cat_dog_q[0].type == "cat":
            self.cat_queue.popleft()
        else:
            self.dog_queue.popleft()
        return self.cat_dog_q.popleft()

    def dequeue_cat(self):
        self.helper_clean()
        if not self.cat_queue:
            return None
        if self.cat_dog_q[0].type == "dog":
            self.cats_given += 1
        else:
            self.cat_dog_q.popleft()
        return self.cat_queue.popleft()

    def dequeue_dog(self):
        self.helper_clean()
        if not self.dog_queue:
            return None
        if self.cat_dog_q[0].type == "cat":
            self.dogs_given += 1
        else:
            self.cat_dog_q.popleft()
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
    a.dequeue_cat()
    print a
    a.dequeue_cat()
    print a
    a.dequeue_cat()
    print a
    a.dequeue_cat()
    print a
    a.dequeue_cat()
    print a
    a.dequeue_cat()
    print a
    a.dequeue_dog()
    print a
    a.dequeue_dog()
    print a
    a.dequeue_any()
    print a
    a.dequeue_any()
    print a