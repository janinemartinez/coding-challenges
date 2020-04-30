# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def threesnfives(limit):

    collector = []

    # for i in range(0, limit, 3):
    #     collector.append(i)

    # for i in range(0, limit, 5):
    #     collector.append(i)

    collector.extend(range(0, limit, 3))
    collector.extend(range(0, limit, 5))

    collector = set(collector)

    return sum(collector)

# print(threesnfives(1000))

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def next_num(to):

    old_current = 0
    current = 1
    next_current = 1

    while current < to:
        yield current
        next_current = old_current + current
        old_current = current
        current = next_current

# print(sum([num for num in next_num(4000000) if num % 2 == 0]))

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def largest_p(num):
    remainder = num
    for i in range(2, num):
        while remainder != 1 and remainder % i == 0:
            remainder //= i
        if remainder == 1:
            return i
    return num
    
    #     if remainder == 1:
    #         return num
    #     else:
    #         if remainder%i == 0:
    #             remainder = remainder//i
    #             print("remainder", remainder)
    #             if remainder == 1:
    #                 print("done")
    #                 return factor
    #             else:
    #                 factor = i
    #                 print("factor", factor)
    #                 largest_p(remainder)


# print(largest_p(600851475143))


# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_pal(pow):

    top_range = 10**pow-1
    bot_range = 10**(pow-1)
    pal = 0

    for i in range(top_range, bot_range, -1):
        for j in range(i, bot_range, -1):
            if pal < j*i:
                s = str(int(i*j))
                if s == s[::-1]:
                    pal = int(i*j)
    return pal

# print(largest_pal(3))


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def div_by_all(rng):

    current = rng

    while True:
        for i in range(1, rng+1):
            if current%i == 0:
                if i == rng:
                    return current
                else:
                    continue
            else:
                current+=rng
                break

print(div_by_all(20))