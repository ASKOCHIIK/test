class Test:
    def test(self, x):
        return x


class Beknazar:
    def t (self, x: int, y: int):
        return x, y

b = Beknazar
test = Test
print(b.t(208, 234))
print(test.test('Hello bootcamp'))

class Altyna:
    def word(self,x):
        return  x
altyna = Altyna
print(altyna.word('Akulya'))

class DONIKO:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return self.name

D = DONIKO('Daniel')
print(D.get_info())

