def sorting(Numbers_list):
    i = 0
    while (i < len(Numbers_list)):
    
        j = 0

        while (j <= len(Numbers_list)-2):
    
            if(Numbers_list[j] > Numbers_list[j+1]):
                temp = Numbers_list[j+1]
                Numbers_list[j+1] = Numbers_list[j]
                Numbers_list[j] = temp

            j += j + 1
        i += 1
    return Numbers_list

def list_add(list_size):

    count = 0
    Numbers_list = []

    while (count < list_size):
        print("Enter a number: ")
        number = int(input())
        Numbers_list.append(number)
        count += 1
    print("List: ", Numbers_list)
    return Numbers_list

print("Type the size of the list: ")
list_size = int(input())

Numbers_list = list_add(list_size)

print("Sorted list: ", sorting(Numbers_list))