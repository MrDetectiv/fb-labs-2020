package AffineCipher;

import RuLanguage.Alphabet;

import java.util.*;

public class BigramTextHandler {
    private HashMap<String, Integer> bigramFrequency;
    private String text;

    public BigramTextHandler(String text) {
        this.text = text;
        this.bigramFrequency = new HashMap<>();
    }


    private void insert(String bigram, HashMap<String, Integer> lst) {
        if ( lst.get(bigram) == null ) {
            lst.put(bigram, 0);
        }
        lst.put(bigram, lst.get(bigram) + 1);
    }

    public HashMap<String, Integer> getBigramFrequency() {
        return bigramFrequency;
    }

    public String getText() {
        return text;
    }

    public void setBigramFrequency(HashMap<String, Integer> bigramFrequency) {
        this.bigramFrequency = bigramFrequency;
    }

    public void countFrequency() {
        int n = text.length();

        if ( n % 2 != 0 ) {
            n -= 1;
        }

        for (int i = 0; i < n; i += 2) {
            String bigram = new String();

            bigram += text.charAt(i);
            bigram += text.charAt(i+1);

            this.insert(bigram, this.bigramFrequency);
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

    public String[] getLastNKeys(int n) {
        String[] result = new String[n];

        for ( int i = 1; i <= n; i++ ) {
            result[i-1] = (String) this.bigramFrequency.keySet().toArray()[this.bigramFrequency.size() - i];
        }
        return result;
    }

}
