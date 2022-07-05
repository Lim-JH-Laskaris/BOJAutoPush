import sys

class Stack(list):
    def push__(self,x):
        self.append(x)
        
    def pop__(self):
        if len(self)!=0:
            print(self.pop())
        else : 
            print(-1)
        
    def size__(self):
        print(len(self))
        
    def empty__(self):
        print(1 if len(self)==0 else 0)
        
    def top__(self):
        if len(self)!=0:
            print(self[-1])
        else : 
            print(-1)
        
def commend_exec(cmd_str,stack_instance):
    cmd_list = cmd_str.split()
    if len(cmd_list)==1:
        exec('stack_instance.{0}__()'.format(cmd_list[0]))
    else :
        exec('stack_instance.{0}__({1})'.format(cmd_list[0],cmd_list[1]))
            
def main():
    stack_instance = Stack()
    for i in range(int(sys.stdin.readline(),)):
        commend_exec(sys.stdin.readline(),stack_instance)
        
main()