## 异常
##语法错误和异常



if __name__=='__main__':
    '''
    while True:
        try:
            x=int(input('Please enter a number:'))
        except ValueError:
            print('Oops!Please enter a number.Try again...')
    '''

    try:
        x=1/0
        print(x)
        raise Exception
    except Exception as e:
        print('Error:{0}'.format(e))
        '''
        print('Skip a error!')
        raise
        '''
    print('hello')
    

for i in range(1,9):
    print(i)