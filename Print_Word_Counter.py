times_looped = input('How many times would you liked your word looped? ')
word_inputed = raw_input('What word would you like printed? ')
x = 1
for count in range(times_looped):
    print ("%s #%d" % (word_inputed, x))
    x = x + 1
