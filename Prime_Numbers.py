my_list = list(range(0,100))

#4 filtering prime numbers
my_list=list(filter(lambda x:x%2!=0,my_list))
print(list(my_list))
fp = open("primes.txt","a")

for num in my_list:
    for i in range(2,num-1):
        if (num%i == 0):
                break

    else:
        fp.write("\n{}".format(str(num)))

fp.close()

#5  using context manager
with open("prime1.txt","a") as fp:
    for num in my_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            fp.write("\n{}".format(str(num)))

#6 reading from the text file
with open("prime1.txt","r")as fp:
    print(fp.read())