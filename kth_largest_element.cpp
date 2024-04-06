//https://leetcode.com/problems/kth-largest-element-in-an-array/
//Problem solved using Priority Queue



#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        priority_queue<int> q;
        for(auto i:nums){
            q.push(i);
        }
        int value;
        for(int i=0;i<k;i++){
            value = q.top();
            q.pop();
            
        }

        return value;
        
    }
};


//Min Heap


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        priority_queue<int, vector<int>, greater<int>> q;
        for(auto i:nums){
            q.push(i);
            if(q.size()>k){
                q.pop();
            }

        }
        return q.top();
        
    }
};