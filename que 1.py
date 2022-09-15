class _StackNode :
    def __init__( self, item, link ) :
        self.item = item
        self.next = link
        
class Stack :

    def __init__( self ): 
        self._top = None 
        self._size = 0

    def isEmpty( self ): 
        return self._top is None

    def __len__( self ): 
        return self._size

    def peek( self ):
        if self._top==None:
            print("Empty")
        else:
            return self._top.item

    def pop( self ):
        if self._top==None:
            print("Empty")
        else:
            node = self._top
            self._top = self._top.next
            self._size -= 1
            return node.item

    def push( self, item ) :
        self._top = _StackNode( item, self._top ) 
        self._size += 1


myS = Stack()
print("Length: ",myS.__len__())
print("Is stack empty: ",myS.isEmpty())
n=int(input("Enter how many elements do you want to add in stack: "))
for i in range(0,n):
    print("Enter element",i,": ")
    e=int(input())
    myS.push(e)
    
print("Length: ",myS.__len__())
print("Top item: ",myS.pop())
print("Top item after removing top: ",myS.peek())
print("Is stack empty: ",myS.isEmpty())
