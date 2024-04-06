class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {        
        vector<int> ans(2);
        int lower_bound = -1;
        int upper_bound=-1;
        
        //lower bound
        int low=0;
        int high=nums.size()-1;
        while(low<=high){
            int mid=(low+high)/2;
            if(nums[mid]==target){
                lower_bound=mid;
                high=mid-1;
            }
            if(nums[mid]>=target){
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
       

        //upper bound
        int low_1=0;
        int high_1 = nums.size()-1;
        while(low_1<=high_1){
            int mid_1=(low_1+high_1)/2;

                if(nums[mid_1]==target){
                    
                    upper_bound=mid_1;
                    low_1 = mid_1+1;
                }
                

            if(nums[mid_1]>target){
                high_1=mid_1-1;

            }else{
                low_1=mid_1+1;
            }
        }
        ans[0]=lower_bound;
        ans[1]=upper_bound;
        return ans;


        
    }
};
