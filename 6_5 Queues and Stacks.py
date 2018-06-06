class Stack:
    def __init__(self, size):
        self.items = []
        self.size = int(size)
        for i in range(self.size):
            self.items.append('')
        self.isfull = False
        self.current = 0

    def isEmpty(self):
         return self.isempty

    def push(self, item):
        if self.isfull:
            raise 'Stack is FULL'
        self.items[self.current] = item
        
        if self.current + 1 == self.size:
            self.isfull = True
        else:
            self.current += 1

    def pop(self):
        if self.current == 0:
            raise 'Stack is EMPTY'
            
        if self.isfull:
            item = self.items[self.current]
            self.isfull = False
        else:
            item = self.items[self.current - 1]
            self.current -= 1

        return item

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

class Queue:
    def __init__(self, size):
        self.items = []
        self.size = int(size)
        for i in range(self.size):
            self.items.append('')
        self.isempty = True
        self.current = 0
        self.next = 0

    def isEmpty(self):
        return self.isempty

    def enqueue(self, item):
        
        if self.next == self.current and self.isempty == False:
            raise 'Queue is FULL'
            
        self.items[self.next] = item
        self.isempty = False
        self.next = (self.next + 1) % self.size                
        
    def dequeue(self):
        if self.isempty : 
            raise 'Queue is EMPTY'    
            
        item = self.items[self.current]
        self.current = (self.current + 1) % self.size
        if self.current == self.next:
            self.isempty = True
        return item

    def size(self):
        return len(self.items)    

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class QueueOnList:
    
    def __init__(self):
        self.first = None
        self.last = None
        
    def enqueue(self, value):
        item = ListNode(value)
        
        if self.first == None:
            self.first = item
            self.last = item
        else:
            self.last.next = item
            self.last = item
        
    def dequeue(self):
        if self.first == None:
            raise 'Queue is Empty'
            
        item = self.first
        self.first = self.first.next
        
        return item.value

    def printQueue(self):
        item = self.first
        arr = []
        while item != None:
            arr.append(item.value)
            item = item.next
        print arr
    
        
class StackOnList:
    
    def __init__(self):
        self.first = None
        
    def push(self, value):
        item = ListNode(value)
        item.next = self.first
        self.first = item
        
    def pop(self):
        if self.first == None:
            raise 'Stack is EMPTY'
        item = self.first
        self.first = self.first.next
        
        return item.value
    
    def printStack(self):
        item = self.first
        arr = []
        while item != None:
            arr.append(item.value)
            item = item.next
        print arr
        
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = StackOnList()
        self.queue = QueueOnList()
    
    def pushCharacter(self, ch):
        self.stack.push(ch)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def enqueueCharacter(self, ch):
        self.queue.enqueue(ch)
        
    def dequeueCharacter(self) :
        return self.queue.dequeue()
    
    