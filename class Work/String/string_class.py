import re
ade = "pawpaAw is a kind of fruit12344"
result =r"[a-z0-9]+"
print(re.match(result,ade))
