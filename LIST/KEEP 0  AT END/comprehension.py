numbers = [0, 1, 0, 3, 12]
res =[i for i in numbers if i!=0] +[i for i in numbers if i==0]
print(res)