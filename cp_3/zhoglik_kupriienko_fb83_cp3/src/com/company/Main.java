package com.company;

import AffineCipher.*;
import RuLanguage.Alphabet;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {

    public static void main(String args[]) throws Exception {
        String data = "";
        try {
            File myObj = new File("09.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                data += myReader.nextLine();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        BigramTextHandler bg = new BigramTextHandler(data);
        bg.countFrequency();
        bg.setBigramFrequency(bg.sortHashMapByValues(bg.getBigramFrequency()));

        String[] cipheredMostPopularBigrams = bg.getLastNKeys(5) ;

        for ( int i = 0; i < 5; i++ ) {
            System.out.println(cipheredMostPopularBigrams[i]);
        }

        Set<Key> uniqueKeys = new HashSet<>();

        String tempX1, tempX2, tempY1, tempY2;
        for (int x = 0; x < Alphabet.mostPopularBigrams.length * Alphabet.mostPopularBigrams.length; x++) {
            if ((x / 5) == (x % 5)) continue;
            tempX1 = Alphabet.mostPopularBigrams[x / 5];
            tempX2 = Alphabet.mostPopularBigrams[x % 5];
            for (int y = 0; y < cipheredMostPopularBigrams.length * cipheredMostPopularBigrams.length; y++) {
                if ((y / 5) == (y % 5)) continue;
                tempY1 = cipheredMostPopularBigrams[y / 5];
                tempY2 = cipheredMostPopularBigrams[y % 5];


                List<Key> keys = AffineDecoder.findKeys(Alphabet.bigramOrd(tempX1),
                        Alphabet.bigramOrd(tempX2),
                        Alphabet.bigramOrd(tempY1),
                        Alphabet.bigramOrd(tempY2),
                        Alphabet.mod);

                uniqueKeys.addAll(keys);
            }

        }

        System.out.println(uniqueKeys);

        for ( Key key : uniqueKeys ) {
            AffineDecoder decoder = new AffineDecoder(data, key);
            try {
                decoder.decode();
            } catch (WrongIndex e) {
                continue;
            } catch (NoSolutions e) {
                continue;
            }

            try {
                if (Alphabet.isCorrectText(decoder.getOpenedText())) {
                    System.out.println(key + " Возможно этот кандидат является решением");
                }
            } catch (WrongKey e) {
                System.out.println(key + " " + e.info);
            }
        }

        AffineDecoder decoder = new AffineDecoder(data, new Key( 314, 34));
        decoder.decode();

        System.out.println(decoder.getKey());
        System.out.println(decoder.getOpenedText());


    }
}
