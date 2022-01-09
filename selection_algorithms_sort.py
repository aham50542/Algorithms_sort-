#الترتيب يكون تنازلي
def selection (s_list):
    for i in range (0,len(s_list)):
        min_value = s_list[i]
        for j in range (0,len(s_list)):
            if s_list[i]< s_list[j] :
                s_list[i] ,s_list[j]=s_list[j], s_list[i]
    return s_list
print (selection([3,2,4]))