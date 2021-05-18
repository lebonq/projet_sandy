class Plage:

    def __init__(self, num = None):
        if num is None:
            self.num = 0
        else:
            self.num = num

    def getNum(self):
        return self.num
    
    def setNum(self, num):
        self.num = num

    def print_hello(self):
        print("Hello World !")
        return
