class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size=0

    def insertEnd(self,data):

        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    
    
        

    def traverseList(self) :
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode


def merge(a,b):
    temp=None
    start=None
    if a is None:
        return b
    elif b is None:
        return a
    while(a is not None and b is not None):
        if(a.data<=b.data and temp is None):
            temp=a
            start=temp
            a=a.nextNode
        elif (a.data>=b.data and temp is None):
            temp=b
            start=temp
            b=b.nextNode
        elif (a.data<=b.data):
            temp.nextNode=a
            temp=a
            a=a.nextNode
        elif (a.data>=b.data):
            temp.nextNode=b
            temp=b
            b=b.nextNode
    if(a is None and b is not None):
        while(b is not None):
            temp.nextNode=b
            temp=b
            b=b.nextNode
    elif (a is not None and b is None):
        while(a is not None):
            temp.nextNode=a
            temp=a
            a=a.nextNode
    return start




linkedlist1=LinkedList()
linkedlist2=LinkedList()
linkedlist3=LinkedList()

b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert \n 2 to traverse \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist1.insertEnd(a)
    elif b==2:
        linkedlist1.traverseList()


b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert \n 2 to traverse \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist2.insertEnd(a)
    elif b==2:
        linkedlist2.traverseList()




linkedlist3.head=merge(linkedlist1.head,linkedlist2.head)
linkedlist3.traverseList()


