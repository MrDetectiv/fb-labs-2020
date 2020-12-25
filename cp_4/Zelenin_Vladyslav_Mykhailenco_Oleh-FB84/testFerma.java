package com.company;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Random;
public class testFerma extends getRandomNumber {
    testFerma(BigInteger p) {
        //STEP 0
        int k = 13;
        int counter = 0;
        //STEP 1
        for (int i = 0; i < 14; i++) {
            Random random = new Random();
            BigInteger x = new BigInteger(p.bitLength(), random);
            while (x.compareTo(p) >= 1) {
                x = new BigInteger(p.bitLength(), random);
            }
            BigInteger one = new BigInteger("1");
            BigInteger valueOne = BigInteger.ONE;
            BigInteger euclid = x.gcd(p);
            BigInteger n;
            if (euclid.equals(one)) {
                n = x.modPow(p.subtract(one), p);
                if (n.equals(one)) {
                    counter++;
                    if (counter==k) {
                        goodNumber.add(p);
                    }
                }
            } else {
                badNumber.add(p);
                break;
            }
            //STEP2
        }
    }
}
