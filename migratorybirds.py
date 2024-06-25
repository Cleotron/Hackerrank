def migratoryBirds(l):
    bird_dict = {}
    for elem in l:
        if elem not in bird_dict:
            bird_dict[elem] = 1
        else:
            bird_dict[elem] += 1
    temp = max(bird_dict.values())
    id_list = [key for key in bird_dict if bird_dict[key] == temp]
    return min(id_list)

if __name__ == '__main__':
    print(migratoryBirds([1,1,2,2,3])) #1
    print(migratoryBirds([1,4,4,5,3])) #4