class Solution {
    public int solution(int n) {
        int answer = 1;
        for (int i = 1; i<=11; i++) {
            answer *= i;
            if (answer > n) {
                return i-1;
            }
        }
        return 1;
    }
}