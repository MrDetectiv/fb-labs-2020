package com.company;

import java.util.HashMap;

public class FrequencyOfLetter {
    String alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
    char[] alpha ={'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','\u0020'};
     FrequencyOfLetter(String txt) {
        int totalChars = txt.length();
         for (int a = 0; a < alpha.length; a++) {
             char letter = alpha[a];
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
                 System.out.print("Число повторов буквы " + letter + " - " + map.get(letter));
                 System.out.println("|| Вероятность буквы : " + (double)map.get(letter)/totalChars);
             }
         }
     }
}

