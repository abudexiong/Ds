# -*-coding:utf-8 -*-
__author__ = '凯'

class Stack:
    def __init__(self,size=32):
        self.stack=[]
        self.size=size
        self.top=1
    def set_size(self,size):
        self.size=size
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def is_full(self):
        if self.top +1 ==self.size:
            return True
        else:
            return False
    def top(self):
        if self.is_empty():
            raise Exception("StackIsEmpty")
        else:
            return self.stack[self.top]
    def push(self,obj):
        if self.is_full():
            raise Exception("StackOverFlow")
        else:
            self.stack.append(obj)
            self.top+=1
    def pop(self):
        if self.is_empty():
            raise Exception("StackIsEmpty")
        else:
            self.top-=1
            return self.stack.pop()
    def show(self):
        print(self.stack)

s=Stack(10)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.show()
s.pop()
s.show()
s.push(7)
s.show()
