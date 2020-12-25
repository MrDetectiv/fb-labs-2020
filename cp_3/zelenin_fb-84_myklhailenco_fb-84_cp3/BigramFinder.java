package com.company;

import java.util.*;

public class BigramFinder {
    public static float bigram(String clear) {
        char[] charArray = clear.toCharArray();
        Map<String, Float> count = new HashMap<String, Float>();
        for (int i = 0; i < clear.length() - 1; ++i) {
            char s = charArray[i];
            char sOne = charArray[i + 1];
            String bigram = String.valueOf(s) + sOne;
            if (count.containsKey(bigram)) {
                count.put(bigram, count.get(bigram) + 1);

            } else {
                count.put(bigram, (float) 1);
                i++;
            }
        }
        count.entrySet().stream().sorted(Map.Entry.<String, Float>comparingByValue().reversed());
        String[] arr1 = new String[count.size()];
        String[] arr2 = new String[count.size()];
        Set entries = count.entrySet();
        Iterator entriesIterator = entries.iterator();
        int i = 0;
        while(entriesIterator.hasNext()){
            Map.Entry mapping = (Map.Entry) entriesIterator.next();
            arr1[i] = mapping.getKey().toString();
            arr2[i] = mapping.getValue().toString();
            i++;
        }
        for (int j = 0; j < count.size(); j++) {
            System.out.print(arr1[j]);
            System.out.println("=" + arr2[j]);
        }
        return 0;
    }

}
