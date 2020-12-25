package AffineCipher;

public class WrongIndex extends Exception{
    public int state;

    public WrongIndex(int st) {
        this.state = st;
    }
}
