import VigenereCipher.Decoder.Decoder;
import VigenereCipher.Encoder.Encoder;
import VigenereCipher.KeyGenerator.KeyGenerator;
import VigenereCipher.СonformityIndexCounter.ConfirmityIndexCounter;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.security.spec.ECField;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) throws IOException {
        String data = new String();

        try {
            File myObj = new File("TextFiles/openedText.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                data += myReader.nextLine();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }


        data = data.toLowerCase();
        data = data.replace('ё', 'e');
        data = data.replaceAll("[^а-я]+", "");


        Encoder encoderKey2 = new Encoder("ио", data);
        encoderKey2.encode();
        try (FileWriter writer = new FileWriter("TextFiles/cipheredTextKey2.txt", false)) {
            writer.write(encoderKey2.getCipheredText());
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        Encoder encoderKey3 = new Encoder("рэп", data);
        encoderKey3.encode();
        try (FileWriter writer = new FileWriter("TextFiles/cipheredTextKey3.txt", false)) {
            writer.write(encoderKey3.getCipheredText());
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        Encoder encoderKey4 = new Encoder("кста", data);
        encoderKey4.encode();
        try (FileWriter writer = new FileWriter("TextFiles/cipheredTextKey4.txt", false)) {
            writer.write(encoderKey4.getCipheredText());
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        Encoder encoderKey5 = new Encoder("чашка", data);
        encoderKey5.encode();
        try (FileWriter writer = new FileWriter("TextFiles/cipheredTextKey5.txt", false)) {
            writer.write(encoderKey5.getCipheredText());
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }


        Encoder encoderKey12 = new Encoder("контерстрайк", data);
        encoderKey12.encode();
        try (FileWriter writer = new FileWriter("TextFiles/cipheredTextKey12.txt", false)) {
            writer.write(encoderKey12.getCipheredText());
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        //task 2
        String indexesResult = new String();
        ConfirmityIndexCounter cipheredTextIndex2 = new ConfirmityIndexCounter(encoderKey2.getCipheredText());
        ConfirmityIndexCounter cipheredTextIndex3 = new ConfirmityIndexCounter(encoderKey3.getCipheredText());
        ConfirmityIndexCounter cipheredTextIndex4 = new ConfirmityIndexCounter(encoderKey4.getCipheredText());
        ConfirmityIndexCounter cipheredTextIndex5 = new ConfirmityIndexCounter(encoderKey5.getCipheredText());
        ConfirmityIndexCounter cipheredTextIndex12 = new ConfirmityIndexCounter(encoderKey12.getCipheredText());
        indexesResult += "cipheredTextKey2: " + cipheredTextIndex2.countCounformityIndex(1) + "\n";
        indexesResult += "cipheredTextKey3: " + cipheredTextIndex3.countCounformityIndex(1) + "\n";
        indexesResult += "cipheredTextKey4: " + cipheredTextIndex4.countCounformityIndex(1) + "\n";
        indexesResult += "cipheredTextKey5: " + cipheredTextIndex5.countCounformityIndex(1) + "\n";
        indexesResult += "cipheredTextKey12: " + cipheredTextIndex12.countCounformityIndex(1) + "\n";

        try (FileWriter writer = new FileWriter("TextFiles/confirmityIndexesCipheredTextForKeys2-5_12.txt", false)) {
            writer.write(indexesResult);
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }


//task3

        String cipheredText = new String();
        String buff = new String();
        try {
            File myObj = new File("TextFiles/text.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                cipheredText += myReader.nextLine();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        ConfirmityIndexCounter cipheredTextIndex = new ConfirmityIndexCounter(cipheredText);

        for ( int i = 2; i <= 30; i++ ) {
            buff += "R=" + i + ":" + cipheredTextIndex.countCounformityIndex(i) + "\n";
        }

        try (FileWriter writer = new FileWriter("TextFiles/confirmityIndexesForKeys2-30.txt", false)) {
            writer.write(buff);
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        KeyGenerator keyGenerator = new KeyGenerator(17, cipheredText);
        keyGenerator.generateKey();
        System.out.println(keyGenerator.getKey());

        String key = "войнамагаэндшпиль";

        Decoder decoder = new Decoder(key, cipheredText);
        decoder.decode();
//        System.out.println(key);

        try (FileWriter writer = new FileWriter("TextFiles/decodedTest.txt", false)) {
            writer.write(decoder.getOpenedText());
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

    }
}