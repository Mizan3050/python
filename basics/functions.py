#BINARY SEARCH!!
a_List = [0,3,4,55,44,67,23,43,5,65,32,12,17,75,18,28,9,2]
def binary_search(search_list,number_to_search):
    search_list.sort()
    high = len(search_list)-1
    low = 0
    mid = int((high+low)/2)
    print(search_list)
    if(mid < 1 and number_to_search!=search_list[0]):
        print("number does not exist in the List")
    if(search_list[mid] == number_to_search):
        print("Search number found at found", mid)
    while(search_list[mid]!=number_to_search and mid!=0):
        print(mid)
        if(number_to_search > search_list[mid]):
            low = mid
            mid = int((high+low)/2)
        else:
            high = mid
            mid = int((high+low)/2)
    print("Search number found at", mid)

number_to_search = input('Enter a number to search: ')
binary_search(a_List, int(number_to_search))