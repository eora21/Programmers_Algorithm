import java.util.ArrayList;

class Solution {
    public int solution(String s) {
        ArrayList AL = new ArrayList();
        for (int i = 0; i < s.length(); i++) {
            if (!AL.isEmpty() && AL.get(AL.size() - 1).equals(s.charAt(i)))
                AL.remove(AL.size() - 1);
            else
                AL.add(s.charAt(i));
        }

        return AL.size() > 0 ? 0 : 1;

    }
}