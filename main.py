def letter_index(x, y):
  alp = 'abcdefghijklmnopqrstuvwxyz'
  index = [] # index of each replacement letter
  words = [] 
  for letter in x.lower(): 
    if letter in alp:
      s = alp.index(letter) # "original" index
      s += int(y)
      index.append(s % 26)
      
  for item in index:
    words.append(alp[item]) # change from index to letter
    
  return "".join(words) # return of the 'encrypted' sentence

print('Caesar Cipher!\n')

phrase = input('Enter the sentence you would like to encrypt: ')

while True:
  number = input('\nEnter the number of the displacement: ')
  try:
    int(number)
    break
  except ValueError:
    print('Enter a valid number!')
    
print(f'\nThe encrypted sentence is: {letter_index(phrase, number)}\nEncryption code: {number}')