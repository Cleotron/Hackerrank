def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return "YES"
    
    if x1 < x2 and v1 < v2:
        return "NO"
    
    while x1 < 100000000 and x2 < 100000000:
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    print(kangaroo(0,3,4,2)) #Yes
    print(kangaroo(0,2,5,3)) #No
    print(kangaroo(21,6,47,3)) #No