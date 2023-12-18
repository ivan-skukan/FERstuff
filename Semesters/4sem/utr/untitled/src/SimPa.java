
import java.util.*;

public class SimPa {

    private Set<String> alphabet;
    private Set<String> states;
    private Set<String> stackAlphabet;
    private Set<String> acceptStates;
    private String startState;
    private String startStack;
    private Map<String, String> transitions;

    private String[] toDo;

    public SimPa(Set<String> alphabet, Set<String> states, Set<String> stackAlphabet, Set<String> acceptStates
            , String startState, String startStack, Map<String, String> transitions, String[] toDo) {
        this.alphabet = alphabet;
        this.states = states;
        this.stackAlphabet = stackAlphabet;
        this.acceptStates = acceptStates;
        this.startState = startState;
        this.startStack = startStack;
        this.transitions = transitions;
        this.toDo = toDo;

        this.task();
    }

    public String currentStatusString(String currentState, String forPrint, boolean printEps) {
        String result = "";
        result += currentState + "#";
        StringBuilder sb = new StringBuilder(forPrint);
        if (!printEps) {
            String[] print = sb.reverse().toString().split(" ,");
            for(String s : print) {
                result += s;
            }
        } else {
            result += "$";
        }
        return result;
    }

    public String doTransition(Stack<String> stack, String currentState, String[] sym) {
        String result = "";
        boolean inputAccepted = true;
        boolean valid;
        boolean printEps;
        boolean epsilonFirst;
        String symbol;
        int i = 0;
        symbol = new String(sym[i]);
        while(i<sym.length || !acceptStates.contains(currentState)) {
            epsilonFirst = false;
            printEps = false;
            valid = true;

            if(!stack.isEmpty()) {
                String stackTop;

                stackTop = stack.peek();
                String key = currentState + "," + symbol + "," + stackTop;
                String key2 = currentState + "," + "$" + "," + stackTop;

                if (transitions.get(key) != null || transitions.get(key2) != null) {
                    String nextStackSym = new String("");
                    String nextState;

                    if(transitions.get(key) != null && !epsilonFirst) {
                        nextStackSym = transitions.get(key).split(",")[1];
                        nextState = transitions.get(key).split(",")[0];
                        currentState = new String(nextState);
                    } else {

                        nextStackSym = transitions.get(key2).split(",")[1];
                        nextState = transitions.get(key2).split(",")[0];
                        currentState = new String(nextState);
                        epsilonFirst = true;
                    }

                    if (nextStackSym.length() >= 2) {
                        stack.pop();
                        StringBuilder sb = new StringBuilder(nextStackSym);
                        sb.reverse();
                        nextStackSym = new String(sb);
                        for(Character c: nextStackSym.toCharArray()) {
                            stack.push(c.toString());
                        }
                    } else if (stackTop.equals(nextStackSym)) {
                        //radi nista?
                    } else {
                        if(!stack.isEmpty()) {
                            stack.pop();
                            if (stack.isEmpty()) {
                                printEps = true;
                            }
                        } else valid = false;

                    }
                } else {
                    if(!symbol.equals("$")) valid = false;
                    else break;
                }
            } else valid = false;


            //System.out.println(stack.peek());
            if (valid) {
                //Stack<String> newStack = (Stack<String>)stack.clone();
                String forPrint = stack.toString().substring(1,stack.toString().length()-1);
                result += currentStatusString(currentState, forPrint, printEps) + "|";

            } else {
                result += "fail|";
                inputAccepted = false;
                break;
            }
            if(!epsilonFirst) i++;
            if(i < sym.length) {
                symbol = new String(sym[i]);
            } else {
                symbol = new String("$");
            }

        }

        if (acceptStates.contains(currentState) && inputAccepted) {
            result += "1\n";
        } else {
            result += "0\n";
        }

        return result;
    }

    public void task() {
        String result = new String("");
        for (String set : this.toDo) {
            String[] sym = set.split(",");
            Stack<String> stack = new Stack<>();
            stack.push(startStack);
            //System.out.println(stack.peek());
            String currentState = new String("");
            //Set<String> newStates = new TreeSet<>(); //necessary??
            currentState += startState;

            result += startState + "#" + startStack + "|";
            result += doTransition(stack, currentState, sym);

        }
        System.out.println(result);
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String[] toDo = scanner.nextLine().split("\\|"); //????
        Set<String> states = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        Set<String> alphabet = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        Set<String> stackAlphabet = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        Set<String> acceptStates = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        String start = scanner.nextLine();
        String startStack = scanner.nextLine();
        Map<String, String> transitions = new HashMap<>();

        String line;
        while (scanner.hasNextLine() && !(line = scanner.nextLine()).isEmpty()) {
            String key = line.split("->")[0];
            String newState = line.split("->")[1];
            transitions.put(key, newState);
        }

        SimPa simpa = new SimPa(alphabet, states, stackAlphabet, acceptStates, start, startStack, transitions, toDo);

    }
}
