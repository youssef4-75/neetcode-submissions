class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i, j;
        int[] answer = {-1, -1};
        for (i=0; i<nums.length - 1; i++){
            for (j=i+1; j<nums.length; j++){
                if (nums[i] + nums[j] == target){
                    answer[0] = i;
                    answer[1] = j;
                    return answer;
                }
            }
        }

        return answer;
    }
}
