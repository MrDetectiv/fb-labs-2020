package com.company;
import java.math.BigInteger;
import java.io.IOException;
import java.util.*;

public class Main {
    static ArrayList<Integer> keys = new ArrayList<>();
    static char[] alpha ={'а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','э','ю','я'};
    static String fileName = "C:\\Users\\What Is Love\\Desktop\\Crypt3\\src\\com\\company\\cipher_text.txt";
    static int[] X = new int[5];
    static int[] Y = new int[5];
    public static void fun(char[] alpha, String[] array) {
        XY num = new XY();
        int[] arr1 = new int[5];
        int[] arr2 = new int[5];
        for (int j = 0 ; j < 5 ; j ++) {
            for (int i = 0 ; i < alpha.length; i++) {
                if (alpha[i] == array[j].charAt(0)) {
                    arr1[j] = i;
                }
            }
        }
        for (int j = 0 ; j < 5 ; j ++) {
            for (int i = 0 ; i < alpha.length; i++) {
                if (alpha[i] == array[j].charAt(1)) {
                    arr2[j] = i;
                }
            }
        }
        for (int i = 0 ; i < 5 ; i++) {
            System.out.println(num.findXY(arr1[i],arr2[i], alpha.length));
        }
    }
    public static void main(String[] args) throws IOException {
        ReadFile file = new ReadFile(fileName);
        String cipher_text = file.readUsingBufferedReader(fileName);
        //BigramFinder bigram = new BigramFinder();
          //bigram.bigram(cipher_text);
        String[] mostPopularBigramm = {"ээ", "вд", "гн", "цг", "чф"};
        String[] mostPopularBigrammRus = {"ст", "но", "то", "на", "ен"};
        XY t = new XY();
        FindKeyA s = new FindKeyA();
        int[] mostPopularY = {896, 66, 106, 685, 733};
        int[] mostPopularX = {545, 417, 572, 403, 168};
        XY num = new XY();
        int []arrX = new int[5];
        for (int i = 0; i < 5; i++) {
            //arrX[i] = num.findXY((int)mostPopularBigramm[i].charAt(0)-1073, mostPopularBigramm[0].charAt(1)-1073, alpha.length);
           // arrX[i] = num.findXY((int)mostPopularBigrammRus[i].charAt(0)-1073, mostPopularBigrammRus[0].charAt(1)-1073, alpha.length);
        }
        FindKeyA keya = new FindKeyA();
        int x = 0;
        int b = 0;
        List<Integer> listBkeys = new ArrayList<Integer>();
        for (int i = 0; i < 4; i++) {
            for (int j = 1; j < 5; j++) {
                if (j == i || i > j) {
                    continue;
                }
                for (int k = 0; k < 4; k++) {
                    for (int o = 1; o < 5; o++) {
                        if (k == o || k > o) {
                            continue;
                        }
                       x = keya.findKey(mostPopularX[i] - mostPopularX[j], mostPopularY[k] - mostPopularY[o], 961);
                        b = (mostPopularY[k] - (x*mostPopularX[i])%961);
                        if (b<0) {
                            b = b + 961;
                        }
                        listBkeys.add(b);
                                // System.out.println(p.invElement(mostPopularX[i] - mostPopularX[j], alpha.length)*(mostPopularY[k] - mostPopularY[o])%31);
                    }b = (mostPopularY[k] - (x*mostPopularX[i])%961);
                    if (b<0) {
                        b = b + 961;
                    }
                    listBkeys.add(b);
                }

            }
        }
        Integer []keysArray = new Integer[keys.size()];
        for (int i = 0 ; i < keysArray.length; i++) {
            keysArray[i] = keys.get(i);
            while (keysArray[i] < 0) {
                keysArray[i] = keysArray[i] + 961;
            }
        }
        List<Integer> listOfGoodKeys = new ArrayList<Integer>();
        List<Integer> list = new ArrayList<>();
        listOfGoodKeys = Arrays.asList(keysArray);
        inverseElement inv = new inverseElement();
        Decoder dec = new Decoder();
        System.out.println(listBkeys.get(3) ==listBkeys.get(4) );
        for (int i = 0 ; i < listBkeys.size()-1;i++) {
            if ((int)listBkeys.get(i) == (int)listBkeys.get(i+1)) {
                listBkeys.remove(i);
            }
        }
        Set<Integer> set = new LinkedHashSet<Integer>(listBkeys);
        Set<Integer> set2 = new LinkedHashSet<Integer>(listOfGoodKeys);
        System.out.println(listBkeys);
        dec.decode(314,34,cipher_text,alpha);
        for (int i = 1 ; i < set.size(); i++) {
        //        dec.decode(listOfGoodKeys.get(i), listBkeys.get(i), cipher_text, alpha);
        }

    }

    }

