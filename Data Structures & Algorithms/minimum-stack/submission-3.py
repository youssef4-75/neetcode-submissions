class MinStack:

    def __init__(self):
        self.__s = []
        self.__m = []
        

    def push(self, val: int) -> None:
        self.__s.append(val)
        if self.__m and self.__m[-1] < val:
            self.__m.append(self.__m[-1])
        else:
            self.__m.append(val)


    def pop(self) -> None:
        self.__s.pop()
        self.__m.pop()
        

    def top(self) -> int:
        return self.__s[-1]

    def getMin(self) -> int:
        return self.__m[-1]
        
