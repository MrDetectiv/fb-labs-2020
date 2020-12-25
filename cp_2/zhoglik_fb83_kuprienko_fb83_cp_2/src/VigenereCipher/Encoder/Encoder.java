package VigenereCipher.Encoder;

public class Encoder {
    private String key;
    private String openedText;
    private String cipheredText;

    public Encoder(String key, String openedText) {
        this.key = key;
        this.openedText = openedText;
        this.cipheredText = new String();
    }

    public void encode() {
        for ( int i = 0, j = 0; i < openedText.length(); i++, j++ ) {
            if ( j >= key.length()) {
                j = 0;
            }
            char encodedSymbol = ' ';
            int diff = 1072;

            int openedSymbolIndex = (int)openedText.charAt(i) - diff;
            int keySymbolIndex = (int)key.charAt(j) - diff;

            int encodedSymbolUtf = openedSymbolIndex + keySymbolIndex + diff;
            if ( encodedSymbolUtf > 'я' ) {
                encodedSymbolUtf -= 32;
            }
            encodedSymbol = (char)encodedSymbolUtf;

            cipheredText += encodedSymbol;
        }
    }

    public String getKey() {
        return this.key;
    }

    public String getOpenedText() {
        return this.openedText;
    }

    public String getCipheredText() {
        return this.cipheredText;
    }
}
