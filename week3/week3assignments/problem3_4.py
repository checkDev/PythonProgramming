def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    d = {"1" : "January", "2" : "February" , "3" :"March" , "4" : "April", "5" : "May", "6" : "June" 
         ,"7" : "July" 
         , "8" : "August"
         ,"9" : "September","10" : "October","11" : "November","12" : "December"}
    getKey =0;
    for key,value in d.items():
        if value == str(mon):
            getKey = key
            break
    
            
    s = str(getKey) + "/"+ str(day)+"/"+str(year)
    print(s) 
