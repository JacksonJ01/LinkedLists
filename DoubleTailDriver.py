from DoubleTailLinked import *
TLinks = DoubleLinkedListTail()

i = 10
while i > 5:
    print(TLinks.add_head(i))
    print(TLinks.show_ht())
    i -= 1
print(TLinks.display())
print(TLinks.display_bk())
print("\n\n")


print(TLinks.clear_all())


i = 0
while i < 6:
    print(TLinks.add_tail(i))
    print(TLinks.show_ht())
    i += 1
print(TLinks.display())
print(TLinks.display_bk())
print('\n\n')


print(TLinks.clear_all())


i = 0
while i < 11:
    print(TLinks.add_tail(i))
    print(TLinks.show_ht())
    i += 1
print(TLinks.display())
print(TLinks.display_bk())
print('\n\n')


i = -2
while i < 13:
    print(TLinks.seek(i))
    i += 1
print("\n\n")


i = -2
while i < 13:
    print(TLinks.search(i))
    i += 1
print('\n\n')


print(TLinks.remove_head())
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove_tail())
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove(1))
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove(2))
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove(4))
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove(6))
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove(8))
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove(9))
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')


print(TLinks.remove_tail())
print(TLinks.display())
print(TLinks.display_bk())
print(TLinks.show_ht())
print('\n\n')
