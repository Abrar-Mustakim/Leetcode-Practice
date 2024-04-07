//https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/?envType=study-plan-v2&envId=binary-search
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        int ans=INT_MAX;

        while(low<=high){
            int mid = low+(high-low)/2;
            if(nums[low]==nums[mid] && nums[mid]==nums[high]){
                if(nums[mid]<ans) ans=nums[mid];
                low++;
                high--;
                continue;
            }
            
            //left sorted
            if(nums[low]<=nums[mid]){
                if(nums[low]<ans) ans=nums[low];
                low = mid+1;
            }

            //right sorted
            else{
                if(nums[mid]<ans) ans=nums[mid];
                high = mid-1;
            }
        }
        return ans;
        
    }
};