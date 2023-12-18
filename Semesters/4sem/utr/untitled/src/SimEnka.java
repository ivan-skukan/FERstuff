import java.util.*;

public class SimEnka {

    private Set<String> alphabet;
    private Set<String> states;
    private Set<String> acceptStates;
    private String startState;
    private Map<String, Set<String>> transitions;

    private String[] toDo; //vjv ce trebat bit set il nes

    public SimEnka(Set<String> alphabet, Set<String> states, Set<String> acceptStates,
                               String startState, Map<String, Set<String>> transitions, String[] toDo) {
        this.alphabet = alphabet;
        this.states = states;
        this.acceptStates = acceptStates;
        this.startState = startState;
        this.transitions = transitions;
        this.toDo = toDo;
    }

    public Set<String> epsilon (Set<String> currentStates) {
        Boolean[] visited = new Boolean[currentStates.size()];
        Map<String, Boolean> mapOfVisited = new TreeMap<>(); //da stavim sva stanja i da je sve false?
        for(String s: this.states) mapOfVisited.put(s,false);
        boolean oneTransition = true;

        while(oneTransition) {
            oneTransition = false;
            Set<String> cscopy = new HashSet<>(currentStates);
            for(String s: cscopy) {
                String key = s + ",$";
                Set<String> newSet = transitions.get(key);
                if (newSet != null && mapOfVisited.get(s) == false) {
                    oneTransition = true;
                    currentStates.addAll(newSet);
                }
                mapOfVisited.put(s,true);
            }
        }
        return currentStates;
    }

    public String getNext(Set<String> currentStates, String[] sym,Set<String> newStates) {
        String result = "";
        Set<String> checkEpsilon = epsilon(new TreeSet<String>(currentStates)); //new hashset (currentstates)
        currentStates.addAll(checkEpsilon);
        boolean permanentBreak = false;
        boolean novoDodano;
        boolean prvaIteracija = true;
        for(String symbol : sym) {
            boolean isntHash = false;
            novoDodano = false;
            if(permanentBreak) {
                result = result + "#|";
                continue;
            }
            int i = 0;
             //PAZI NA JEDNAKOST!!!!
            Set<String> cscopy = new TreeSet<>(currentStates);
            Set<String> csnew = new TreeSet<>();
            for(String current : cscopy) {
                String key = current + "," + symbol;
                newStates = transitions.get(key);
                currentStates.remove(current);
                if(newStates != null) {
                    novoDodano = true;
                    isntHash=true;
                    csnew.addAll(newStates);
                }
                else {  //nekaj sa # valjda
                    if(novoDodano && !prvaIteracija) currentStates.remove(current);
                }

                prvaIteracija = false;
            }
            currentStates.addAll(csnew);
            if(isntHash) {
                checkEpsilon = epsilon(currentStates);
                currentStates.addAll(checkEpsilon);
                String tempString = new String();
                tempString = "";
                for(String s: currentStates) {
                    if(i==0) {i++; result = result + s;}
                    else result = result + "," + s;
                }

                result = result + "|" + tempString;
            }
            else {
                result = result + "#|";
                permanentBreak = true;
            }

        }
        return result.substring(0,result.length()-1);
    }

    public void doIt() {
        for (String set: this.toDo) {
            String[] sym = set.split(",");
            Set<String> currentStates = new TreeSet<>();
            currentStates.add(this.startState);
            Set<String> checkEpsilon = epsilon(new TreeSet<String>(currentStates));
            currentStates.addAll(checkEpsilon);
            Set<String> newStates = new TreeSet<>();
            String result1 = new String("");
            int i = 0;
            for(String s: currentStates) {
                if(i == 0) {
                    i++;
                    result1 = result1 + s;
                }
               else result1 = result1 + "," + s;
            }
            result1 = result1 +"|"+ getNext(currentStates,sym,newStates);

            System.out.println(result1);
        }
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        String[] toDo = scanner.nextLine().split("\\|"); //"\\|"?
        Set<String> states = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        Set<String> alphabet = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        Set<String> acceptStates = new HashSet<>(Arrays.asList(scanner.nextLine().split(",")));
        String start= scanner.nextLine();
        Map<String, Set<String>>  transitions = new HashMap<>();

        String line;
        while (scanner.hasNextLine() && !(line = scanner.nextLine()).isEmpty()) {
            String key = line.split("->")[0];
            String[] newSets = line.split("->")[1].split(",");
            if(!newSets[0].equals("#")) {
                Set<String> ns = new TreeSet<>(Arrays.asList(newSets));
                transitions.put(key,ns);
            }

        }

        SimEnka enka = new SimEnka(alphabet,states,acceptStates,start,transitions,toDo);

        enka.doIt();
    }
}


/* List<String> sortedList = new ArrayList<>(currentStates);
            Collections.sort(sortedList);
            currentStates.clear();
            currentStates.addAll(sortedList);*/