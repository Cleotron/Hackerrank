def sherlockAndAnagrams(s):
    result = 0

    for i in range(0, len(s)-1):
        for z in range(1, len(s)):
            dict_1 = {}
            for x in s[i:i+z]:
                if x in dict_1:
                    dict_1[x] += 1 
                else:
                    dict_1[x] = 1
            print('dict_1: ', dict_1) 
            for j in range(i, len(s)-z):
                dict_2 = {}
                for y in s[j+1:j+z+1]:
                    if y in dict_2:
                        dict_2[y] += 1 
                    else:
                        dict_2[y] = 1  
                print('dict_2: ', dict_2) 
                if dict_1 == dict_2:
                    result +=1
        print('result: ', result)
    print('final', result)

if __name__ == '__main__':
    sherlockAndAnagrams("kkkk")