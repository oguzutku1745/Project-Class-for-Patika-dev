a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten_a = lambda a:[e for l in a for e in flatten_a(l)] if type(a) is list else [a]

print(flatten_a(a))



