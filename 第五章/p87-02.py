def testB():
    print('---- testB start----')
    print('这⾥是testB函数执⾏的代码...(省略)...')
    print('---- testB end----')
def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')
testA()