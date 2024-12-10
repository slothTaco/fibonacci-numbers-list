#Input: Initialize the list 
fib_list = [1, 1]

#input: Initialize value, n
n = 10

#Generate: list of n fibonacci numbers
for number in range(2, n):
    
  #Calculate: next value
  next_value = fib_list[-1] + fib_list[-2]
  
  #Append: next value to the list
  fib_list.append(next_value)
  
#Output: print sequence
print(fib_list)
