my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list2 = []

for i in my_list:
    my_list2 = my_list.count(i)
    if i > 1:
        del my_list[i]
print ("Elements únics:",str(my_list[-2])+" i "+str(my_list[-1]))

print("La llista amb elements únics: ",my_list2-1)
