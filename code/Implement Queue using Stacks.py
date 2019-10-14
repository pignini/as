class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x=None #把x(第一個數)就是self當下的那個值設成None，None表示裡面是空的
        self.next=None     #self.next(下一個位置)設成None

    def push(self, x: int) -> None:       #push就是把資料放進Queue的最後面，x: int是輸入要加的數字(int是整數)
        """
        Push element x to the back of queue.
        """
        if self.x == None:       #如果第一個值是空的            
            self.x=x         #要加的數字就會是新的第一個數，舉例：假如我要加一個數字0，x就會＝0，原本self.x裡面是空的，把0加進來，0就變self.x
        elif self.x != None:   #如果self.x不是空的(!= 是不等於的意思)
            n=self                   #設self是一個代號n
            while n.next != None:      #如果n的下一個也不是空的，跑while迴圈，
                n=n.next                      #要把原本的n.next改成n，原本的n.next.next變成n.next
                                                     #舉例：假設self裡面有0,1，我要加2進來，會變成1,2
            n.next=MyQueue()         
            n.next.x=x                        #所以現在n.next.x就是2了，也就是你要加進來的數字x: int的x => n.next.x=x
                                                     #舉例：數值1,2,3，要加4進來，第一個值跟第二個值都不是空的(1,2)，所以再往後看，2,3也不是空的，3後是空的，所以4可以進來

    def pop(self) -> int:    #把前面所指向的資料從Queue中移除，並更新front。
        """
        Removes the element from in front of queue and returns that element.
        """
        n=self           #一樣設self是n
        m=self.x       #self.x是m
        if n.x != None and n.next == None:      #如果數列只有一個數字，就是n自己的話
            n.x=None       #把n刪掉
        elif n.next != None:       #如果n.next還有數字
            n.x=n.next.x     #這裡就跟上面push是一樣觀念，要把原本的n.next改成n，原本的n.next.next變成n.next
            n.next=n.next.next
        return m              #傳回被pop的值
            

    def peek(self) -> int:    #查看self裡面的第一個數
        """
        Get the front element.
        """
        return self.x    #假設我的linked list是(0,1,2,3,4)他要的是0，也就是self.x

    def empty(self) -> bool:  #如果數列是空的
        """
        Returns whether the queue is empty.
        """
        return self.x == None    #那self.x就是None了


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
