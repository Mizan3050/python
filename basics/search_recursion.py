#IMPLEMENT SEARCH AND FIBONACCI (WITH BOTH NORMAL AND RECURSIVE DICT)

#SEARCH WITH RECURSION
a_List = [0,3]
def binary_search(search_list,number_to_search):
    high = len(search_list)-1
    low = 0
    mid = int((high+low)/2)
    print(search_list)
    if(mid <= 1 and number_to_search!=search_list[0]):
        print("number does not exist in the List")
    if(search_list[mid] == number_to_search):
        print("Search number found at found", mid)
    while(search_list[mid]!=number_to_search and mid>1 and mid <= high):
        print('Mid -', mid, 'High -',high, 'Low -', low )
        if(number_to_search > search_list[mid]):
            low = mid
            mid = int((high+low)/2)
        else:
            high = mid
            mid = int((high+low)/2)
    print("Search number found at", mid)

def sort_and_search():
        a_List.sort()
        binary_search(a_List, int(number_to_search))

number_to_search = input('Enter a number to search: ')
sort_and_search()

