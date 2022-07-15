import random
when=["a few years ago", "yesterday", "last night", "a long time ago", "on 20th of october"]
who=["cat", "mouse", "elephant", "dog", "rabbit"]
name=["yazan", "mohammed", "maryam", "ahmed", "yousef"]
residence=["palictine", "UAE", "saudi arabia", "egypt"]
went=["school", "cenima", "home", "laundry", "seminar"]
happened=["made lots of friends", "ate a burger", "finds a secret key", "brought a book", "solved a mystrey"]
print(random.choice (when)+','+ random.choice (who)+' that lived in '+ random.choice (residence)+',went to the '+ random.choice (went)+' and '+ random.choice (happened))