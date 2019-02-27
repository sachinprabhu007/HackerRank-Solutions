#Get the K groups and a list of all room numbers

k,fam_array = int(input()),list(map(int,input().split()))

#Get the unique set of room numbers
_set = set(fam_array)

#Multiply the sum of unique numbers by k (as if every room number was repeated k times).
#Subtract the sum of given room numbers. The difference will be (k-1)*captains_room_number. #Divide by (k-1) to get the captains room number

print(((sum(_set)*k)-(sum(fam_array)))//(k-1))



