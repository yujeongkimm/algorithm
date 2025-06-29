class Solution {
    public int majorityElement(int[] nums) {
        // length/2 보다 많이 나온 element return

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int num : nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        int n = nums.length/2;

        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > n) {
                return entry.getKey();
            }
         }

         return 0;

    }
}