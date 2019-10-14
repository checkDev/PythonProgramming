def problem2_7():
    """ computes area of triangle using Heron's formula. """
    xstr = input ("Enter length of side one:")
    x = float(xstr)
    ystr = input ("Enter length of side two:")
    y = float(ystr)
    zstr  = input ("Enter length of side three:")
    z = float(zstr)
    area = 0.0
    s = 0.5* (x + y +z )
    area = s *(s- x) *(s -y ) *(s -z )
    area = area**0.5
    print("Area of a triangle with sides" ,x ,y,z,"is" ,area)
