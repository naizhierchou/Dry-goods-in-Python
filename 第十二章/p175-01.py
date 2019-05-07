class ShortInputException(Exception):
    # '''⾃定义的异常类'''
    def __init__(self, length, atleast):
        # super().__init__()
        self.length = length
        self.atleast = atleast

    def __str__(self):
        return ('输⼊的⻓度是 %d,⻓度⾄少应是 %d' % (self.length, self.atleast))


def main():
    try:
        s = input('请输⼊ --> ')
        if len(s) < 3:
            # raise 引发⼀个⾃定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:  # x这个变量被绑定到了错误的实例
        print('ShortInputException:' % result)
    else:
        print('没有异常发⽣.')
main()
