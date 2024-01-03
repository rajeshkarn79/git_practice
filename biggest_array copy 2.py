array_=[1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 0, 12, 11, 121, 12, 89, 12, -1, -9, -8, -7, -100, 12, 23]

# def find(list_):
#     biggest_number = list_[0]
#     for index in range(0, len(list_)):
#         if list_[index] < biggest_number:
#             biggest_number = list_[index]
    
#     print(biggest_number)

# find(array_)


def find(list_):
    biggest_number = list_[0]
    for index in range(0, len(list_)):
        if list_[index] > biggest_number:
            biggest_number = list_[index]
    
    print(biggest_number)

find(array_)