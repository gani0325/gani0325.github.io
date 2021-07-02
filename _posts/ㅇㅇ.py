def main() :
    numYearBase10 = 2021
    numYearBase8 = 3733
    numYearBase16 = 0x7DB

    print("Year by base 10 : %d, by base 8: %d, by base 16 : %d"%(numYearBase10, numYearBase8, numYearBase16))
    numComplex1 = complex(3, 4)
    numComplex2 = 4+3j

    print("Complex value : ", numComplex1)
    print("Absolute value : ", abs(numComplex2))
    print("Real value : ", numComplex2.real)
    print("Image value : ", numComplex2.imag)

    strDeptName = ("Industrial & System Engineering")
    strUnivName = ("KAIST")
    print("Department : ", strDeptName)
    print("Full name of dept : ", strDeptName, ", ", strUnivName)

main()    
