class stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
        # self.list = [item] + self.list

    def pop(self):
        return self.list.pop()
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # prints 30


class queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)
        # self.list = [item] + self.list

    def dequeue(self):
        return self.list.pop(0)
    
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # prints 10


# Binary Search
arr = [10, 20, 30, 40, 50]
x = int(input("Enter value to search: "))
start = 0
end = len(arr) - 1

while start <= end:
    mid = (start + end) // 2
    if arr[mid] == x:
        print("Element is present in the set at index ", mid)
        break
    elif arr[mid] < x:
        start = mid + 1
    else:
        end = mid - 1
    

# print(arr)  # prints {10, 20, 30, 40, 50}

