package AffineCipher;

import RuLanguage.Alphabet;

import java.util.HashMap;

public class TextHandler {
    String text;

    public TextHandler(String text) {
        text = text.toLowerCase();
        text = text.replace('ё', 'e');
        text = text.replace('ъ', 'ь');
        text = text.replaceAll("[^а-я]+", "");

        this.text = text;
    }

    public String getText() {
        return text;
    }


}
