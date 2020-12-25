import VigenereCipher.Encoder.Encoder;
import org.junit.Assert;
import org.junit.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class EncoderTest {
    @Test
    public void encodeMethod() {
        Encoder encoder = new Encoder("кальян", "сашажогликиартемкуприенко");

        encoder.encode();

        assertEquals('ы', encoder.getCipheredText().charAt(0));
        assertEquals('а', encoder.getCipheredText().charAt(1));
        assertEquals('г', encoder.getCipheredText().charAt(2));
        assertEquals('н', encoder.getCipheredText().charAt(6));
    }
}
