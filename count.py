# count.py
#
# 


strng = input("Input the string you want to count:")

chars = input("Input the characters you want to count:")

def Convert(chars, strng):
    count = 0
    for n in strng:
       if n in chars:
        count += 1
    return count



#print(Convert(chars))
print("The number of times", chars,"appears in", strng,"is",Convert(chars, strng),".")