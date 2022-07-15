import random
when=["a few weeks ago", "before 2 days", "last weekend", "a while ago", "on 8th of november"]
who=["snake", "rat", "horse", "spider", "bunny"]
name=["yazan", "mohammed", "maryam", "ahmed", "yousef"]
residence=["syria", "india", "iraq", "iran"]
went=["school", "mall", "his house", "park"]
happened=["made lots of friends", "ate a burger", "finds a secret key", "brought a book", "solved a mystrey"]
print(random.choice (when)+', '+ random.choice (who)+' that lived in '+ random.choice (residence)+', went to the '+ random.choice (went)+' and '+ random.choice (happened))