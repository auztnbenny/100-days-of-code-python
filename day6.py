#To find the sum of elements  in an array and multiply it with the length of the array
def sum_multiply(arr):
    total_sum=sum(arr)
    length=len(arr)
    result=total_sum*length
    return result
user_input=input("Enter the array:")
if user_input:
    array = list(map(int, user_input.split()))
    result=sum_multiply(array)
    print("result is:",result)
else:
    print("no input provided")



