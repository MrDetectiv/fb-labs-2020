package VigenereCipher.KeyGenerator;

import VigenereCipher.СonformityIndexCounter.ConfirmityIndexCounter;

public class KeyGenerator {
    private int keyLength;

    private String key;
    private String sortedAlphabet;
    private String cipheredText;


    public KeyGenerator(int keyLength, String cipheredText) {
        this.keyLength = keyLength;
        this.cipheredText = cipheredText;
        this.key = "";

        sortedAlphabet = "оеаинтслврмдкупяыьбгзчйжшчюэщцфъ";
    }

    public void generateKey() {
        ConfirmityIndexCounter cipheredTextIndex = new ConfirmityIndexCounter(cipheredText);
        cipheredTextIndex.countCounformityIndex(keyLength);
        String[] textBlock = cipheredTextIndex.getTextBlock();
        String[] lettersStatInEachBlock = new String[keyLength];
        int diff = 1072;

        for ( int i = 0; i < keyLength; i++) {
            ConfirmityIndexCounter blockTextIndex = new ConfirmityIndexCounter(textBlock[i]);
            blockTextIndex.countLettersAmount();
            int[] amount = new int[32];
            amount = blockTextIndex.getLettersAmount();

            String letters = blockTextIndex.getLetters();
            lettersStatInEachBlock[i] = getSortedLettersInBlock(letters, amount);
        }
//        for ( int j = 0; j < keyLength; j++) {
//            System.out.println(lettersStatInEachBlock[j]);
//        }

        for ( int i = 0; i < keyLength; i++ ) {
            int cipheredIndex = (int)lettersStatInEachBlock[i].charAt(31);
            int expectedOpenedIndex = (int)sortedAlphabet.charAt(0);

            System.out.println((char)cipheredIndex);

            int expectedKeyIndex = cipheredIndex - expectedOpenedIndex + diff;
            if ( expectedKeyIndex < 'а' ){
                expectedKeyIndex += 32;
            }

            key += (char)expectedKeyIndex;
        }
    }


    public String getSortedLettersInBlock(String letters, int[] amount) {
        String result = "";

        for ( int i = 1; i < letters.length(); i++ ) {
            int tmp = amount[i];
            StringBuilder t = new StringBuilder(letters);
            int j = i - 1;
            char tmpC = letters.charAt(i);

            for ( ; j >= 0 && amount[j] > tmp; j-- ) {
                amount[j+1] = amount[j];
                t.setCharAt(j+1, letters.charAt(j));
            }
            amount[j+1] = tmp;
            t.setCharAt(j+1, tmpC);
            letters = t.toString();
        }

        result = letters;

        return result;
    }

    private void swap(int i, int i1) {
        int tmp = i;

        i = i1;
        i1 = tmp;
    }

    public String getKey() {
        return this.key;
    }

}
