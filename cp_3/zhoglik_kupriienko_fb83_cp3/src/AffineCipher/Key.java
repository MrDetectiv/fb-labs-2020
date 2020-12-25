package AffineCipher;

import java.util.Objects;

public class Key {
    private int a;
    private int b;

    public Key(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public void setA(int a) {
        this.a = a;
    }

    public void setB(int b) {
        this.b = b;
    }

    public String toString() {
        String result = "( " + this.a + ", " + this.b + ")";
        return result;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Key key = (Key) o;
        return a == key.a &&
                b == key.b;
    }

    @Override
    public int hashCode() {
        return Objects.hash(a, b);
    }
}
