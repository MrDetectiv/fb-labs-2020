package com.company;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Map;
import java.util.Random;

public class getRandomNumber extends Main {

    public getRandomNumber() {
    }

    public static BigInteger generateNumber(int length) {
        BigInteger genereatedNumber = rnd(BigInteger.valueOf(2).pow(length));
        return genereatedNumber;
    }
    public static BigInteger rnd(BigInteger max) {
        BigInteger randomNumber;
        Random randomSource = new Random();
        do {
            randomNumber = new BigInteger(max.bitLength(), randomSource);
        } while (randomNumber.compareTo(max) >=0);
        return randomNumber;
    }
    getRandomNumber(int length) {
       /* for (int i = 0; i < 100000; i++) {
            testFerma mil = new testFerma(generateNumber(length));
        }
        */
    }
}
