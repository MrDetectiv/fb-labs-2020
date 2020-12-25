package AffineCipher;
import RuLanguage.Alphabet;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class AffineDecoder extends  AffineCipher{
    public AffineDecoder(String cipheredText, Key key) {
        this.key = key;
        this.cipheredText = this.handleText(cipheredText);
        this.openedText = "";
    }

    public void decode() throws Exception {
        int openedBigramIndex = 0;
        int cipheredBigramIndex = 0;
        int mod = Alphabet.mod;
        String openedBigram = new String();
        String cipheredBigram = new String();

        if (this.cipheredText.length() % 2 != 0) {
            this.cipheredText = this.cipheredText.substring(0, this.cipheredText.length() - 1);
        }

        for (int i = 0; i < this.cipheredText.length(); i += 2) {
            cipheredBigram = this.cipheredText.substring(i, i + 2);
            openedBigram = "";

            cipheredBigramIndex = Alphabet.letterOrd(cipheredBigram.charAt(0)) * Alphabet.length + Alphabet.letterOrd(cipheredBigram.charAt(1));


            int aInversed = inverse(key.getA(), mod);

            openedBigramIndex = (aInversed * (cipheredBigramIndex - key.getB())) % mod;

            if ( openedBigramIndex < 0 ) {
                openedBigramIndex += mod;
            }


            openedBigram += Alphabet.letterByOrd(openedBigramIndex / Alphabet.length);
            openedBigram += Alphabet.letterByOrd(openedBigramIndex % Alphabet.length);


            openedText += openedBigram;
        }
    }

    // Завдання 1, математичні операції
    public static int gcd (int a, int b) {
        if (b != 0) {
            return gcd(b, a%b);
        }
        return a;
    }

    public static int inverse (int a, int m) {
        int r0 = a;
        int r1 = m;
        int q = 0;
        int u0 = 1;
        int u1 = 0;

        for ( ; r0 % r1 != 0; ) {
            int t = r0 % r1;
            r0 = r1;
            r1 = t;
            t = u1;
            u1 = u0 - q * u1;
            u0 = t;

            if (r1 != 0) {
                q = r0 / r1;
            } else {
                break;
            }
        }
        return (u1 + m) % m;
    }

    public static List<Integer> multiplySolutions(int dx, int dy, int mod) throws NoSolutions {
        List<Integer> solutions = new ArrayList<>();
        int d = gcd(dx,mod);
        if(d==1){
            int dx_inv = inverse(dx,mod);
            int result = (dx_inv*dy)%mod;

            if ( result < 0 ) {
                result += mod;
            }
            solutions.add(result);
        }
        else {
            if(dy%d==0) {
                int dx1 = dx / d;
                int dy1 = dy / d;
                int mod1 = mod / d;
                int X0 = multiplySolutions(dx1,dy1,mod1).get(0);

                for(int i = 0; i < d; i++){
                    solutions.add(X0 + i * mod1);
                }
            }
            /*else {
                throw new NoSolutions();
            }*/
        }
        return solutions;
    }

    public static List<Integer> findingSolutions(int x1, int x2, int y1, int y2, int m) throws NoSolutions {
        int dY = 0;
        int dX = 0;
        dY = (y1 - y2 )% m;
        dX = (x1 - x2 )% m;
        return multiplySolutions(dX,dY,m);
    }

    public static List<Key> findKeys(int x1, int x2, int y1, int y2, int m) throws NoSolutions {
        int dY = 0;
        int dX = 0;
        dY = (y1 - y2);
        dX = (x1 - x2);
        List<Integer> aKeys = multiplySolutions(dX, dY, m);
        List<Integer> bKeys = new ArrayList<>();
        List<Key> keys = new ArrayList<>();

        for (int i = 0; i < aKeys.size(); i++) {
            int b = (y1 - aKeys.get(i) * x1) % m;
            if (b < 0) {
                b += m;
            }
            bKeys.add(b);

            keys.add(new Key(aKeys.get(i), bKeys.get(i)));
        }

        return keys;
    }
}
