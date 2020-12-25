package VigenereCipher.Decoder;

public class Decoder {
    private String key;
    private String openedText;
    private String cipheredText;

    public Decoder(String key, String cipheredText) {
        this.key = key;
        this.cipheredText = cipheredText;
        this.openedText = new String();
    }

    public void decode() {
        for ( int i = 0, j = 0; i < cipheredText.length(); i++, j++ ) {
            if ( j >= key.length()) {
                j = 0;
            }
            char decodedSymbol = ' ';
            int diff = 1072;

            int cipheredSymbolIndex = (int)cipheredText.charAt(i) - diff;
            int keySymbolIndex = (int)key.charAt(j) - diff;

            int decodedSymbolUtf = cipheredSymbolIndex - keySymbolIndex + diff;
            if ( decodedSymbolUtf < 'а' ) {
                decodedSymbolUtf += 32;
            }
            decodedSymbol = (char)decodedSymbolUtf;

            openedText += decodedSymbol;
        }
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getKey() {
        return this.key;
    }

    public String getCipheredText() {
        return this.cipheredText;
    }

    public String getOpenedText() {
        return this.openedText;
    }
}
