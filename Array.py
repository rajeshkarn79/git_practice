import array

my_array = array.array("i",[12,89,90,223])

# print("array : ",my_array)

#Search Element
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i

    return "Not_Found"

a= linear_search(my_array, 2)
print(a)