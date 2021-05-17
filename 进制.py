# a = int(input("输入十进制："))
# b = hex(a)
# print(b)

class CC:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def print(self):
        print(self.x, self.y)


dd = CC(5, 6)
dd.print()


class rectangle():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_rectangle(self):
        return self.x

    def reset_rectangle(self, x):
        self.x = x

    def del_rectangle(self):
        del self.x
        del self.y

    def getPerimeter(self):
        return (self.x + self.y)*2

    def getArea(self):
        return self.x * self.y

    rect_long = property(get_rectangle, reset_rectangle, del_rectangle)


true_retangle = rectangle(6, 9)
true_retangle.rect = (5)
print(true_retangle.getPerimeter())
print(true_retangle.getArea())
