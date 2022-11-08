class _PriorityQEntry( object ):
  def __init__( self, item, priority ):
    self.item = item
    self.priority = priority
    self.next=None


class PriorityQueueL:
    def __init__( self ):
        self._qhead = None
        self._qtail = None
        self._size = 0

    def isEmpty( self ):
        return self._qhead is None

    def __len__( self ):
        return self._size

    def prnpq ( self ):
      temp=self._qhead
      while(temp):
        print(temp.item,temp.priority)
        temp=temp.next

    def enqueue( self, item, priority ):

        node = _PriorityQEntry( item, priority )
        
        if self.isEmpty() :
            self._qhead = node
        else :
            self._qtail.next = node
        
        self._qtail = node
        self._size += 1

    def dequeue( self ) :
        
        assert not self.isEmpty(), 

        prenode = self._qhead
        node=self._qhead.next
        
        highpri  = self._qhead.priority 
        highnode = self._qhead
        
        while prenode !=  None :
          if node.priority < highpri :
            highpri  = node.priority
            highnode = node
          prenode=prenode.next

        prenode == highnode.next
        

            



mypql = PriorityQueueL()
mypql.enqueue( "purple", 5 )
mypql.enqueue( "black", 1 )
mypql.enqueue( "orange", 3 )
mypql.enqueue( "white", 0 )
mypql.enqueue( "green", 1 )
mypql.enqueue( "yellow", 5 )
mypql.prnpq()
mypql.dequeue()
print("\n")
mypql.prnpq()
