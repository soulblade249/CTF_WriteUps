import socket, gmpy2, random

def sieve():
    primes = set()
    sieve = [True for _ in range(2**16)]
    for i in range(2, len(sieve)):
        if sieve[i]:
            primes.add(i)
        j = i
        while (i * j) < len(sieve):
            sieve[i * j] = False
            j += 1
    return primes

def connect():
    s = socket.socket()
    s.connect(("shell2017.picoctf.com", 47321))
    return s

def recv(s):
    return s.recv(1024).decode("ascii")

primes = sorted(sieve())[:175]
s = connect()
print(recv(s))
_, Ns, es, _ = recv(s).splitlines()
N = gmpy2.mpz(Ns.split(":")[1])
e = gmpy2.mpz(es.split(":")[1])
d = {1:1}
for p in primes:
    s.sendall((str(p) + "\n").encode("ascii"))
    recv(s)
    response = recv(s)
    d[p] = gmpy2.mpz(response.strip().splitlines()[0])
s.sendall(b"-1\n")
recv(s)
x = recv(s).strip().splitlines()[0]
chal = gmpy2.mpz(x)
res = gmpy2.mpz(1)
for p in primes:
    while chal % p == 0:
        res *= d[p]
        res %= N
        chal //= p
res *= d.get(chal, chal)
res %= N
print(res, chal)
s.sendall((str(res) + "\n").encode("ascii"))
print(recv(s))
print(recv(s))
