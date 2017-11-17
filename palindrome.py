import csv

def baseN(num,b):
    # From the discussion here: http://code.activestate.com/recipes/65212/
    # This will convert from decimal integer to any base 
    if b > 36 or b < 2 or not isinstance(b, int):
        return 'Invalid Base'
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

def isPalindrome(s):
    # Check if a string is a reverse of itself
    if not isinstance(s, basestring):
        return False
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

            # Keep increasing base until palindrome is found, if none by 36 then not possible
            while not isPalindrome(baseN(i,base)) and base <= 36:
                base = base + 1

            # write the output to csv
            writer.writerow({
                "decimal": i, 
                "base": isPalindrome(baseN(i,base)) and base or '-', 
                "palindrome": isPalindrome(baseN(i,base)) and baseN(i,base) or '-'
            })

if __name__ == '__main__':
    output()
