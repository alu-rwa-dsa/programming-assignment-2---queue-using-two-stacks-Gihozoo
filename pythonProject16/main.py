# Enter your code here. Read input from STDIN. Print output to STDOUT
class Q(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def sync(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def dequeue(self):
        self.sync()
        return self.s2.pop()

    def top(self):
        self.sync()
        return self.s2[-1]


queue1 = Q()

n = int(input())
for i in range(n):
    myQueue = tuple(map(int, input().strip().split(' ')))
    if len(myQueue) > 1:
        queue1.enqueue(myQueue[1])
    elif myQueue[0] == 2:
        queue1.dequeue()
    else:
        print(queue1.top())

