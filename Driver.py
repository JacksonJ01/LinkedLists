from LinkedList import *
import time
time.sleep(2.5)

Links = LinkedList()

print('We\'re gonna prepend 2, 1, and 0, in that order, then append 3.')
Links.add_head(2)
Links.add_head(1)
Links.add_head(0)
Links.add_end(3)
print(Links.dis_elm())

print('\nNow we\'re going to append 4 to the end')
Links.add_end(4)
print(Links.display())

print('\nI don\'t want this List to start with 0, so I\'ll remove it')
print(Links.rem_front())
print(Links.display())

print("\nLet's search the LinkedList if we have a 4 in the list and return a boolean value:"
      f"\n{Links.search1(4)}")
print("Now let's search the LinkedList if we have a 3 in the list and return a boolean value:"
      f"\n{Links.search2(3)}")

print("\nAlright, lettuce remove them")
print('Let\'s remove 2 first:',
      f'\n{Links.remove1(2)}')
print(Links.display())

print('\nNow let\'s remove 3:',
      f'\n{Links.remove2(3)}')
print(Links.display())

print('Okay, let\'s remove 4:',
      f'\n{Links.remove1(4)}')
print(Links.display())

Links.add_end(4)
print('Okay, let\'s remove 4:',
      f'\n{Links.remove2(4)}')
print(Links.display())

print('Okay, let\'s remove 1:',
      f'\n{Links.remove1(1)}')
print(Links.display())

Links.add_head(1)
print('Okay, let\'s remove 1:',
      f'\n{Links.remove2(1)}')
print(Links.display())

print("\nThe remove code doesn't work the way it should,"
      " so I'm going to delete all the nodes and start over, with more Links:")
Links.clear_all()

add = 0
while add < 11:
    Links.add_end(add)
    add += 1

print(Links.dis_elm())

print("\nAlright, lettuce remove them")
print('Let\'s remove 10 first:',
      f'\n{Links.remove1(10)}')
print(Links.display())

print('\nNow let\'s remove 3:',
      f'\n{Links.remove2(0)}')
print(Links.display())

print('\nOkay, let\'s remove 4:',
      f'\n{Links.remove1(9)}')
print(Links.display())

print('\nOkay, let\'s remove 1:',
      f'\n{Links.remove1(1)}')
print(Links.display())

Links.clear_all()

print("\nHello world")
print(Links.display())

print("Seems like everything is working a-okay"
      "\nNow it's your turn, no more watching me")
print("\nI'm going to take you to the interface now, but before i do that.."
      "\n This is what the interface will look like:"
      "\n- PREPEND,(type pre)"
      "\n- APPEND, (type app)"
      "\n- REMOVE FORM HEAD, (type rh)"
      "\n- REMOVE FROM END, (type re)"
      "\n- REMOVE A VALUE, (type r)"
      "\n- SEARCH LIST, (type S)"
      "\n- DISPLAY LIST, (type d)"
      "\n- CLEAR ALL, (type CLEAR ALL)"
      "\n- EXIT, (type EXIT)")

input("Got it?"
      "\n\n\n\nPRESS ENTER")

Links.interface()
