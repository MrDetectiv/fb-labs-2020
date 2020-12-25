package com.company;

public class FindKeyA extends Main {
    public static int findKey(int a, int b, int mod) {
        inverseElement l = new inverseElement();
        gcd ne = new gcd(a,mod);
        int res = 0;
        int number =0;
        int d = ne.gcd2(a,mod);
        if (d == 1) {
                    res = l.invElement(a,mod) * b % mod;
                    keys.add(res);
                    return res;
                }
                else if (b%d != 0) {
                    System.out.println("Error");
                    return 0;
                }
                else {
                    number = l.invElement(a/d, mod/d) * b/d;
                    for (int k = 1 ; k < d; k++ ) {

                        res = (number + k * mod) % mod;
                        keys.add(res);
                    }
        }
       return 0;
    }
    FindKeyA(int a,int b, int mod) {
        System.out.println(findKey(a,b,mod));
    }
    FindKeyA() {};
}
