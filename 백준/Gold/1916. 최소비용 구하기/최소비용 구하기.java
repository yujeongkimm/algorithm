import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        ArrayList<ArrayList<City>> costs = new ArrayList<>();

        // 초기화
        for(int i=0; i<N+1; i++) {
            costs.add(new ArrayList<>());
        }

        for(int i=0; i<M; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            int cost = sc.nextInt();
            costs.get(start).add(new City(end, cost));
        }

        int ans_f = sc.nextInt();
        int ans_t = sc.nextInt();

        int ans = bfs(ans_f, ans_t, costs, N);

        System.out.println(ans);
    }

    static int bfs(int start, int end, ArrayList<ArrayList<City>> costs, int length) {
        PriorityQueue<City> pq = new PriorityQueue<>();
        boolean[] visited = new boolean[length+1];
        pq.add(new City(start, 0));

        while(!pq.isEmpty()) {
            City now = pq.poll();
            visited[now.node] = true;

            if (now.node == end) {
                return now.cost;
            }

            for(City next : costs.get(now.node)) {
                if(!visited[next.node])
                    pq.add(new City(next.node, now.cost + next.cost));
            }

        }

        return -1;
    }

    static class City implements Comparable<City>{
        int node;
        int cost;

        public City(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }

        @Override
        public int compareTo(City c) {
            return this.cost - c.cost;
        }
    }
}