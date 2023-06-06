# # Objects of type dict are also like lists, but here instead of indexing using integers, indexing is done using keys.

# capitals = {'France': 'Paris', 'Italy': 'Rome', 'Japan':'Kyoto'}
# # for key in capitals:
# #  print('The capital of', key, 'is', capitals[key])

# # we can use items to retrieve both keys and values

# # for key, val in capitals.items():
# #     print(key,val)

# print(capitals, len(capitals),len(capitals["France"]))

# animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

# print(animals.keys(), animals.values())
# print(animals)



def lyrics_to_freq(lyrics):

    myDictionary = {}
    
    for word in lyrics:
        if word in myDictionary:
            myDictionary[word] +=1
        else:
            myDictionary[word] = 1
    return myDictionary

def most_common_word(freqs):

    values = freqs.values()
    most_common = max(values)
    words = []

    for k in freqs:
        if freqs[k] == most_common:
            words.append(k)
        print(words, most_common)



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


print(animals.values())
a = len(animals.values())
print(a)
def how_many(animals):
    a = len(animals.values())
    print(a)
# print(how_many(animals))
how_many({'B': [15], 'u': [10, 15, 5, 2, 6]})