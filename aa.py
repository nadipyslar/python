#path = r'/Users/franz/Desktop/python/dz4.py'
#data = 'всем мир'
#with open (path,'w', encoding='UTF-8') as file:
#    new_file=file.write(data)
#переписывает файл. path , 'r' - read

#path = r'/Users/franz/Desktop/python/dz4.py'
#data = 'всем мир'
#with open (path,'r', encoding='UTF-8') as file:
#    new_file=file.readlines()
#    for i in range (len(new_file)):
#            new_file[i]=int(new_file[i][:-2])  #такая 2 убирает 2 символа с конца, команда .strip уберет из строки все раб символы типа слэшей и точек

#my_list=[1,2,3,5,1,3,10]
#my_list=list(filter(lambda x : my_list.count(x)==1, my_list)) #count подсчитывает вхожд элемента в список
#print(my_list)