import java.util.Arrays;

class Solution {
    public int solution(int[] priorities, int location) {
        int arrow = 0, cnt = 0;
        
        int [] clone = priorities.clone(); 
        Arrays.sort(clone);
        while (true) {
            if (clone[priorities.length - 1 - cnt] == priorities[arrow]) {
                priorities[arrow] = 0;
                cnt += 1;
                if (arrow == location)
                    return cnt;
            }
            arrow += 1;
            arrow %= priorities.length;
        }
    }
}