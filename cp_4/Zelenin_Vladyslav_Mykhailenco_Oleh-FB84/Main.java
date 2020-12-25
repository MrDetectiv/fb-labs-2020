package com.company;

import java.io.*;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<BigInteger> goodNumber = new ArrayList<BigInteger>();
    static ArrayList<BigInteger> badNumber = new ArrayList<BigInteger>();
    public static void main(String[] args) throws IOException {
        getRandomNumber num = new getRandomNumber(256);
        generateKeyPair key = new generateKeyPair();
    }
}
