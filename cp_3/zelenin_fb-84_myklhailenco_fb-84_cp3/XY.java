package com.company;

public class XY {
    public static int findXY(int first_letter, int second_letter, int alph_length) {
        int X;
        X = first_letter * alph_length + second_letter;
        return X;
    }
    XY() {}
}
