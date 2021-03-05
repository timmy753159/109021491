import sys
from Myfun import fun
m=int(sys.argv[1])
n=int(sys.argv[2])


print(int(fun(m)/(fun(n)*fun(m-n))))