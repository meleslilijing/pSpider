'''
Created on 2016年1月26日

@author: lilijing
'''
import asyncio

@asyncio.coroutine
def A():
    r = ''
    print('1')
    n = yield r
    if n != 2:
        return
    print('2')
    print('3')
    r = "mm"

def B(c):
    c.send(None)
    print('x')
    print('y')
    r = c.send(2)
    print('z')
    print('r: %s'%r)
    c.close()

if __name__ == '__main__':
    c = A()
    B(c)