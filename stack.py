# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:45:18 2021
@author: RAKESH
"""

stack = []
while True:
    print('\n1.Push into stack\n2.Pop from stack\n3.Fetch Top Element\n4.Check IsEmpty\n5.Display stack elements\n6.Exit')
    n=int(input())
    if n==1:
        print('Enter element to push into stack:')
        x=input()
        stack.append(x)
        print(x,'is pushed into stack.')
    elif n==2:
        if len(stack)<=0:
            print('No elements in the stack')
        else:
            print('Element popped from stack is',stack.pop())
    elif n==3:
        print('Top element is:',stack[-1])
    elif n==4:
        if len(stack)==0:
            print('Stack is empty')
        else:
            print('Stack contains few elements.')
    elif n==5:
        i=len(stack)-1
        print('stack elements are:')
        while i>=0:
            print(stack[i], end=' ')
            i=i-1
        print()
    else:
        print('Exiting from stack')
        break