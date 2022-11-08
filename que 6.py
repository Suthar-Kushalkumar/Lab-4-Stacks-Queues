class Queue :

    def __init__( self ): 
        self.qList = list()

    def isEmpty( self ): 
        return len( self ) == 0

    def __len__( self ):
        return len( self.qList )

    def printq(self):
        print("Queue: ")
        for i in self.qList:
            print(i)

    def enqueue_rear( self, item ):
        print("Enqueue from rear side: ",item)
        self.qList.append( item )

    def enqueue_front(self,item):
        print("Enqueue from front side: ",item)
        new_list=[]
        new_list.append(item)
        for i in self.qList:
            new_list.append(i)
        self.qList=new_list

    def dequeue_rear(self):
        print("Dequeue from rear side element: ")
        return self.qList.pop((len(self.qList))-1)
        
    def dequeue_front( self ):
        print("Dequeue from front side element: ")
        return self.qList.pop( 0 )


myQ = Queue()

print(myQ.isEmpty())
myQ.enqueue_rear(28)
print(myQ.isEmpty())
myQ.enqueue_rear(19)
myQ.enqueue_front(45)
myQ.printq()
print(myQ.dequeue_front())
myQ.printq()
print(myQ.dequeue_rear())
myQ.printq()



