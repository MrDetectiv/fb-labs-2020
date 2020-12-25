package AffineCipher;

import java.util.*;

public class MonogramTextHandler {
    private HashMap<String, Integer> monogramFrequency;
    private String text;

    public MonogramTextHandler(String text) {
        this.text = text;
        this.monogramFrequency = new HashMap<>();
    }


    private void insert(String bigram, HashMap<String, Integer> lst) {
        if ( lst.get(bigram) == null ) {
            lst.put(bigram, 0);
        }
        lst.put(bigram, lst.get(bigram) + 1);
    }

    public HashMap<String, Integer> getMonogramFrequency() {
        return monogramFrequency;
    }

    public String getText() {
        return text;
    }

    public void setMonogramFrequency(HashMap<String, Integer> monogramFrequency) {
        this.monogramFrequency = monogramFrequency;
    }

    public void countFrequency() {
        int n = text.length();

        for (int i = 0; i < n; i++) {
            String bigram = new String();
            bigram += text.charAt(i);

            this.insert(bigram, this.monogramFrequency);
        }
    }

    public LinkedHashMap<String, Integer> sortHashMapByValues(
            HashMap<String, Integer> passedMap) {
        List<String> mapKeys = new ArrayList<>(passedMap.keySet());
        List<Integer> mapValues = new ArrayList<>(passedMap.values());
        Collections.sort(mapValues);
        Collections.sort(mapKeys);

        LinkedHashMap<String, Integer> sortedMap =
                new LinkedHashMap<>();

        Iterator<Integer> valueIt = mapValues.iterator();
        while (valueIt.hasNext()) {
            int val = valueIt.next();
            Iterator<String> keyIt = mapKeys.iterator();

            while (keyIt.hasNext()) {
                String key = keyIt.next();
                int comp1 = passedMap.get(key);
                int comp2 = val;

                if (comp1 == comp2) {
                    keyIt.remove();
                    sortedMap.put(key, val);
                    break;
                }
            }
        }
        return sortedMap;
    }

    public String getLastKey() {
        return (String) this.monogramFrequency.keySet().toArray()[this.monogramFrequency.size()-1];
    }

    public String getFisttKey() {
        return (String) this.monogramFrequency.keySet().toArray()[0];
    }
}
