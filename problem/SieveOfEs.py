from sys import stdin, stdout

def SieveAlgo(n):
    ''' A simple way to find out all primes less than n:
        
        sieve of Eratosthenes
    '''
    sieve = [1]*(n+1)
    p = 2

    while p*p <= n:
        if sieve[p]:
            for i in range(p*2, n+1, p):
                sieve[i] = 0
        p += 1

    for i in range(2, n+1):
        if sieve[i]:
            stdout.writelines('%d\n' % i)

if __name__ == '__main__':
    n = int(stdin.readline().strip())
    SieveAlgo(n)