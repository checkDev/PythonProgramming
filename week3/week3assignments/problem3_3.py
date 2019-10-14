def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    d = {1 : "January", 2 : "February" , 3 :"March" , 4 : "April", 5 : "May", 6 : "June" ,7 : "July" 
         , 8 : "August"
         ,9 : "September",10 : "October",11 : "November",12 : "December"}
    #print(d[month] ," ",)
    s = d[month] + " "+str(day)+", "+str(year)
    print(s) 
