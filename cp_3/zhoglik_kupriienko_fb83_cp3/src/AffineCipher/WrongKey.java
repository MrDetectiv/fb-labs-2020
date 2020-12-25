package AffineCipher;

public class WrongKey extends Exception{
    public String info;

    public WrongKey(String info) {
        this.info = info;
    }
}
