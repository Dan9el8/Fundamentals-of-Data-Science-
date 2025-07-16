#Loops are fundamentals to programming because we can step through list or other data structures methodollogies, one element at a time
#for loop can be used to loop through a list or dictionary
list = [1,2,3,4]
for element in list:
    print(element)

    for i in range(len(list)):
        print(i)

        for index, element in enumerate(list):
            print(index, element)