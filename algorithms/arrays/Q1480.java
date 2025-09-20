class Solution {
    public int[] runningSum(int[] nums) {
        int i,currSum=0;
        int[] retArray = new int[nums.length];
        for(i=0;i<nums.length;i++){
            currSum+=nums[i];
            retArray[i]=currSum;
        }
        return retArray;
    }
}