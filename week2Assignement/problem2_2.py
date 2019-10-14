alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):
    print(my_list)
    print(my_list[0])
    print(my_list[len(alist)-1])
    
    newList =[]
    for i in range(3, 5):
        newList.append(my_list[i])
    print (newList)
        #print(my_list[i] , end =" ") 
    #print( )
    newList1 =[]
    for i in range(0,3):
         newList1.append(my_list[i])
    print (newList1)
       # print(my_list[i] , end =" ") 
    #print( )
    newList2 =[]
    for i in range(3,len(alist)):
        newList2.append(my_list[i])
    print (newList2)
    print(len(my_list))  #6 
    my_list.append('z') #7
    print(my_list)
