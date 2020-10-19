# Write a function that returns how many times each letter appears in a string

# Ex: input: 'aaabbc'

#a : 3
#b : 2
#c : 1

def letter_count(string):
  #create an empty dict
  d = {}
  #loop through the string
  for char in string:
    #have we seen this char before?
    #i.e. does it exist in our dict?
    if char in d:
      # the char exists, simply increment its value in the dictionary
      d[char] +=1
    else:
      # it does not exist! Let's add it to our dict
      d[char] = 1
    
    return d

def print_sorted_letter_count(string):
  # get the sorted_dict
  d = letter_count(string)
  # print the items out in alphabetical order
  # Convert the Dict into a list of its key values
  items = list(d.items())
  print(items)

  items.sort(key=lambda item: item[0].lower(), reverse=True)

  for i in items:
        print(f'{i[0]}: {i[1]}')


# # print(letter_count("The quick brown fox jumps over the lazy dogs"))
print_sorted_letter_count("The quick brown fox jumps over the lazy dogs")
