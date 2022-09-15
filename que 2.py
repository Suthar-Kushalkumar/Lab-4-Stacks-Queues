class StackNode :
    def __init__( self, item, link ) :
        self.item = item
        self.next = link
        
class Stack :

    def __init__( self ): 
        self.top = None 
        self.size = 0

    def isEmpty( self ): 
        return self.top is None

    def len( self ): 
        return self.size

    def peek( self ):
        if self.top==None:
            print("Empty")
        else:
            return self.top.item

    def pop( self ):
        if self.top==None:
            print("Empty")
        else:
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.item

    def push( self, item ) :
        self.top = StackNode( item, self.top ) 
        self.size += 1

    def postfix(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                e1 = self.pop()
                e2 = self.pop()
                self.push(str(eval(e2 + i + e1)))
        return int(self.pop())
    

myS=Stack()
exp=input("Enter an equation in postfix form: ")
print("Answer: ",myS.postfix(exp))

