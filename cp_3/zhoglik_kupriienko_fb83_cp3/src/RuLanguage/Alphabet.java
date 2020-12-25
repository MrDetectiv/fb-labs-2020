package RuLanguage;

import AffineCipher.*;

public class Alphabet {
    public static int length = 31;
    public static String alphabet = alphabetInit();
    public static int mod = Alphabet.length * Alphabet.length;
    public static String[] mostPopularBigrams = {"ст" , "но", "то", "на", "ен"};
    public static String[] mostPopularMonograms = {"о" , "е", "а"};
    public static String[] lostPopularMonograms = {"ф" , "ц", "щ"};

    public Alphabet() {

    }

    public static String alphabetInit() {
        alphabet = "";
        for ( int i = 'а'; i <= 'я'; i++) {
            alphabet += (char)i;
        }
        return alphabet;
    }
    public static int letterOrd(char letter) {
        if (letter == 'а') return 0;
        if (letter == 'б') return 1;
        if (letter == 'в') return 2;
        if (letter == 'г') return 3;
        if (letter == 'д') return 4;
        if (letter == 'е') return 5;
        if (letter == 'ж') return 6;
        if (letter == 'з') return 7;
        if (letter == 'и') return 8;
        if (letter == 'й') return 9;
        if (letter == 'к') return 10;
        if (letter == 'л') return 11;
        if (letter == 'м') return 12;
        if (letter == 'н') return 13;
        if (letter == 'о') return 14;
        if (letter == 'п') return 15;
        if (letter == 'р') return 16;
        if (letter == 'с') return 17;
        if (letter == 'т') return 18;
        if (letter == 'у') return 19;
        if (letter == 'ф') return 20;
        if (letter == 'х') return 21;
        if (letter == 'ц') return 22;
        if (letter == 'ч') return 23;
        if (letter == 'ш') return 24;
        if (letter == 'щ') return 25;
        if (letter == 'ь') return 26;
        if (letter == 'ы') return 27;
        if (letter == 'э') return 28;
        if (letter == 'ю') return 29;
        if (letter == 'я') return 30;
        return -1;
    }
    public static char letterByOrd(int ord) throws Exception {

        if (ord == 0) return 'а';
        if (ord == 1) return 'б';
        if (ord == 2) return 'в';
        if (ord == 3) return 'г';
        if (ord == 4) return 'д';
        if (ord == 5) return 'е';
        if (ord == 6) return 'ж';
        if (ord == 7) return 'з';
        if (ord == 8) return 'и';
        if (ord == 9) return 'й';
        if (ord == 10) return 'к';
        if (ord == 11) return 'л';
        if (ord == 12) return 'м';
        if (ord == 13) return 'н';
        if (ord == 14) return 'о';
        if (ord == 15) return 'п';
        if (ord == 16) return 'р';
        if (ord == 17) return 'с';
        if (ord == 18) return 'т';
        if (ord == 19) return 'у';
        if (ord == 20) return 'ф';
        if (ord == 21) return 'х';
        if (ord == 22) return 'ц';
        if (ord == 23) return 'ч';
        if (ord == 24) return 'ш';
        if (ord == 25) return 'щ';
        if (ord == 26) return 'ь';
        if (ord == 27) return 'ы';
        if (ord == 28) return 'э';
        if (ord == 29) return 'ю';
        if (ord == 30) return 'я';
        return '_';
    }

    public static int bigramOrd(String bigram) {
        return Alphabet.letterOrd(bigram.charAt(0)) * Alphabet.length + Alphabet.letterOrd(bigram.charAt(1));
    }

    public static boolean isCorrectText(String text) throws WrongKey {
        boolean isTopLetterExist = false;
        boolean isBottomLetterExist = false;
        MonogramTextHandler th = new MonogramTextHandler(text);
        th.countFrequency();
        th.setMonogramFrequency(th.sortHashMapByValues(th.getMonogramFrequency()));


        String mostPopularLetter = th.getLastKey();
        String lostPopularLetter = th.getFisttKey();

        if ( mostPopularLetter == "_") {
            return false;
        }

        for ( int i = 0; i < Alphabet.mostPopularMonograms.length; i++ ) {
            if (Alphabet.letterOrd(mostPopularLetter.charAt(0)) == Alphabet.letterOrd(Alphabet.mostPopularMonograms[i].charAt(0))) {
                isTopLetterExist = true;
            }
        }

        if ( isTopLetterExist ) {
            for ( int i = 0; i < Alphabet.lostPopularMonograms.length; i++ ) {
                if (Alphabet.letterOrd(lostPopularLetter.charAt(0)) == Alphabet.letterOrd(Alphabet.lostPopularMonograms[i].charAt(0))) {
                    isBottomLetterExist = true;
                }
            }
        } else {
            throw new WrongKey("Не прошел проверку по самым часто встречаемым буквам");
        }

        if (isTopLetterExist && isBottomLetterExist) {
            return true;
        }
        throw new WrongKey("Не прошел проверку по самым редко встречаемым буквам");
    }

}
