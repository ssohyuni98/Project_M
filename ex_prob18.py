num_list = [1,2,3,4,5]

for i in range(len(num_list)+1):
    print(" ".join(map(str,num_list[0:i])))