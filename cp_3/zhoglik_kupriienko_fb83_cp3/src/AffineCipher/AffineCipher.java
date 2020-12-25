package AffineCipher;

import RuLanguage.Alphabet;

import java.util.HashMap;

public abstract class AffineCipher {
    protected String openedText;
    protected String cipheredText;

    protected Key key;

    public String getCipheredText() {
        return cipheredText;
    }

    public String getOpenedText() {
        return openedText;
    }

    public Key getKey() {
        return key;
    }

    public void setCipheredText(String cipheredText) {
        this.cipheredText = cipheredText;
    }

    public void setKey(Key key) {
        this.key = key;
    }

    public void setOpenedText(String openedText) {
        this.openedText = openedText;
    }

    public String handleText(String text) {
        TextHandler textHandler = new TextHandler(text);

        return textHandler.getText();
    }
}
