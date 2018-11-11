
def print_product(i,j):
    print(str(i) + "*" + str(j) + "=" + str(i * j))

n =3
print("Instance of a for loop based solution:")
for i in range(1,n+1):

    for j in range(1,n+1):
        print_product(i, j)

print("Instance of a while loop based solution:")
i=1
while i<=n:
    j=1
    while j<=n:
        print(str(i) + "*" + str(j) + "=" + str(i * j))
        j+=1
    i+=1