## 对象


class Reverse:

    def __init__(self,data):
        self.data=data
        self.index=len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]


# yield 迭代器
def rev1(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]


if __name__ == "__main__":
    rev=Reverse('zhang')
    print(iter(rev))
    for char in rev:
        print(char)

    for x in rev1('long'):
        print(x)





