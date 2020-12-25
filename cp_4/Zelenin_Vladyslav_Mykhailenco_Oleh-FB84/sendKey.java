package com.company;

import java.math.BigInteger;
import java.util.ArrayList;

public class sendKey {
    public static ArrayList<BigInteger> sendKeyFunc(BigInteger k, BigInteger d, BigInteger n, BigInteger e1, BigInteger n1) {
        sign signA = new sign();
        encrypt encA = new encrypt();
        BigInteger s = signA.signFun(k , d , n);
        BigInteger s1 = encA.encryptNum(s, e1, n1);
        BigInteger k1 = encA.encryptNum(k, e1, n1);
        ArrayList<BigInteger> secretMessage = new ArrayList<>();
        secretMessage.add(s1);
        secretMessage.add(k1);
        return secretMessage;
    }
    sendKey() {};
    sendKey(BigInteger k, BigInteger d, BigInteger e, BigInteger e1, BigInteger n1) {
        sendKeyFunc(k,d,e,e1,n1);
    }
}
