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

class Kairat:
    def User(self, name, lastname):
        self.n = name
        self.l = lastname

n = Kairat.User('kairat', 'ajybaev')
print(n)