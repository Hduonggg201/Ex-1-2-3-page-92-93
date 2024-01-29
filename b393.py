import time

tb = time.time()

n = 0

s = 0

x = int(input())

while x > 0:

    n = n + 1

    s = s + x

    x = int(input())

if n > 0 : 
    print("Trung bình cộng: ", s/n)

print("\nTime: %.4f sec"%(time.time()-tb))