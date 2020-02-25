from LinkedList import *

Links = LinkedList()

# Links.add_end(3)
Links.add_head(2)
Links.add_head(1)
Links.add_head(0)
Links.add_end(3)
print(Links.display())

Links.add_end(4)
print(Links.display())

print(Links.rem_front())
print(Links.display())

print(Links.search1(1))
print(Links.search2(2))

print(Links.remove(2))
print(Links.display())
