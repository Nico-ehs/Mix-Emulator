



## done 0   8-23
## non in 1.0:  34-38  48-55
## INC? =
## DEC? =
## ENT? =
## ENN? =

# primes fraction
# at every 10

# 1 at ram 1001
# 0 at ram 1000

rA=0

r = ram 2000+ 

add 1 to rA
check prime
if prime: add to primes 


if %1000 =0
r=r+ "p/n"

fn_1: 'uses rA '

1 data[2] to rA
2 ADD data[1]
3 rA to data[2]
'1 to 3: add 1 to n and rA=n'
4 JMP to check prime(fn_2)    rA to 1=prime 0=notprime
'check if n n is prime by fn_2 and if yes rA=1 else rA=0'
5 ADD data[3]
6 rA to data[3]
7 data[2] to rA
8 SUB data[4]
9 JMP_testx rA f=0 to 1
10 END 

data:
1 to_word(1) 'constant 1'
2 to_word(0) '# fn on : n'
3 to_word(0) '# of primes'
4 to_word(10000) 'numbers to test'


fn_2: 'input in rA' start at x1

0 'rA = input'
1 STJ m=data[1] 
2 SUB (1)
3 JMP_testx rA==0 to end
4 ADD (1)
'2-4 if 1 then output not prime'
5 STA m=data[2]
6 LD1 m=data[6]
7 LDA m=data[4]
8 STA m=data[5]
9 LDA m=data[5]
10 JMP_testx rA<=0 to isprime




JMP to 10


notprime STZ m=data[6]
JMP to end

isprime  LDA m=data[4]
ADD m=data[3]
STA m=data[4]



end LDA m=data[6]
JMP m=data[1]


LDA m=data[x]
ADD m=data[3]
STA m=data[x]
'add 1 to x'
LDA m=data[x]
SUB m=data[3]
STA m=data[x]
'subtract 1 to x'



x rA=1
JMP

data: starts at
1 (0)   'jump back adress'  
2 (0)   'input'
3 (1)   'constant 1'
4 (0)    '# saved primes'
5 (0)    '# primes left to test'
6 (1)   'output'
x1: 6 to 6+n [(2)]



'x0 if rA <2 jump to x2'
SUB (2)
JMP_testx rA>=0 to x4
ADD (2)
rA to data[1]
'x1 if d[4]<=d[3] jump to '
 d[4] to rA
 SUB d[3]
 JMP_testx rA f= to 1
'x1.5'
## if d[1]<d[6+d[4]] JMP to x4
'x2 if '
' else d[4]++'
data[1] to rA
d[4] to I1
d[6+i1] to d[2]
## ?=rA%
JMP_testx ? f= to 1
JMP to x1
'x3 prime=0'
(0) to rA
reset data 'exept d[3] d[x1]'
JMP to fn call
'x4 prime=1'
d[5] to rA
reset data 'exept d[3] d[x1]'
JMP to fn call


data: starts at
1 ()  
2 () 
3 ()   'saved primes '
4 ()   'primes tested'
5 (1)   'output
x1: 6 to 6+n [(2)]


at 100000
8*5

10 10 10

10000

at every 10

convert
    