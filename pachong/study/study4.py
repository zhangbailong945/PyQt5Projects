## 异常
##语法错误和异常



if __name__=='__main__':
    while True:
        try:
            x=int(input('Please enter a number:'))
        except ValueError:
            print('Oops!Please enter a number.Try again...')