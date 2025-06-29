class Solution {
    public int maxProfit(int[] prices) {
        int answer = 0;

        for(int i=0; i<prices.length-1; i++) {
            for (int j=i+1; j<prices.length; j++) {
                if (prices[i] < prices[j]) {
                    // maximum size 기록
                    answer = Math.max(answer, prices[j] - prices[i]);
                }
            }
        }

        return answer;
    }
}