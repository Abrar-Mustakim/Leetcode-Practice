//https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=binary-search
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low=0;
        int high = nums.size()-1;
        int mid;
        
        while(low<=high){
            mid = (low+high)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]>target) high=mid-1;
            else low=mid+1;
            
        }
        if(mid==0&&nums[mid]<target) return mid+1;
        else if(nums[mid]<target) return mid+1;
        return mid;
        
    }
};