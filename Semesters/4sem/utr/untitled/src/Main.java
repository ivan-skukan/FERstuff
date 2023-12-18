import java.util.*;

public class Main {

    public static void dfs(Set<String> visited, Map<String,String> transitions, String state,List<String> alphabet) {
        if (visited.contains(state)) return;
        visited.add(state);

        for(String symbol : alphabet) {
            String newState = transitions.get(state + "," + symbol);
            dfs(visited,transitions,newState,alphabet);
        }
    }

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

        Set<String> visited = new HashSet<>();

        dfs(visited,transitions,start,alphabet);
        List<String> copyStates = new ArrayList<>(states);
        for(String s : copyStates) {
            if(!visited.contains(s)) states.remove(s);
        }

        List<List<String>> partitions = new ArrayList<>();
        List<String> nonAccept = new ArrayList<>();

        for(String s : states) {
            if(!acceptStates.contains(s)) nonAccept.add(s);
        }

        partitions.add(acceptStates);
        partitions.add(nonAccept);

        /*while(true) {
            boolean change = false;
            int counter = 0;

            for(List<String> list : partitions) {
                int removed = 0;

                for(String elem : list) {
                    int i = 0;
                    int length = list.size()-list.indexOf(elem) - removed;

                    boolean first = true;
                    String temp[] = new String[] {""};

                    for(int j = 0; j < length; j++) {
                        int k = list.indexOf(list.indexOf(i)+1+i-removed);
                        i++;

                        for (String symbol : alphabet) {
                            Set<String> keys = transitions.keySet();

                        }
                    }
                }
            }
        }*/

        Map<String,Boolean> pairs = new TreeMap<>();
        for(String state1 : states) {
            for(String state2: states) {
                if(!state1.equals(state2) && !(pairs.containsKey(state1+","+state2) || pairs.containsKey(state2+","+state1))) {
                    if((acceptStates.contains(state1) && acceptStates.contains(state2)) || (!acceptStates.contains(state1) && !acceptStates.contains(state2))) {
                        pairs.put(state1+","+state2,true);
                    } else
                        pairs.put(state1+","+state2,false);
                }
            }
        }

        Map<String,Set<String>> pairToPairs = new TreeMap<>();

        for(String pair : pairs.keySet()) {
            for(String symbol : alphabet) {
                String state1 = pair.split(",")[0];
                String state2 = pair.split(",")[1];
                String newState1 = transitions.get(state1+","+symbol);
                String newState2 = transitions.get(state2+","+symbol);

                if(newState1.compareTo(newState2)>0) {
                    String temp = new String(newState1);
                    newState1 = new String(newState2);
                    newState2 = new String(newState1);
                }

                boolean same = state1.equals(newState1) && state2.equals(newState2) || state1.equals(newState2) && state2.equals(newState1)
                                || newState2.equals(newState1) && (state1.equals(newState1)|| state2.equals(newState1));

                if(!same) {
                    if(pairs.get(newState1+","+newState2) != null && pairs.get(newState1+","+newState2) == true) {
                        pairToPairs.get(newState1+","+newState2).add(state1+","+state2);
                    } else {
                        pairs.put(state1+","+state2,false);
                        if(pairToPairs.containsKey(state1+","+state2)) {
                            Set<String> toChange = new TreeSet<>(pairToPairs.get(state1+","+state2));
                            for(String str : toChange) {
                                pairs.put(str,false);
                            }
                        }
                    }
                }
            }
        }

        for(String pair : pairs.keySet()) {
            if(pairs.get(pair) == true) {
                String str1 = pair.split(",")[0];
                String str2 = pair.split(",")[1];
                if(str1.compareTo(str2) < 0) {
                    states.remove(str2);
                    transitions.remove(str2);
                    if(acceptStates.contains(str2)) acceptStates.remove(str2);
                } else {
                    states.remove(str1);
                    transitions.remove(str1);
                    if(acceptStates.contains(str1)) acceptStates.remove(str1);
                }
            }
        }
        String line1 = new String("");
        for(String state : states) {
            line1 = line1 + state + ",";
        }
        line1 = line1.substring(0,line1.length()-2);
        System.out.println(line1);

        line1 = new String("");
        for(String symbol : alphabet) {
            line1 = line1 + symbol + ",";
        }
        line1 = line1.substring(0,line1.length()-2);
        System.out.println(line1);

        line1 = new String("");
        for(String accept : acceptStates) {
            line1 = line1 + accept + ",";
        }
        line1 = line1.substring(0,line1.length()-2);
        System.out.println(line1);

        System.out.println(start);

        for(String string : transitions.keySet()) {
            String transition = new String("");
            transition = string + "->" + transitions.get(string);
        }
    }
}
