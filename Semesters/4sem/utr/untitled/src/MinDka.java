import java.util.*;
public class MinDka {
    private List<String> alphabet;
    private List<String> states;
    private List<String> acceptStates;
    private String startState;
    private Map<String, String> transitions;
    public MinDka(List<String> alphabet, List<String> states, List<String> acceptStates,
                   String startState, Map<String, String> transitions) {
        this.alphabet = alphabet;
        this.states = states;
        this.acceptStates = acceptStates;
        this.startState = startState;
        this.transitions = transitions;
    }

    public void minimize() {

    }
    public void doIt(MinDka dka) {
        //first we eliminate unreachable states
        boolean stopChecking = false;

        while(stopChecking == false) {
            stopChecking = true;
            boolean hasTransition = false;

            for(String state : states) {
                List<String> keySet = transitions.keySet().stream().toList();
                for(String key: keySet) {
                    String checkState = transitions.get(key);
                    if(checkState.equals(state)) {
                        hasTransition = true;
                    }
                }
                if(hasTransition == false) {
                    stopChecking = false;
                    transitions.remove(state);
                }
            }
        } //this should work?
        System.out.println("before minimize");
        minimize();
        MinDka minimized = dka;
        String firstLine = new String("");
        for(String state: minimized.states) {
            firstLine = firstLine+state+",";
        }
        System.out.println(firstLine.substring(0,firstLine.length()-1));
        String secondLine = new String("");
        for(String letter : minimized.alphabet) {
            secondLine = secondLine+letter+",";
        }
        System.out.println(secondLine.substring(0,secondLine.length()-1));
        String thirdLine = new String("");
        for(String accept : minimized.acceptStates) {
            thirdLine = thirdLine+accept+",";
        }
        System.out.println(thirdLine.substring(0,thirdLine.length()-1));
        System.out.println(minimized.startState);
        Set<String> keySet = minimized.transitions.keySet();
        for(String key:keySet) {
            System.out.println(key+"->"+minimized.transitions.get(key));
        }
    }
    //this code is made to minimize a given DKA
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        List<String> states = new ArrayList<>(Arrays.asList(scanner.nextLine().split(",")));
        List<String> alphabet = new ArrayList<>(Arrays.asList(scanner.nextLine().split(",")));
        List<String> acceptStates = new ArrayList<>(Arrays.asList(scanner.nextLine().split(",")));
        String start= scanner.nextLine();
        Map<String, String>  transitions = new HashMap<>();

        String line;
        while (scanner.hasNextLine() && !(line = scanner.nextLine()).isEmpty()) {
            String key = line.split("->")[0];
            String newState = line.split("->")[1];
            transitions.put(key,newState);
        }

        MinDka dka = new MinDka(alphabet,states,acceptStates,start,transitions);
        dka.doIt(dka);
    }
}

/*
        while(true) {
            Set<List<String> newPartitions = new ArrayList<>();

            for(List<String partition: partitions) {
                for(String symbol : alphabet) {
                    Set<List<String> symbolPartitions = new ArrayList<>();
                    for (String state: partition) {
                        List<String tranSet = transitions.get(state);
                        for(List<String p : partitions) {
                            if(p.containsAll(tranSet) && tranSet.containsAll(p)) {
                                symbolPartitions.add(p);
                                break;
                            }
                        }
                    }

                    if(symbolPartitions.size()>1) {
                        for (List<String newPartition : symbolPartitions) {
                            newPartitions.add(newPartition);
                        }
                    }

                    newPartitions.remove(partition);
                    break;
                }
            }
        }*/
