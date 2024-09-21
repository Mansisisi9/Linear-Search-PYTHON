arr=[]
n=int(input("Enter the number of elements you want in your Array: "))
for i in range(n):
 arr.append(int(input(f"Enter Element {i+1}: ")))
# Print the elements of the arrayse that are parated by commas
print(*arr, sep=",")
value=int(input("Enter the element you want to find in your array:"))
# Perform Linear Search
count=0
for i in range(n):
 if arr[i]==value:
  count+=1
  break
if count==1:
 print(f"The index at which {value} can be found is {i}")
else:
 print("Element cannot be found in the Array")