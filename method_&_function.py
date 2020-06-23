import math

# Create a simple list
lst = [1,2,3,4,5]

lst.append(6)
print("list",lst)

# Check how many times 2 shows up in the list
print("count",lst.count(2))

###############################################


def greeting(name):
    print('Hello %s' %(name))
greeting('KoKhant')


def add_num(num1,num2):
    return num1+num2
add_num(3,4)
#or
result = add_num(3,4)
print(result)


def is_prime(num):
    '''    method of checking for primes.   '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

is_prime(17)


def is_prime1(num):
    '''    Better method of checking for primes.    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

print(is_prime1(18))


###################################################################

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))


def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Crazy Kangaroo'))


#capital letter
def old_helloworld(name):
    if len(name) > 5:
        return name[:5].capitalize() + name[5:].capitalize()
    else:
        return 'Name is too short!'

print(old_helloworld("helloworld"))


#counting primenumber
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in primes:  # primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))


#map function
mynames = ['Banyar','Kitty','Fatty','Kalay']
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]

print(list(map(splicer,mynames)))

name = 'This is a global name'


#nested statement
def greet():
    name = 'Maung Myint'

    def hello():
        print('Hello ' + name)
    hello()

greet()



#kwargs
def myfunc(*args, **kwargs):
    if 'fruit' in kwargs:
        print(f"I like {' and '.join(args)} but My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")

myfunc('orange', fruit='apple')
myfunc()



