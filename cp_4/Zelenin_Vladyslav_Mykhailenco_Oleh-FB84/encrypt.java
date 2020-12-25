package com.company;

import java.math.BigInteger;

public class encrypt {
    public static BigInteger encryptNum(BigInteger M, BigInteger e, BigInteger n) {
        BigInteger C = M.modPow(e,n);
        return C;
    }
    encrypt() {

    }
    encrypt(BigInteger M, BigInteger e , BigInteger n) {
        encryptNum(M, e,n);
    }
}
