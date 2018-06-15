#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

string을 concat하는 여러가지 방법

'''


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


def method2(str_arr):
    from io import StringIO
    file_str = StringIO()
    for num in range(len(str_arr)):
        file_str.write(str_arr[num])
    return file_str.getvalue()


hello = "hello"
world = "world"

method2(hello)

print (hello + " " + world)
print (hello, world)
print ("%s %s" % (hello, world))
print ("{} {}".format(hello, world))
print (' '.join([hello, world]))

method2(["awdaw", "awwss", "dddd"])



'''

generator에 대한 설명 및 예제

'''

def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in generator(5):
    print (x)


'''

generator가 머신 러닝에 적용되는 예제

'''

### 문서를 스트리밍 형식으로 읽도록 하는 함수
def stream_docs(dataset):
    for row in dataset:
        text, label = row[0], row[1]
        yield text, label


### 미니배치를 얻어오는 함수
def get_minibatch(doc_stream, size):
    docs, y = [], []
    try:
        for _ in range(size):
            text, label = next(doc_stream)
            docs.append(text)
            y.append(label)
    except StopIteration:
        return None, None
    return docs, y


### N x 2 의 형태로 되어있는 데이터셋
doc_stream = stream_docs({your data})


### Some codes/logics here
for _ in range(10):
    X_train, y_train = get_minibatch(doc_stream, size=500)