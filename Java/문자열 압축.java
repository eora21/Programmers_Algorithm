class Solution {

    public int count_ans(int cnt, int ans, String now) {
        if (cnt != 1)
            while (cnt > 0) {
                ans++;
                cnt /= 10;
            }
        ans += now.length();

        return ans;
    }

    public int solution(String s) {
        String before = "", now = "";
        int cnt = 1, ans, min_ans = s.length();

        for (int i = 1; i < s.length() / 2 + 1; i++) {
            ans = 0;
            cnt = 1;
            before = s.substring(0, i);

            for (int j = 2; i * j <= s.length(); j++) {
                now = s.substring(i * (j - 1), i * j);

                if (now.equals(before))
                    cnt++;
                else {
                    ans = count_ans(cnt, ans, now);
                    before = now;
                    cnt = 1;
                }
            }

            ans = count_ans(cnt, ans, now);
            ans += s.length() % i;

            if (min_ans > ans)
                min_ans = ans;
        }
        return min_ans;
    }
}