class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x=None  #把x(第一個數)就是self當下的那個值設成None，None表示裡面是空的
        self.next=None     #self.next(下一個位置)設成None       

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.x == None:       #如果第一個值是空的            
            self.x=x         #要加的數字就會是新的第一個數，舉例：假如我要加一個數字0，x就會＝0，原本self.x裡面是空的，把0加進來，0就變self.x
        else:   #如果self.x不是空的
            n=self                   #設self是一個代號n
            while n.next != None:      #如果n的下一個也不是空的，跑while迴圈，
                n=n.next                      #要把原本的n.next改成n，原本的n.next.next變成n.next
                                                     #舉例：假設self裡面有0,1，我要加2進來，會變成1,2
            n.next=MyStack()         
            n.next.x=x             #要加的數字就會是新的第一個數，舉例：假如我要加一個數字0，x就會＝0，原本self.x裡面是空的，把0加進來，0就變self.x        
            
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n=self           #一樣設self是n
        while n.next != None and n.next.x != None: 
            n=n.next     #這裡就跟上面push是一樣觀念，要把原本的n.next改成n，原本的n.next.next變成n.next          
        m = n.x           
        n.x=None
        return m 
        
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.x == None:       #如果第一個值是空的            
            return None        #要加的數字就會是新的第一個數，舉例：假如我要加一個數字0，x就會＝0，原本self.x裡面是空的，把0加進來，0就變self.x
        elif self.x != None:   #如果self.x不是空的(!= 是不等於的意思)
            n=self                   #設self是一個代號n
            while n.next != None and n.next.x != None:      #如果n的下一個也不是空的，跑while迴圈，
                n=n.next   
        return n.x    #假設我的linked list是(0,1,2,3,4)他要的是0，也就是self.x

    def empty(self) -> bool:  #如果數列是空的
        return self.x == None    #那self.x就是None了
