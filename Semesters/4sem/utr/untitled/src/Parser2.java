import java.util.*;

public class Parser2 {

    private static LinkedList<String> symbols = new LinkedList<>();
    private static int i = 0;
    private static String result = new String("");
    private static String ulaz = new String("");

    public static void tryGetNext() {
        if(i < symbols.size() - 1) {
            i++;
            ulaz = symbols.get(i);
        } else ulaz = "f";
    }

    static boolean A() {
        boolean accepted = true;

        result += "A";

        if(ulaz.equals("a") && (i+1) <= symbols.size()) {
            tryGetNext();
            return true;
        }
        else if(ulaz.equals("b") && (i+1) <= symbols.size()) {
            tryGetNext();
            accepted = C();
        } else return false;

        return accepted;
    }

    static boolean B() {
        boolean accepted = true;

        result += "B";

        if(ulaz.equals("c")) {
            tryGetNext();
            if(!ulaz.equals("c")) return false;
            tryGetNext();
            accepted = S();

            if(accepted) {
                if(!ulaz.equals("b")) return false;
                tryGetNext();
                if(!ulaz.equals("c")) return false;
                tryGetNext();
            } else return false;
        }

        return true;
    }

    static boolean C() {
        boolean accepted = true;

        result += "C";

        accepted = A();
        if(accepted) accepted = A();
        else return false;

        return accepted;
    }

    static boolean S() {
        boolean accepted = true;
        boolean callOne = true;
        boolean callTwo = true;

        result += "S";

        if(ulaz.equals("a") ) {
            tryGetNext();
            callOne = A();
            if (callOne) callOne = B();
            else return false;
        } else if(ulaz.equals("b")) {
            tryGetNext();
            callTwo = B();
            if(callTwo) callTwo = A();
            else return false;
        } else return false;

        return accepted && callOne && callTwo;
    }

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        String in = s.nextLine();

        for(Character c: in.toCharArray()) {
            symbols.add(c.toString());
        }

        boolean accepted;
        ulaz = symbols.get(i);
        accepted = S();
        System.out.println(result);
        if(i == symbols.size()-1 && accepted) System.out.print("DA");
        else System.out.print("NE");

    }
}
