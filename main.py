def letter_index(x, y):
  alp = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
  index = [] # index of each replacement letter
  words = [] 
  for letter in x.lower(): 
    if letter in alp:
      s = alp.index(letter) # "original" index
      s += int(y)
      index.append(s % 26)
      
  for item in index:
    words.append(alp[item]) # change from index to letter
    
  return "".join(words) # return 

print('Caesar Cipher!\n')

phrase = input('Enter the phrase you would like to encrypt: ')

while True:
  number = input('\nEnter the number of the displacement: ')
  try:
    int(number)
    break
  except ValueError:
    print('Enter a valid number!')
    
print(f'\nThe encrypted word is: {letter_index(phrase, number)}\nEncryption code: {number}')