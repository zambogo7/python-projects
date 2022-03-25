# A python program to implement bubble sort


numbers=[8,7,6,4,5,3,9,1]

def bubble_sort(numbers):
    has_swapped=True
    no_of_iteration=0
    while has_swapped:
        has_swapped=False
        for number in range(len(numbers)-no_of_iteration-1):
            #compare the number from index 0 to 0+1
            if numbers[number]>numbers[number+1]:
                #swap using
                numbers[number],numbers[number+1]=numbers[number+1],numbers[number]
                #or
                #temp=numbers[number]
                #numbers[number]=numbers[number+1]
                #numbers[number+1]=temp
                has_swapped=True
                no_of_iteration+=1


    return numbers

#bubble_sort(numbers)

print(f"the unsorted list is \n{numbers}")
print(f"The sorted list is \n{bubble_sort(numbers)}")

