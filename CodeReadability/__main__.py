from CodeReadability.finder import *


p1 = P('Don', 16)
p2 = P('Sally', 50)

finder = Finder()
yng = finder.find([p1, p2])

print('youngest')
print(yng)

