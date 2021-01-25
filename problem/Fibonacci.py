from sys import stdin,stdout

class Fibonacci():
    def __init__(self, n: int):
        ''' The n-th fibonacci number
        
        '''
        self.N = n

    def usual(self, n: int) -> int:
        ''' usual fabonacci number
        
        '''
        if n < 0: return
        return n + self.fibonacci_usual(n-1) if n > 1 else n

    def generator(self, n: int) -> int:
        ''' Calculate fibonacci number by generator
        
        '''
        def generator(n: int):
            a, b = (1, 1)
            while n > 2:
                a, b = b, a+b
                n-=1
                yield(a, b)
        
        fibo = generator(n)
        x, y = -1, -1
        
        for i in range(n-2):
            x, y = next(fibo)
        
        return y

    def dynamic(self, n: int) -> int:
        ''' dp fibonacci
        
        '''
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a

    def exponent(self, n: int) -> set:
        ''' the fastest fibonacci
        
        '''
        if n == 0:
            return (0,1)
        else:
            a, b = self.exponent(n//2)
            c = a*(2*b-a)
            d = a*a+b*b

            return (c,d) if n % 2 == 0 else (d, c+d)

    def main(self, method_code: int):
        if method_code == 0:
            stdout.writelines("%d\n" % self.usual(self.N))
        elif method_code == 1:
            stdout.writelines("%d\n" % self.generator(self.N))
        elif method_code == 2:
            stdout.writelines("%d\n" % self.dynamic(self.N))
        elif method_code == 3:
            stdout.writelines("%d\n" % self.exponent(self.N)[0])
        else:
            stdout.writelines("Wrong code\n")


if __name__ == '__main__':
    n, code = map(int, stdin.readline().strip().split())
    fibo = Fibonacci(n)
    fibo.main(code)
