def pop(x):
    print(x)

    prodList = []

    for i in x:
        prod = 1

        for j in x:
            if j != i:
                prod *= j

        prodList.append(prod)

    print(prodList)

# Defining main function
def main():

    test1 = [1,2,4,6]
    pop(test1)

    test2 = [-1,0,1,2,3]
    pop(test2)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()