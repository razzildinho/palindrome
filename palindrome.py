import csv

def baseN(num,b):
    if b > 36:
        return 'Invalid Base'
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

def isPalindrome(s):
    if not isinstance(s, basestring):
        return False
    return s == s[::-1]

def output():
    with open('output.csv' , 'w') as csvfile:
        fieldnames = ["decimal", "base", "palindrome"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1,1001):
            base = 2
            while not isPalindrome(baseN(i,base)) and base <= 36:
                base = base + 1
            writer.writerow({
                "decimal": i, 
                "base": isPalindrome(baseN(i,base)) and base or '-', 
                "palindrome": isPalindrome(baseN(i,base)) and baseN(i,base) or '-'
            })

if __name__ == '__main__':
    output()
