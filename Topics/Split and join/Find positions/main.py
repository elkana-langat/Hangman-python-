number_list = input().split(" ")
number = int(input())

length = len(number_list)

counter = 0
for i in range(length):
    if int(number_list[i]) == number:
        counter += 1
        print(i)

if counter == 0:
    print("not found")