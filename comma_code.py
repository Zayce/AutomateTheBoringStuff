spam = ['apples', 'bananas', 'tofu', 'cats', 'girl', 'feminine', 'bob', 'bangs']
for i in range(len(spam) - 2):
    print(spam[i], end =', ')
print(spam[-2], end =' ')
print('and ' + spam[-1])