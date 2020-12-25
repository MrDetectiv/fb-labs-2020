package com.company;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Decoder extends inverseElement {
    static char[] alpha ={'а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я'};
    public static void decode(int a,int b, String text, char[] alpha) {
        ArrayList<Character> alphabet = new ArrayList<>();
        for (int i = 0 ; i < alpha.length; i++) {
            alphabet.add(alpha[i]);
        }
        char []cipher = text.toCharArray();
        ArrayList<String> bigrams = new ArrayList<String>();
       for (int i = 0 ; i < 31; i++) {
           for (int j=0 ; j < 31;j++) {
               bigrams.add(alpha[i] + "" +alpha[j]);
           }
       }
       int y1,y2;
       int Y;
       int X;
        FindKeyA find = new FindKeyA();
        ArrayList<Integer> openBigrams = new ArrayList<Integer>();
        for (int i = 1 ; i < cipher.length-1; i = i + 2) {
            y1 = alphabet.indexOf(cipher[i]);
            y2 = alphabet.indexOf(cipher[i+1]);
            Y =y1*alpha.length+y2;
            X = find.findKey(a,Y-b, 961);
            openBigrams.add(X);
            //cipherBigram.add(text.charAt(i) + "" + text.charAt(i+1) );
       }
        for (int i = 0 ; i < openBigrams.size(); i++) {
            if (openBigrams.get(i) < 0) {
                int x = openBigrams.get(i) + 961;
                if (x < 0) {
                    x = x + 961;
                }
                openBigrams.set(i,x);
            }
        }
        String txt = "";
        for (int i = 0 ; i < openBigrams.size(); i ++) {
            txt += alphabet.get(openBigrams.get(i) / 31) + "" + alphabet.get(openBigrams.get(i)%31);
        }
        System.out.println(txt);
        INDEX ind = new INDEX(txt);

    }

    Decoder(int a, int b, String text) {
    }
    Decoder() {};
}
