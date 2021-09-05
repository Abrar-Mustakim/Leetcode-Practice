#Sort an Array


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max = nums[0]
        for i in nums:
            if i>max:
                max = i 
            max = max+5       
        new_nums = [0]*((max*2)+1)
        
        for i in range(len(nums)):
            a = nums[i]+max
            
            new_nums[a]+=1 
            
        index = 0  
        for i in range(len(new_nums)):
            
            if new_nums[i] == 1:
                a = i - max 
                
                nums[index] = a 
                
                index +=1       
            elif new_nums[i] > 1:
                a = i - max 
                j = 0 
                while j < new_nums[i]:
                    
                    nums[index] = a 
                    index += 1 
                    j+=1           
        return nums
                    
###---------------------Basic COunting Sorting ------------------------  
                    
#Key Sorting
def key_sorting(s):
  
  max = s[0]
  print(s)
  for i in s:
    if i > max:
      max = i 
  new_s = [0] * (max+1)
  #print(new_s)
  for i in range(len(s)):
    a = s[i]
    new_s[a] += 1 
  #print(new_s)
  index = 0
  for i in range(len(new_s)):
    
    if new_s[i] == 1:
      s[index] = i 
      index+=1
    elif new_s[i] > 1:
      a = new_s[i]
      j = 0
      while j < a:
        s[index] = i
        index+=1
        j+=1
    


  print(s)

  a = 10
  if a > len(new_s):
    print("False")
  else:
    if new_s[a]!=0:
      print("True")
    else:
      print("False")

  


a = [6,6,5,1,8,2,6,8,3,8]
key_sorting(a)


def key_sort_neg(s):
  print(s)
  max = s[0]

  for i in s:
    if i > max:
      max = i 
    max = max+5

  max_len = (max*2) +1  

  new_s = [0]* max_len

  print(new_s)
  for i in range(len(s)):
    a = s[i]
    a = a + max 

    new_s[a] += 1
  print(new_s)


  index = 0 
  for i in range(len(new_s)):
    

    if new_s[i] ==1:
      i = i - max
      s[index] = i
      index += 1
    elif new_s[i] > 1:
      i = i - max
      s[index] = i
      index += 1 
    

  print(s)

  a = 10 

  a = a + max 
  if a>len(new_s):
    print("False")
  else:
    if new_s[a] > 0:
      print("True")
    else:
      print("False")






s=[-1,2,-8,-10]
key_sort_neg(s)


#OOP method

class KeyIndex:
  def __init__(self, array):
    self.s = array

  def key_sort(self):

    s = self.s


  
    self.max = s[0]

    for i in s:
      if i > self.max:
        self.max = i 

    max_len = (self.max*2) +1  

    self.new_s = [0]* max_len

    
    for i in range(len(s)):
      a = s[i]
      a = a + self.max 

      self.new_s[a] += 1
    


    index = 0 
    for i in range(len(self.new_s)):

      if self.new_s[i] == 1:
        i = i - self.max
        s[index] = i
        index += 1 
      elif self.new_s[i] > 1:
        a = self.new_s[i]
        i = i - self.max
        j = 0
        while j < a:
        
          s[index] = i
          index += 1
          j+=1

    return s

  def search(self, value):
    a = value
    a = a + self.max 
    if a>len(self.new_s):
      return "False"
    else:
      if self.new_s[a] > 0:
        return "True"
      else:
        return "False"
 

s=[-5,2,-1,5,3,5,2,8,2]
a = KeyIndex(s)
print(a.key_sort())
print(a.search(8))

                    
                    
