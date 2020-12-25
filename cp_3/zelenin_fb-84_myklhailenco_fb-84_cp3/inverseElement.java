package com.company;

public class inverseElement {
    public static int invElement(Integer a ,Integer b) {
        int x=0,y=1,last_x=1,last_y=0,temp;
        while(b!=0)
        {
            int q=a/b;
            int r=a%b;
            a=b;
            b=r;
            temp=x;
            x=last_x-q*x;
            last_x=temp;
            temp=y;
            y=last_y-q*y;
            last_y=temp;
        }
        return last_x;
    }
    inverseElement() {

    }
    inverseElement(int a, int mod) {
        invElement(a, mod);
    }
}
