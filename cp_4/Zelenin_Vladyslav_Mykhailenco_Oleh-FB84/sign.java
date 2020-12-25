package com.company;

import java.math.BigInteger;

public class sign {
    public static BigInteger signFun(BigInteger M, BigInteger d, BigInteger n) {
        BigInteger S = M.modPow(d,n);
        return S;
    }
    sign() {};
    sign(BigInteger M , BigInteger d, BigInteger n) {
        signFun(M,d,n);
    }
}
