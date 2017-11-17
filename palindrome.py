import csv

def baseN(num,b):
    # From the discussion here: https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base
    # This will convert from decimal integer to any base

    # Base needs to be at least 2 and args need to be integers
    if not isinstance(num, int):
        raise Exception('Invalid integer')
    if not isinstance(b, int) or b < 2:
        raise Exception('Invalid base')

    digits = []
    while num > 0:
        digits.insert(0, num % b)
        num = num // b
    return digits

def isPalindrome(s):
    # Check if an array or string is a reverse of itself
    if not isinstance(s, list):
        raise Exception('Invalid argument')
    return s == s[::-1]

def output():
    with open('output.csv' , 'w') as csvfile:

        fieldnames = ["decimal", "base", "palindrome"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Loop from 1 to 1000
        for i in range(1,1001):

            # Start at base 2 and increase as needed
            base = 2

            # Keep increasing base until palindrome is found
            while not isPalindrome(baseN(i,base)):
                base = base + 1

            # write the output to csv
            writer.writerow({
                "decimal": i, 
                "base": base, 
                "palindrome": '-'.join([str(x) for x in baseN(i,base)])
            })

if __name__ == '__main__':
    output()
