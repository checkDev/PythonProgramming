def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    myList = []
    for i in range(0, 10 ,1):
        randomfloat = random.random() * 5
        #print(randomfloat)
        randomfloat += 30
        #print("now", randomfloat)
        myList.append(randomfloat)
    print(myList)
