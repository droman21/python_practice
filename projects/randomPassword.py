import random

uppercaseLetter=chr(random.randint(65,90))

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(0,9))
digit2=chr(random.randint(0,9))
punctuationSign1=chr(random.randint(33,38))
punctuationSign2=chr(random.randint(33,38))

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)

print(password)