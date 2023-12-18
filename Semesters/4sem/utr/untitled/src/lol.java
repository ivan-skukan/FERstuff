import java.util.*;

public class lol {

    static boolean isSorted(List<Integer> list) {
        for(int i = 1; i < list.size(); i++) {
            if(list.get(i) < list.get(i-1))
                return false;
        }
        return true;
    }

    public static void main(String args[]) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(2);
        list.add(1);
        for(int i = 3; i < 12; i++) {
            list.add(i);
        }

        do {
          Collections.shuffle(list);
        } while(!isSorted(list));

        System.out.println("lol");
    }
}
