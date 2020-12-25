package com.company;

import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class generateKeyPair {
    public static BigInteger getE(BigInteger fi) {
        BigInteger one = BigInteger.ONE;
        BigInteger max = fi.subtract(one);
        BigInteger randomNumber;
        Random randomSource = new Random();
        do {
            randomNumber = new BigInteger(max.bitLength(), randomSource);
        } while (randomNumber.compareTo(max) >=0);
        return randomNumber;
    }
    public static BigInteger reverseElement(BigInteger a, BigInteger b) {
        BigInteger x = new BigInteger("0"), y = new BigInteger("1"), lastx = new BigInteger("1"), lasty = new BigInteger("0"), temp;
        while (!b.equals(new BigInteger("0"))) {
            BigInteger q = a.divide(b);
            BigInteger r = a.mod(b);
            a = b;
            b = r;
            temp = x;
            x = lastx.subtract(q.multiply(x));
            lastx = temp;
            temp = y;
            y = lasty.subtract(q.multiply(y));
            lasty = temp;
        }
        return lastx;
    }
    generateKeyPair() throws IOException {
       BigInteger p,p1,q,q1;
       p = new BigInteger("14967568988040225479967761104497604129961474515493967906476571540736038445589");
       q = new BigInteger("35016834287065361753195441098960275281195499781503133197061769400198608538701");
       p1 = new BigInteger("105536713232898414342527793216791186291168911776980645283478423770722953165579");
       q1 = new BigInteger("108420308173091395574613843557146706842971801986983869070489609587396281961593");
       BigInteger one = BigInteger.ONE;
       BigInteger n = p.multiply(q);
       BigInteger n1 = p1.multiply(q1);
       BigInteger fi = p.subtract(one).multiply(q.subtract(one));
       //BigInteger e = BigInteger.valueOf(2);
       BigInteger fi1 = p1.subtract(one).multiply(q1.subtract(one));
       /*do {
          e = getE(fi);
       } while (!e.gcd(fi).equals(one));*/
       /* BigInteger e1 = BigInteger.valueOf(2);
        do {
            e1 = getE(fi1);
        } while (!e1.gcd(fi1).equals(one)); */
       //BigInteger d = reverseElement(e, fi);
        BigInteger d = new BigInteger("12262787970074932551657829036224960114732503946444842939532806832559043650537152078068813984325565883477187412377778438964427705480930406587005907363761");
        BigInteger e = new BigInteger("521255146184170160693664772176540155184423347526578133111772555004530702558063172176357311958050253181213617559637861857633510338375406464647631323793041");
      //BigInteger d1 = reverseElement(e1,fi1);
      // System.out.println(n1);
       BigInteger d1 = new BigInteger("4381596033746114716132944628514471937597686159000027454198627881047076365314682298830859474603971618788732060645764623599459696068504949436333451426137409");
       BigInteger e1 = new BigInteger("212109528257259114778772539998976477643377714514381724318781368667814411850364662411580663707041669030127425769510845587390987158954082529043500132625137");
       ArrayList<BigInteger> openKeyA = new ArrayList<BigInteger>();
       openKeyA.add(n);
       openKeyA.add(e);
       ArrayList<BigInteger> openKeyB = new ArrayList<BigInteger>();
       openKeyB.add(n1);
       openKeyB.add(e1);
       ArrayList<BigInteger> secretKeyA = new ArrayList<BigInteger>();
       secretKeyA.add(n);
       secretKeyA.add(d);
       ArrayList<BigInteger> secretKeyB = new ArrayList<BigInteger>();
       secretKeyB.add(n1);
       secretKeyB.add(d1);

       BigInteger M = new BigInteger("330");
       sendKey k1 = new sendKey();
       ArrayList<BigInteger> k = new ArrayList<>();
       k = k1.sendKeyFunc(M, secretKeyA.get(1), secretKeyA.get(0), openKeyB.get(1), openKeyB.get(0));
      // System.out.println(k);
       receiveKey r1 = new receiveKey(k.get(0), k.get(1), secretKeyB.get(0), secretKeyB.get(1), openKeyA.get(0), openKeyA.get(1));
       encrypt keyA = new encrypt();
       encrypt keyB = new encrypt();
       //decrypt decB = new decrypt(secretKeyB.get(1), secretKeyB.get(0), keyB.encryptNum(M,openKeyB.get(1), openKeyB.get(0)));
       //decrypt decA = new decrypt(secretKeyA.get(1), secretKeyA.get(0), keyA.encryptNum(M, openKeyA.get(1), openKeyA.get(0)));
       sign signA = new sign();
       verify verifyA = new verify();
      // System.out.println(verifyA.verifyFunc(signA.signFun(M, secretKeyA.get(1), secretKeyA.get(0)), openKeyA.get(1), openKeyA.get(0)));
        encrypt asdlas = new encrypt();
        System.out.println(asdlas.encryptNum(M, e1,n1));
        System.out.println("Сгенерированые значения для A: ");
        System.out.println("----------------------------------------------");
        System.out.println("p: " + p);
        System.out.println("q: " + q);
        System.out.println("d: " + d);
        System.out.println("n: " + n);
        System.out.println("e: " + e);
        System.out.println("----------------------------------------------");
        System.out.println("Сгенерированые значения для B: ");
        System.out.println("----------------------------------------------");
        System.out.println("p1: " + p1);
        System.out.println("q1: " + q1);
        System.out.println("d1: " + d1);
        System.out.println("n1: " + n1);
        System.out.println("e1: " + e1);
        System.out.println("----------------------------------------------");
       ArrayList<BigInteger> site = new ArrayList<>();
        String hexN = "8EB8F87CE1564A1B1DCABCAC8A92DCC298A315F122C3148E1E7D73184BA09CC7A1AC8775CC7FE3735CC80C3271E385E17E2D72B3CB1428669AAE03870B803DF7";
        String hexE = "10001";
        BigInteger noHexN = new BigInteger(hexN, 16);
        BigInteger noHexE = new BigInteger(hexE, 16);
        sendKey k2 = new sendKey();
        ArrayList<BigInteger> k3 = new ArrayList<>();
        k3 = k2.sendKeyFunc(M, secretKeyA.get(1), secretKeyA.get(0), noHexE, noHexN);
        //System.out.println(k3);
        BigInteger s1_s  = new BigInteger("4511846589840956008445452028472716541263301400571060621545285019666561258169261769345442607974311429040157300341274440166403350696633004344373085955812052");
        BigInteger k1_s = new BigInteger("3473732333515177587312852103313797959783709415547635444482100030044261712736169961218827290230838589732169922305625809592035862862285528036876243094874416");
        String k1_tosite = k1_s.toString(16);
        String s1_tosite = s1_s.toString(16);
        String n_toSite = n.toString(16);
        String e_toSite = e.toString(16);
        System.out.println(n_toSite);
        System.out.println(e_toSite);
        System.out.println(k1_tosite);
        System.out.println(s1_tosite);
        String toSiteHexN = noHexN.toString(16);
        String toSiteHexE = noHexE.toString(16);
        System.out.println(toSiteHexN);
        System.out.println(toSiteHexE);
    }
}
