package com.company;

import java.math.BigInteger;

public class verify {
    public static BigInteger verifyFunc(BigInteger S , BigInteger e, BigInteger n) {
        BigInteger M = S.modPow(e,n);
        return M;
    }
    verify() {};
    verify(BigInteger S , BigInteger e, BigInteger n) {
        verifyFunc(S,e,n);
    }
}
