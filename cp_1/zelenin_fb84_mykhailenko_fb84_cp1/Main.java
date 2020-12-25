package com.company;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.DecimalFormat;
import java.util.*;

public class Main {
    public static double countEntropForBigram(double bigram[][]) {
        double result = 0;

        for (int i = 0; i < alpha.length; i++) {
            for (int j = 0; j < alpha.length; j++) {
                if (bigram[i][j] > 0) {
                    double p = bigram[i][j];
                    result += p * (Math.log(p)/Math.log(2)) / 2;
                }
            }
        }
        result *= -1;
        return result;
    }
    public static double[][] count(String file,char[] alpha)
            throws IOException {
        double bigram[][] = new double[alpha.length][alpha.length];
        for (int i = 0; i < alpha.length; i++)
            for (int j = 0; j < alpha.length; j++)
                bigram[i][j] = 0;
        int a = alpha.length+1, b = alpha.length+1;
        float total = 0;
        Scanner in = new Scanner(new File(file));
        while(in.hasNext("\\S+")) {
            String word = in.next("\\S+");
            word.toLowerCase();
            for (int k = 0; k < word.length()-1; k++)
            {
                a = alpha.length+1;
                b = alpha.length+1;
                for (int m = 0; m < alpha.length; m++)
                {
                    if (word.charAt(k) == alpha[m])
                        a = m;
                    if (word.charAt(k+1) == alpha[m])
                        b = m;
                }
                if (a < alpha.length && b < alpha.length)
                {
                    bigram[a][b]++;
                    total++;

                }
            }
        }
        PrintWriter out = new PrintWriter(new FileWriter(file+"a1.txt"));
        for (int p = 0; p < alpha.length; p++) {

            out.print(p + " ");
            for (int q = 0; q < alpha.length; q++) {
                bigram[p][q] = (bigram[p][q] / total);
                double l = bigram[p][q];
                out.print(new DecimalFormat("#0.00000000").format(bigram[p][q]) + " ");
            }
            out.println();
        }

        out.close();
        countEntropForBigram(bigram);
        return bigram;
    }

    static String fileName = "C:\\Users\\What Is Love\\Desktop\\Крипта\\src\\com\\company\\5.txt";
    static int totalChars = fileName.length(); //Полное количество символов в файле
    static String alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
    static char[] alpha ={' ', 'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'};
    private static String readUsingBufferedReader(String fileName) throws IOException {
        BufferedReader reader = new BufferedReader( new FileReader(fileName));
        String line = null;
        StringBuilder stringBuilder = new StringBuilder();
        String ls = System.getProperty("line.separator");
        while( ( line = reader.readLine() ) != null ) {
            stringBuilder.append( line );
            stringBuilder.append( ls );
        }
        stringBuilder.deleteCharAt(stringBuilder.length()-1);
        return stringBuilder.toString();
    }
    public static void main(String[] args) throws IOException {
        double bi1[][] = count("C:\\Users\\What Is Love\\Desktop\\Крипта\\src\\com\\company\\5.txt", alpha);
        for (int i = 0; i < alpha.length; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < alpha.length; j++) {

                    System.out.print(new DecimalFormat("#0.00000000").format((double) bi1[i][j]) + " ");
            }
            System.out.println();
        }
        System.out.println("------------------------------------");
        System.out.println("             Задание 1");
        System.out.println("------------------------------------");
        String resultatString = readUsingBufferedReader(fileName);
        String Sym = readUsingBufferedReader(fileName);
        String wsymbols = Sym.replaceAll("[^а-яёА-ЯЁ\\s]", "");
        wsymbols = wsymbols.replaceAll("\\s{2,}", " ").trim();
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("C:\\Users\\What Is Love\\Desktop\\Крипта\\src\\com\\company\\NoSymbols.txt"), "utf-8"))) {
            writer.write(wsymbols);
        }

        String noM = "C:\\Users\\What Is Love\\Desktop\\Крипта\\src\\com\\company\\NoSymbols.txt";
        System.out.print("Энтропия с пробелами: ");
        noM = noM.toLowerCase();
        Entropy a = new Entropy(noM);
        String textWithoutSpacesEtc = resultatString.replaceAll("[^а-яёА-ЯЁ]", "");
        String lowerCase = textWithoutSpacesEtc.toLowerCase();
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("C:\\Users\\What Is Love\\Desktop\\untitled\\src\\com\\company\\NoSpace.txt"), "utf-8"))) {
            writer.write(lowerCase);
        }
        String fileWithoutSpaces = "C:\\Users\\What Is Love\\Desktop\\untitled\\src\\com\\company\\NoSpace.txt";
        System.out.print("Энтропия без пробелов: ");
        Entropy b = new Entropy(fileWithoutSpaces);
        FrequencyOfLetter freq = new FrequencyOfLetter(resultatString);
        Bigramma step1 = new Bigramma(resultatString, 1, "Количество биграмм с шагом 1 с пробелами : ");
        Bigramma step2 = new Bigramma(resultatString, 2, "Количество биграмм с шагом 2 с пробелами : ");
        Bigramma step1_n = new Bigramma(lowerCase, 1, "Количество биграмм с шагом 1 без пробелов: ");
        Bigramma step2_n = new Bigramma(lowerCase, 2, "Количество биграмм с шагом 2 без пробелов : ");
        System.out.println("------------------------------------");
        System.out.println("             Задание 3");
        System.out.println("------------------------------------");
        double Ideal= Math.log(totalChars)/Math.log(2);
        System.out.println("Идеальная энтропия: " + Ideal);
        int total = lowerCase.length();
        double IdealNS= Math.log(total)/Math.log(2);
        System.out.println("Идеальная энтропия для текста без пробелов: " + IdealNS);
        double R = 1- (4.508985545926398/totalChars);
        System.out.println("Энтропия для биграмм для текста с пробелами " + countEntropForBigram(count("C:\\Users\\What Is Love\\Desktop\\Крипта\\src\\com\\company\\5.txt", alpha)));
        System.out.println("Энтропия для биграмм для текста без пробелов " + countEntropForBigram(count("C:\\Users\\What Is Love\\Desktop\\Крипта\\src\\com\\company\\NoSpace.txt", alpha)));
        System.out.println("R для текста с пробелами : " + R);
        double R1 = 1- (4.531538491601421/totalChars);
        System.out.println("R для текста без пробелов : " + R1);
    }
}
