package com.company;

import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Entropy {
    Entropy(String txt) {
        System.out.println(getEntropy(getTextFileStatistic(txt)));
    }
    private static double getEntropy(Map<Character, Integer> statistMap) {
        long countAllChars = 0;
        for (Integer elemMapVal : statistMap.values()) {
            countAllChars += elemMapVal;
        }
        final double CONST_RET = Math.pow(Math.log(2), -1);
        final double CONST_LOCAL = Math.log(countAllChars);
        double preEntropy = 0;
        for (Integer elemMapVal : statistMap.values()) {
            preEntropy += (1. * elemMapVal/countAllChars) * (Math.log(elemMapVal) - CONST_LOCAL);
        }
        return -1 * CONST_RET * preEntropy;
    }

    private static Map<Character, Integer> getTextFileStatistic(String fileName) {
        Map<Character, Integer> statRet = new HashMap<>();
        try(FileReader filRead = new FileReader(fileName)) {
            int charFile;
            while ((charFile = filRead.read()) != -1) {
                    if (statRet.containsKey((char)charFile))
                        statRet.put((char)charFile, statRet.get((char)charFile) + 1);
                    else statRet.put((char)charFile, 1);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return statRet;
    }
}


