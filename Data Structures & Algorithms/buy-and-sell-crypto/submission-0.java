class Solution {
    public int maxProfit(int[] prices) {
        int day=0;
        int maxProfit = 0;
        for(int i=1; i<prices.length; i++){
            if(prices[day] > prices[i]){
                day = i;
            }
            else {
                if(maxProfit < prices[i]-prices[day]){
                    maxProfit = prices[i] - prices[day];
                }
            }
        }
        

        return maxProfit;
        
    }
}
