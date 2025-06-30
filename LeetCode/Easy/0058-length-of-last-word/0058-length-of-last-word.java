class Solution {
    public int lengthOfLastWord(String s) {
        String[] st = s.split(" ");

        String str = st[st.length-1];

        return str.length();

    }
}