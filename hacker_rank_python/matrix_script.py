''' 
Linear search example 
Time complexity O(n)
'''


def search_item(array_list, search_element):
    found = False
    for i in range(len(array_list)):
        if array_list[i] == search_element:
            found = True
            print(f"Element {search_element} found at position {i+1}")
            break
    if found == False:
        print(f"{search_element} is not found in the array list")


if __name__ == "__main__":
    array = [4, 2, 8, 9, 3, 7]
    search_element = 9
    search_item(array, search_element)

'''
output: 
Element 9 found at position 4  
'''