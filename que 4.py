class QueueNode( object ):
  def __init__( self, item ):
    self.item = item
    self.next = None
    
class Queue :

  def __init__( self ):
    self.qhead = None 
    self.qtail = None 
    self.count = 0

  def isEmpty( self ):
    return self.qhead is None

  def len( self ):
    return self.count

  def enqueue( self, item ):
    node = QueueNode( item ) 

    if self.isEmpty() :
      self.qhead = node 
    else :
      self.qtail.next = node

    self.qtail = node
    self.count += 1

  def dequeue( self ):
    if self.isEmpty():
        print("Empty")
    else:
        node = self.qhead

    if self.qhead is self.qtail :
      self.qtail = None

    self.qhead = self.qhead.next 
    self.count -= 1
    return node.item

  def printq(self):
      temp=self.qhead
      while (temp):
          print(temp.item)
          temp=temp.next


myQ = Queue()
n=int(input("Enter how many elements do you want to add in queue: "))
for i in range(1,n+1):
    print("Enter ",i,"th element: ")
    e=int(input())
    myQ.enqueue(e)
print("Lenght before dequeue: ",myQ.len())
print("Your entered queue: ")
print(myQ.printq())
m=int(input("Enter how many elements do you want to a dequeue: "))
for i in range(1,m+1):
    myQ.dequeue()
print("Lenght after dequeue: ",myQ.len())
print("Your queue after dequeue: ")
print(myQ.printq())



