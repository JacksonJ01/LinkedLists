from TailLinked import *
TailLinks = LinkedListTail()

i = 10
while i > -1:
    print(TailLinks.add_head(i))
    i -= 1
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


TailLinks.clear_all()


i = 0
while i < 11:
    print(TailLinks.add_tail(i))
    i += 1
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove_head())
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove_tail())
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


i = 0
while i < 11:
    print(TailLinks.search(i))
    i += 1
print('\n\n')


i = 0
while i < 11:
    print(TailLinks.seek(i))
    i += 1
print('\n\n')


TailLinks.clear_all()


i = 5
while i > -1:
    print(TailLinks.add_head(i))
    i -= 1
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


i = 6
while i < 11:
    print(TailLinks.add_tail(i))
    i += 1
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(0))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(1))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(2))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(5))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(8))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(9))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')


print(TailLinks.remove(10))
print(TailLinks.display())
print(TailLinks.show_ht())
print('\n\n')
