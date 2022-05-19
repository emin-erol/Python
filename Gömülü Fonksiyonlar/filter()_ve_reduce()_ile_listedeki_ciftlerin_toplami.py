from functools import reduce
liste = [1,2,3,4,5,6,7,8,9,10]
a = list(filter(lambda x: x%2==0,liste))
print(reduce(lambda x,y: x+y,a))