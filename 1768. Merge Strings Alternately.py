class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = [0] *(len(word1)+len(word2))
        if len(word1) == len(word2):
            even = 0
            odd = 1
            #word3[0]=word1[0]
            for i in range(0, len(word1)):
                word3[even] = word1[i] 
                word3[odd] = word2[i]
                odd += 2 
                even +=2
        if len(word1) < len(word2):
            a = len(word1)
            z=0
            even = 0
            odd = 1
            while z != a:
                word3[even] = word1[z] 
                word3[odd] = word2[z]
                odd += 2 
                even +=2 
                z+=1
            
            #d = len(word2) - len(word1) 
            e = word2[a:]
            f = 0
            for i in range(len(word3)):
                if word3[i]==0:
                    word3[i] = e[f]
                    f+=1             
        if len(word1) > len(word2):
            a = len(word2)
            z=0
            even = 0
            odd = 1
            while z != a:
                word3[even] = word1[z] 
                word3[odd] = word2[z]
                odd += 2 
                even +=2 
                z+=1
            
            #d = len(word2) - len(word1) 
            e = word1[a:]
            f = 0
            for i in range(len(word3)):
                if word3[i]==0:
                    word3[i] = e[f]
                    f+=1    
        word3 = "".join([str(i) for i in word3]) 
        return word3
