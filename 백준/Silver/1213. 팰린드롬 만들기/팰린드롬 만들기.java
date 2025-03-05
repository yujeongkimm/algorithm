import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        int[] alphaCount = new int[26];
        for(int i=0; i<s.length(); i++) {
            alphaCount[s.charAt(i) - 'A']++;
        }

        // 알파벳 홀수 개수 찾기
        int isOdd = 0;
        for(int i=0; i<26; i++) {
            if(alphaCount[i]%2==1)
                isOdd++;
        }

        String ans = "";
        StringBuilder sb = new StringBuilder();
        if(isOdd>1) {
            System.out.println("I'm Sorry Hansoo");
        } else {
            // 아니면 팰린드롬 만들기
            // 머리 만들기 : alphabet 처음부터 /2 만큼 출력하기
            for(int i=0; i<26; i++) {
                for(int j=0; j< alphaCount[i]/2; j++)
                    sb.append((char)(i+65));
            }

            ans += sb.toString();
            String end = sb.reverse().toString();

            // 중간 만들기 = 홀수 개수 찾기
            for(int i=0; i<26; i++) {
                if(alphaCount[i]%2 == 1) {
                    ans += (char)(i+65);
                }
            }
            System.out.println(ans + end);

        }
    }

}