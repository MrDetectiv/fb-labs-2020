package com.company;

import java.util.HashMap;

public class INDEX {
    String alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
    float count = 0;
    float ind = 0;
    INDEX(String txt) {
        for (int a = 0; a < alph.length(); a++) {
            char letter = alph.charAt(a);
            HashMap<Character, Integer> map = new HashMap<Character, Integer>(40);
            for (int i = 0; i < txt.length(); ++i) {
                char c = txt.charAt(i);
                if (Character.isLetter(c)) {
                    if (map.containsKey(c)) {
                        map.put(c, map.get(c) + 1);
                    } else {
                        map.put(c, 1);
                    }
                }
            }
            if (map.get(letter) == null) {
            } else {
                count += map.get(letter) * (map.get(letter) - 1);
            }

        }
        ind = count / (txt.length()*(txt.length()-1));
        System.out.println(ind);
    }
    INDEX() {}

}
