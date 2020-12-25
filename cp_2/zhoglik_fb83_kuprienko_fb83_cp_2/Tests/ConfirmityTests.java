import VigenereCipher.Encoder.Encoder;
import VigenereCipher.СonformityIndexCounter.ConfirmityIndexCounter;
import org.junit.Assert;
import org.junit.Test;
import VigenereCipher.Decoder.Decoder;
import VigenereCipher.Encoder.Encoder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ConfirmityTests {

    @Test
    public void letterSetTest() {
        ConfirmityIndexCounter openedTextIndex = new ConfirmityIndexCounter("абвгд");

        String expected = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
        assertEquals(expected, openedTextIndex.getLetters());
    }

    @Test
    public void letterAmountTest() {
        ConfirmityIndexCounter openedTextIndex = new ConfirmityIndexCounter("аавд");

        int[] arr = openedTextIndex.countLettersAmount("аавд");

        assertEquals(2, arr[0]);
        assertEquals(0, arr[1]);
        assertEquals(1, arr[2]);
        assertEquals(0, arr[3]);
        assertEquals(1, arr[4]);
    }

    @Test
    public void testIndex() {
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

        Encoder encoderKey3 = new Encoder("рэп", data);
        encoderKey3.encode();

        ConfirmityIndexCounter openedTextIndex = new ConfirmityIndexCounter(data);
        ConfirmityIndexCounter cipheredTextIndex = new ConfirmityIndexCounter(encoderKey3.getCipheredText());


        assertEquals(openedTextIndex.countCounformityIndex(3), cipheredTextIndex.countCounformityIndex(3));

//        double arrO[] = openedTextIndex.getIndex();
//        double arrC[] = cipheredTextIndex.getIndex();
//
//        for ( int i = 0; i < arrC.length; i++ ) {
//            System.out.println(arrC[i]);
//        }
//
//        for ( int i = 0; i < arrO.length; i++ ) {
//            System.out.println(arrO[i]);
//        }
    }
}
