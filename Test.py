word_inputed = raw_input('What word would you like printed 10 times? ')
x = 1
for count in range(10):
    print ("%s #%d" % (word_inputed, x))
    x = x + 1
