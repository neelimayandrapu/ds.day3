 #stack implimentation using list
neel=[]
def push():
    ele=int(input("enter the element :"))
    neel.append(ele)
    print(neel)
def pop():
    if not neel:
        print("stack is empty")
    else:
        p=neel.pop()
        print("removed element :",p)
        print(neel)
while True:
    print(" select operation 1.push 2.pop 3.quit")
    select=int(input())
    if select==1:
        push()
    elif select==2:
        pop()
    elif select==3:
        break
    else :
        print("choose correct option")
        



#stack implimentation using LL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            popendnode=self.head
            self.head=self.head.next
            popendnode.next=None
            return  popendnode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("stack is underflow")
        else:
            while(t !=None):
                print(t.data,end=" ")
                t=t.next
                if(t!=None):
                    print("-->",end=" ")
            return

if __name__=="__main__":
    N=stack()
    N.push(218)
    N.push(265)
    N.push(1)
    N.push(2)
    N.display()
    print(" ")
    print("peek",N.peek())
    N.pop()
    N.pop()
    N.display()
    print(" ")
    print("peek",N.peek())


#stack implimentation using LL(IN CASE OF EMPTY LIST)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            popendnode=self.head
            self.head=self.head.next
            popendnode.next=None
            return  popendnode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("stack is underflow")
        else:
            while(t !=None):
                print(t.data,end=" ")
                t=t.next
                if(t!=None):
                    print("-->",end=" ")
            return

if __name__=="__main__":
    N=stack()
    N.display()
    print(" ")
    print("peek",N.peek())
    N.pop()
    N.pop()
    N.display()
    print(" ")
    print("peek",N.peek())
    N.push(218)
    N.display()

-->>#OUTPUT

stack is underflow
 
peek None
stack is underflow
 
peek None
218 




#queue implimentation using array/list

neel=[]
def enqueue():
    ele=int(input("enter the element :"))
    neel.append(ele)
    print(neel)
def dequeue():
    if not neel:
        print("stack is empty")
    else:
        d=neel.pop()
        print("removed element :",d)
        print(neel)
def display():
    print(neel)
while True:
    print(" select operation 1.ADD 2.REMOVE 3.SHOW ")
    select=int(input())
    if select==1:
        enqueue()
    elif select==2:
        dequeue()
    elif select==3:
        display()
    else :
        print("choose correct option")

-->>OUTPUT
 select operation 1.ADD 2.REMOVE 3.SHOW 
1
enter the element :218
[218]
 select operation 1.ADD 2.REMOVE 3.SHOW 
1
enter the element :265
[218, 265]
 select operation 1.ADD 2.REMOVE 3.SHOW 
1
enter the element :143
[218, 265, 143]
 select operation 1.ADD 2.REMOVE 3.SHOW 
3
[218, 265, 143]
 select operation 1.ADD 2.REMOVE 3.SHOW 



# queue inmplimentation using queue module
import queue
N=queue.Queue(maxsize=5)
N.put(218)
N.put(265)
print(type(N))
print(N.get())
print(N.get())


-->>OUTPUT

<class 'queue.Queue'>
218
265




#stack implimentation using list
neel=[]
naar=[]
def push():
    ele=int(input("enter the element :"))
    if ele%2==0:
        neel.append(ele)
        print(neel)
    else :
        naar.append(ele)
        print(naar)
def pop():
    n=int(input("enter the element:"))
    if n==1:
        neel.pop()
        print(neel)
    else :
        
        naar.pop()
        print(naar)
def display():
    if num==1:
        print(neel)
    else:
        
        print(naar)
while True:
    print(" select operation 1.push 2.pop 3.show 4.quit")
    select=int(input())
    if select==1:
        push()
    elif select==2:
        pop()
    elif select==3:
        print("enter the stack num")
        num =int(input())
        display()
    
    elif select==4:
        break
    else :
        print("choose correct option")

-->>OUTPUT

 select operation 1.push 2.pop 3.show 4.quit
1
enter the element :24
[24]
 select operation 1.push 2.pop 3.show 4.quit
1
enter the element :33
[33]
 select operation 1.push 2.pop 3.show 4.quit
1
enter the element :34
[24, 34]
 select operation 1.push 2.pop 3.show 4.quit
1
enter the element :55
[33, 55]
 select operation 1.push 2.pop 3.show 4.quit
3
enter the stack num
1
[24, 34]
 select operation 1.push 2.pop 3.show 4.quit
3
enter the stack num
2
[33, 55]
 select operation 1.push 2.pop 3.show 4.quit
2
enter the element:1
[24]
 select operation 1.push 2.pop 3.show 4.quit
2
enter the element:2
[33]
 select operation 1.push 2.pop 3.show 4.quit
2
enter the element:1
[]
 select operation 1.push 2.pop 3.show 4.quit
2
enter the element:2
[]
 select operation 1.push 2.pop 3.show 4.quit
3
enter the stack num
1
[]
 select operation 1.push 2.pop 3.show 4.quit
3
enter the stack num
2
[]
 select operation 1.push 2.pop 3.show 4.quit
4

        
# Queue in nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next= Node(data)
            self.last=self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
a_queue =Queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")
    #by using split,do will become a list,split works with string
    do =input("what would you like to do ?").split()
    operation =do[0].strip().lower()
    if operation=="enqueue":
        a_queue.enqueue(int(do[1]))
    elif operation=="dequeue":
        dequeued =a_queue.dequeue()
        if dequeued is None:
            print("queue is empty")
        else:
            print("dequeued element :",int(dequeued))

    elif operation=='quit':
        break
#OUTPUT
-->>
enqueue <value>
dequeue
quit
what would you like to do ?enqueue 100
enqueue <value>
dequeue
quit
what would you like to do ?enqueue 500
enqueue <value>
dequeue
quit
what would you like to do ?dequeue
dequeued element : 100
enqueue <value>
dequeue
quit
what would you like to do ?quit


        


    
        
        

    
        