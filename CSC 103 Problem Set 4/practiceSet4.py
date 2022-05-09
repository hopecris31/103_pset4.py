#Hope Crisafi
#5/2/2021
#Practice Set 4

#NJW 17/20

#Problem 1

#NJW DO NOT comment out answers to my questions please.

# word = 'Monty Python'
# lengthWord = len(word)
# lastLetter = word[lengthWord -1]

# print('first character is', word[0])
# print('the last character is', word[-1])
# print('the last character is still', lastLetter)
# print('the sliced version is', word[:5])



#Problem 2

# word = 'homebody'
# home = word[:4]
# body = word[4:]

# print(home)
# print(body)



#Problem 3

# word = input('enter a string:')
# length = len(word)
# stringHalf = length // 2 #indexes the middle letter of str

# if length % 2 == 0:
#     print('first half is:',word[:stringHalf])
#     print('second half is:',word[stringHalf:])

# else:
#     print('the middle character is:', word[stringHalf])
#     print('the first even half is:',word[:stringHalf])
#     print('the second even half is:',word[-stringHalf:])



#Problem 4

# word = input('enter a word:')
# replaceWith = input('enter a letter to replace:')
# atIndex  = input('enter an index point:')
# index = int(atIndex)

# newWord = word[:index] + replaceWith + word[index+1:]
# print(newWord)



#Problem 5

# sent = input('enter a sentence:')
# wordList = sent.split()
# end = len(sent)
# newSent = sent.replace(wordList[0],'z')

# #print(sentSplit)

#NJW It explictly tells you NOT to use methods. (-3)

# #sentSplit.replace(sentSplit[0],'z')
# print(wordList)
# print(newSent)



#Problem 6

transactions = int(input('enter transaction number:'))
transactionsDone = 0




while transactionsDone <= transactions:
    itemPrice = float(input('Item Price: '))
    tax = 0.07 * itemPrice
    totalPlusTax = tax + itemPrice
    #subtotal = totalPlusTax 
    transactionsDone += 1

    print('subtotal: ','{:.2f}'.format(totalPlusTax))
    print('total:', totalPlusTax[itemPrice] )
    
