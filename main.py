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
