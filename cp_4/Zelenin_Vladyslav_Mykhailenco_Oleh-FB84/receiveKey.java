package com.company;

import java.math.BigInteger;

public class receiveKey {

    receiveKey(BigInteger s1, BigInteger k1, BigInteger n1 ,BigInteger d1 ,BigInteger n, BigInteger e) {
        decrypt decA = new decrypt();
        BigInteger k = decA.decFunc(d1,n1,k1);
        BigInteger s = decA.decFunc(d1,n1,s1);
        verify V = new verify();
       // System.out.println(k);
        System.out.println("Проверка s " + V.verifyFunc(s, e,n));
        System.out.println("Проверка k " + k);
    }
}
