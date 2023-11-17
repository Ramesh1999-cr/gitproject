#generator
def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

# Using the generator
squares = square_numbers(5)
print(next(squares))  # Output: 1
print(next(squares))  # Output: 4
print(next(squares))  # Output: 9
print(next(squares))  # Output: 16
print(next(squares))  # Output: 25



#decorator 

def uppercase_decorator(func):
    def wrapper(text):
        modified_text = text.upper()
        return func(modified_text)
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  # Output: Hello, JOHN!



# 3.map() function

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]


#4.palindrome

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


#5.prime  check


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(7))   # Output: True
print(is_prime(12))  # Output: False



#imp

# 6.Li = [22, 33, [22, 33, 5, 66], [22, 66, 88], 55]

def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

result_list = flatten_list(Li)
print(result_list)



# 7. "gggtttffoo"

def group_consecutive_characters(s):
    if not s:
        return []

    result = [[s[0]]]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            result[-1].append(s[i])
        else:
            result.append([s[i]])

    return result

G = "gggtttffoo"
output = group_consecutive_characters(G)
print(output)

#imp num 8
#[11,22,[33,55,5],[55,77,55,333],88]
#o/p [11,22,33,55,5,55,77,55,333,88]


def filter_li(l):
    add=[]
    for i in l:
        if isinstance (i,list):
            add.extend(i)
        
        else:
            add.append(i)
    return add

l=[11,22,[33,55,5],[55,77,55,333],88]
a=filter_li(l)
print(a)

  #o/p [11,22,33,55,5,55,77,55,333,88]




#lambda
letter=list(filter(lambda x:x,'human'))
print(letter)

#comprehension
letter=[x for x in range(20) if x%2==0]
print(letter)

#lambad
l=[1,65,89956,45564,645,2]
n=list(map(lambda x: x*2, l))
print(n)

#list
l=[32,23,233,222,32,12,23,34,101]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
#print(l[(: :-1)])

l=[2,23,3,3,33,32,213123,33]
l=list(dict.fromkeys(l))
print(l)

#NEW
class Student:
    def _init_(self):
        self.name="ramesh"
        self.id=98
    def display(self):
        print(self.name,self.id)
s=Student()
s.display()
#
s="ramesh"
s.split()
print(s.split())
print(s[1])
print(" ".join(reversed(s.split())))


#Turn every item of a list into its square
a=[1,2,3,4,5,6,7,8,9]
b=[x*x for x in a]
print(b)

# Concatenate two lists in the following order
a=["hello","take"]
b=["dear","sir"]
c=[a[0]+b[1],a[1]+b[1],a[1]+b[0]]
print(c)

#Iterate both lists simultaneously
a=[10,20,30,40]
b=[100,200,300,400]
for a,b in zip(a,b[::-1]):
    print(a,b)


    
#lastest number among list
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(z)
    
   # o/p:552


#ascending order
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(l)

#o/p:[2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 17, 19, 20, 27, 552]

    


#decendind order
l=[10,5,4,2,11,13,17,14,12,8,7,19,27,552,20]
i=0
for i in range(i,len(l)):
    #print(i)
    for j in range(i+1,len(l)):
        if (l[i]<l[j]):
            z=l[i]
            l[i]=l[j]
            l[j]=z
print(l)

#o/p:[552, 27, 20, 19, 17, 14, 13, 12, 11, 10, 8, 7, 5, 4, 2]


# which is higher number in list
l=[33,33,44,77,9,445,889]
largest=l[0]
for i in l:
    if i >largest:
       largest=i
print(i)

#give in list is which is higher number

l=[33,33,44,55,77,33,11,999,665,444]
i=0
for i in range(i,len(l)):
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            tem=l[i]
            l[i]=l[j]
            l[j]=tem
print(tem)
    
