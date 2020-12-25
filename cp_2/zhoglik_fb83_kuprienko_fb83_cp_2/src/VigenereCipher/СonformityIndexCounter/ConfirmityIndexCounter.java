package VigenereCipher.СonformityIndexCounter;

public class ConfirmityIndexCounter {
    private String text;

    private int[] lettersAmount;
    private String letters;
    private double[] index;
    private String[] textBlock;

    public ConfirmityIndexCounter(String text) {
        letters = "";
        for ( char i = 'а'; i <= 'я'; i++ ) {
            letters += i;
        }

        this.text = text;
        this.lettersAmount = new int[letters.length()];
    }

    public double countCounformityIndex(int keyLength) {
        int currentAmount = 0;
        double result = 0;
        int[] amount;
        index = new double[keyLength];
        textBlock = new String[keyLength];

        for ( int i = 0; i < keyLength; i++) {
            textBlock[i] = "";
            currentAmount = 0;

            for ( int j = i; j < text.length(); j += keyLength) {
                textBlock[i] += text.charAt(j);
            }
            amount = countLettersAmount(textBlock[i]);

            for ( int k = 0; k < amount.length; k++ ) {
                index[i] += amount[k] * (amount[k] - 1);
                currentAmount += amount[k];
            }
            index[i] *= (double)1 / (currentAmount * (currentAmount - 1));
        }

        for ( int i = 0; i < keyLength; i++ ) {
            result += index[i];
        }
        result /=  keyLength;

        return result;
    }

    public void countLettersAmount() {
        for ( int i = 0; i < text.length(); i++ ) {
            for ( int j = 0; j < letters.length(); j++ ) {
                if ( text.charAt(i) == letters.charAt(j) ) {
                    lettersAmount[j] += 1;
                }
            }
        }
    }

    public int[] countLettersAmount(String str) {
        int[] lettersAmountTmp = new int[32];
        for ( int i = 0; i < str.length(); i++ ) {
            for ( int j = 0; j < letters.length(); j++ ) {
                if ( str.charAt(i) == letters.charAt(j) ) {
                    lettersAmountTmp[j] += 1;
                }
            }
        }
        return lettersAmountTmp;
    }

    public String getLetters() {
        return this.letters;
    }

    public String[] getTextBlock() { return this.textBlock; }

    public double[] getIndex() { return this.index; }

    public int[] getLettersAmount() { return this.lettersAmount; }
}
