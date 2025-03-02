import java.util.*;
import java.io.*;

class Main {

    // 이상 값 처음 나오는 위치
    static int findLowerBound(int[] cards , int target) {
        int l = 0, r = cards.length - 1;
        int lowerBound = cards.length;

        while (l<=r) {
            int m = (l+r)/2;

            if (target > cards[m]) {  // 필요없는 값
                l = m + 1;
            } else {
                lowerBound = m;
                r = m-1;
            }
        }
        return lowerBound;
    }

    // 초과값 처음 나오는 위치
    static int findUpperBound(int[] cards, int target) {
        int l = 0, r = cards.length-1;
        int upperBound = cards.length;
        while(l<=r) {
            int m = (l+r)/2;

            if (cards[m] <= target) {
                l = m+1;
            } else {
                r = m-1;
                upperBound = m;
            }
        }
        return upperBound;
    }

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] cards = new int[N];
        for (int i=0; i<N; i++) {
            cards[i] = sc.nextInt();
        }

        Arrays.sort(cards);

        int M = sc.nextInt();
        int[] targets = new int[M];
        for(int i=0; i<M; i++) {
            targets[i] = sc.nextInt();
        }

        BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i=0; i<M; i++) {
            bw.write(findUpperBound(cards, targets[i]) - findLowerBound(cards, targets[i]) + " ");
        }
        bw.write("\n");
        bw.flush();
    }
}