# ~~~~~~ X and Y + functions ~~~~~~

x = 6
y = 10
list_global = (x, y)


def min(x, y):
    print(sorted(list_global)[0])

def multiply(x, y):
    print(x * y)

def pow(x, y):
    print(x ** y)

def divmod(x, y):
    print (x // y)

# ~~~~~~ Values List + functions~~~~~~
values_list = [15125,404,42131245,200902,4215,41,51,5215252136,24]


def max(values_list):    
    print(sorted(values_list)[-1])


def len(values_list):
    string = values_list
    a=0
    for number in string:
        a=a+1 
        print(a)


# ~~~~~~ Calling Functions ~~~~~~


min(x, y)
max(values_list)
multiply(x, y)
pow(x, y)
divmod(x, y)
len(values_list)