//https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int low=0;
        int high = nums.size()-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(nums[mid]==target){
                return true;
            }
            //check if mid is equal of low and high
            else if(nums[mid]==nums[low]&&nums[mid]==nums[high]){
                low++;
                high--;
                continue;
            }
           //left sorted
            else if(nums[low]<=nums[mid]){
                if(nums[low]<=target && nums[mid]>target){
                    high = mid-1;
                }else low=mid+1;
            }
           //right sorted
           else{
            if(nums[high]>=target&&nums[mid]<target) low=mid+1;
            else high=mid-1;
           }
        }
        return false;      
    }
};