package com.company;

public class Bigramma {
    Bigramma(String txt, int step, String info) {
            int result = 0;
            for (int i=0; i<txt.length()-3; i+=step){
            result++;
    }
            System.out.println(info + result);
    }
}
