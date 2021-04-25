# here we create the initial list from the input, please do not modify this line
x = json.loads(input())
el = []
a = []

els = [el for a in x for el in a if el > 0]
