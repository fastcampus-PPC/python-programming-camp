#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:42:36 2017

@author: yoon
"""

import timeit

# only python2.x
def method1(str_arr):
    out_str = ''
    for num in xrange(len(str_arr)):
        out_str += num
    return out_str

# python3.x
def method1(str_arr):
    out_str = ''
    for num in range(len(str_arr)):
        out_str += str_arr[num]
    return out_str

# only python2.x
def method2(str_arr):
    from array import array
    char_array = array('c')
    for num in range(len(str_arr)):
        char_array.fromstring(str_arr[num])
    return char_array.tostring()

def method4(str_arr):
    from io import StringIO
    file_str = StringIO()
    for num in range(len(str_arr)):
        file_str.write(str_arr[num])
    return file_str.getvalue()

hello = "hello"
world = "world"

print (hello + " " + world)
print (hello, world)
print ("%s %s" % (hello, world))
print ("{} {}".format(hello, world))
print (' '.join([hello, world]))

start = timeit.default_timer()
method2(["awdaw", "awwss", "dddd"])
stop = timeit.default_timer()
print(stop - start)

def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in generator(5):
    print (x)







