package com.company;

import java.math.BigInteger;

public class decrypt {
    public static BigInteger decFunc(BigInteger d , BigInteger n, BigInteger C) {
        BigInteger M = C.modPow(d,n);
        return M;
    }
    decrypt() {

    }
    decrypt(BigInteger d , BigInteger n, BigInteger C) {
        BigInteger M = C.modPow(d,n);
        System.out.println(M);
    }
}
