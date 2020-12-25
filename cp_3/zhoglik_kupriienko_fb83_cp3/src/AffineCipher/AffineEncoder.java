package AffineCipher;
import RuLanguage.Alphabet;

public class AffineEncoder extends AffineCipher {
    public AffineEncoder(String openedText, Key key) {
        this.key = key;
        this.openedText = this.handleText(openedText);
        this.cipheredText = "";
    }

    public void encode() throws Exception {
        int openedBigramIndex = 0;
        int cipheredBigramIndex = 0;
        int mod = Alphabet.length * Alphabet.length;
        String openedBigram = new String();
        String cipheredBigram = new String();

        if ( this.openedText.length() %2 != 0 ) {
            this.openedText = this.openedText.substring(0,this.openedText.length()-1);
        }

        for ( int i = 0; i < this.openedText.length(); i += 2 ) {
            cipheredBigram = "";
            openedBigram = this.openedText.substring(i,i+2);
            openedBigramIndex = Alphabet.letterOrd(openedBigram.charAt(0)) * Alphabet.length + Alphabet.letterOrd(openedBigram.charAt(1));

            cipheredBigramIndex = (key.getA() * openedBigramIndex + key.getB()) % mod;

            cipheredBigram += Alphabet.letterByOrd(cipheredBigramIndex / Alphabet.length);
            cipheredBigram += Alphabet.letterByOrd(cipheredBigramIndex % Alphabet.length);

            cipheredText += cipheredBigram;
        }
    }
}
