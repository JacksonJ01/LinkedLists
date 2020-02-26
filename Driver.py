from LinkedList import *

Links = LinkedList()

print('We\'re gonna prepend 2, 1, and 0, in that order, then append 3.')
Links.add_head(2)
Links.add_head(1)
Links.add_head(0)
Links.add_end(3)
print(Links.dis_elm())

print('Now we\'re going to append 4 to the end')
Links.add_end(4)
print(Links.dis_elm())

print('I don\'t want this List to start with ')
print(Links.rem_front())
print(Links.dis_elm())

print(Links.search1(1))
print(Links.search2(2))

print('Let\'s remove 2:',
      f'\n{Links.remove1(2)}')
print(Links.display())

print('Now let\'s remove 3:',
      f'\n{Links.remove2(3)}')
print(Links.display())
