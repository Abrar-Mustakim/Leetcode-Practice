#without using recursion
def binary_search(array, data):
  l = 0
  r = len(array)-1 

  while l <= r:

    mid = (l+r)//2

    if data == array[mid]:
      return mid 

    elif data > array[mid]:
      l = mid+1 

    else:
      r = mid-1

  return -1






a = [5,9,17,23,25,45,59,63,71,89]
print(binary_search(a, 59))



#Using Recursion

def binary_search(array, l, r, data):


  while l <= r:

    mid = (l+r)//2

    if data == array[mid]:
      return mid 

    elif data > array[mid]:
      return binary_search(array, mid+1, r, data) 

    else:
      return binary_search(array, l, mid+1, data) 

  return -1






a = [5,9,17,23,25,45,59,63,71,89]
l = a[0]
r = len(a)-1
print(binary_search(a, l, r, 63))





#Leetcode solutions search a 2d matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            
            l = 0
            r = len(i)-1 
            
            while l <=r:
                mid = (l+r)//2
                
                if target == i[mid]:
                    return True 
                
                elif target > i[mid]:
                    l = mid+1 
                    
                else:
                    r = mid-1 
                    
        return False
        
