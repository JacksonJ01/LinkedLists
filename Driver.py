from LinkedList import *

Links = LinkedList()

# Links.add_end(3)
Links.add_head(2)
Links.add_head(1)
Links.add_head(0)
Links.add_end(3)
Links.display()

Links.add_end(4)
Links.display()

print(Links.rem_front())
