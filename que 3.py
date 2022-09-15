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

    def parentheses(self, exp):
        c1=0
        c2=0
        c3=0
        c4=0
        for i in exp:
            if i=='/':
                if i=='/':
                    break
            else:
                if i=='(':
                    c1=c1+1
                if i==')':
                    c2=c2+1
                if i=='[':
                    c3=c3+1
                if i==']':
                    c4=c4+1
        if c1==c2 and c3==c4:
            return "Valid"
        else:
            return "Invalid"

    

myS=Stack()
exp=input("Enter an equation in postfix form: ")
e="231*+9-"
print("Answer: ",myS.parentheses(exp))




