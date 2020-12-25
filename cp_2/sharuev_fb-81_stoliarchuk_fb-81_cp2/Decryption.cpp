#include <iostream>
#include <string>
#include <fstream>
#include <Windows.h>
#include <map>
#include <iomanip> 

using namespace std;

string textFileToString(string text)
{
    string buffer;
    ifstream fin("E:\\prest.txt");
    while (fin >> buffer)
    {
        text = text + buffer + " ";
    }
    return text;
}

string whitepaper(string text)
{
    string newText;
    for (int i = 0; i < text.length(); i++)
    {
        if (text[i] >= 'À' && text[i] <= 'ÿ' || text[i] == '¸')
        {
            if (text[i] >= 'À' && text[i] <= 'ß')
            {
                text[i] += 32;
            }
            if (text[i] == '¸')
            {
                text[i] = 'å';
            }
            newText += text[i];
        }
    }
    return newText;
}

int* textToNumbers(string text)
{
    int size = text.length();
    int* textInNumbers = new int[size];

    for (int i = 0; i < text.length(); i++)
    {
        for (int j = 0; j < 32; j++)
        {
            if (text[i] == 'à' + j)
                textInNumbers[i] = j;
        }
    }
    return textInNumbers;
}

int* encryption(int* text, int* key, int textSize, int keySize)
{
    int* encryptedNumbers = new int[textSize];
    int j = 0;

    for (int i = 0; i < textSize; i++)
    {
        if (j == keySize)
        {
            j = 0;
        }
        if ((text[i] + key[j]) > 31)
        {
            encryptedNumbers[i] = text[i] + key[j] - 32;
        }
        else
        {
            encryptedNumbers[i] = text[i] + key[j];
        }
        j++;
    }
    return encryptedNumbers;
}

int* decryption(int* text, int* key, int textSize, int keySize)
{
    int* decryptedNumbers = new int[textSize];
    int j = 0;

    for (int i = 0; i < textSize; i++)
    {
        if (j == keySize)
        {
            j = 0;
        }
        if ((text[i] - key[j]) < 0)
        {
            decryptedNumbers[i] = text[i] - key[j] + 32;
        }
        else
        {
            decryptedNumbers[i] = text[i] - key[j];
        }
        j++;
    }
    return decryptedNumbers;
}

string numbersToText(int* num, int size)
{
    string text;
    text.resize(size);

    for (int i = 0; i < size; i++)
    {
        text[i] = 'à' + num[i];
    }

    return text;
}

void NumberOfEachLetter(string& text, map <string, double>& table)
{
    string cell;

    for (int i = 0; i < text.length(); i++)
    {
        cell = text.substr(i, 1);
        table[cell] ++;
        cell.clear();
    }

}

map<string, double> Frequency(int length, map<string, double>& table)
{
    map<string, double> frequency;

    for (auto itr = table.begin(); itr != table.end(); ++itr)
    {
        frequency.insert({ itr->first, (itr->second / length) });
    }

    for (auto itr = frequency.begin(); itr != frequency.end(); ++itr)
    {
        if (itr->second > 0.08)
        {
            cout << " " << itr->first << "" << "| ";
            cout << fixed;
            cout.precision(5);
            cout << itr->second << endl;
        }
    }
    cout << endl;
    return frequency;
}

double IndexOfCoincidence(double n, map<string, double>& table)
{
    double I = 0;

    for (auto itr = table.begin(); itr != table.end(); ++itr)
    {
        I += (itr->second * (itr->second - 1)) / (n * (n - 1));
    }
    return I;
}

void IndexForD(string text)
{

    for (int i = 2; i <= 30; i++)
    {
        string* block;
        block = new string[i];

        for (int j = 0; j < text.length() - i; j += i)
        {

            for (int k = 0; k < i; k++)
            {
                block[k] += text.substr(j + k, 1);
            }

        }

        map <string, double>* LettersLine;
        LettersLine = new map <string, double>[i];
        double* Ib;
        Ib = new double[i];

        for (int n = 0; n < i; n++)
        {
            NumberOfEachLetter(block[n], LettersLine[n]);
            Ib[n] = IndexOfCoincidence(block[n].length(), LettersLine[n]);
        }

        double I = 0;

        for (int t = 0; t < i; t++)
        {
            I += Ib[t];
        }

        I = I / i;

        cout << "Index for text with block length [" << i << "] " << I << endl;

        delete[] Ib;
        delete[] LettersLine;
        delete[] block;

    }


}

void OutputTextInBlocks(string text, int length)
{
    string* block;
    block = new string[length];

    for (int j = 0; j < text.length() - length; j += length)
    {

        for (int k = 0; k < length; k++)
        {
            block[k] += text.substr(j + k, 1);
        }

    }
    for (int m = 0; m < length; m++)
    {
        cout << "Block [" << m + 1 << "]: " << block[m] << endl << endl;
    }
    delete[] block;
}

void FindKey(string text, int length)
{
    string* block;
    block = new string[length];

    for (int j = 0; j < text.length() - length; j += length)
    {

        for (int k = 0; k < length; k++)
        {
            block[k] += text.substr(j + k, 1);
        }

    }

    map <string, double>* LettersLine;
    LettersLine = new map <string, double>[length];
    map<string, double>* Freq;
    Freq = new map <string, double>[length];

    for (int n = 0; n < length; n++)
    {
        NumberOfEachLetter(block[n], LettersLine[n]);
        cout << endl << endl << "Frequency for block[" << n + 1 << "]: " << endl;
        Frequency(block[n].length(), LettersLine[n]);

    }

    delete[] block;
    delete[] LettersLine;
    delete[] Freq;
}


int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    string text, key;

    text = textFileToString(text);
    text = whitepaper(text);
    int textSize = text.length();
    cout << "Source text: \n" << text << endl << endl;

    map<string, double> lettersE;
    NumberOfEachLetter(text, lettersE);
    double I = IndexOfCoincidence(text.length(), lettersE);

    cout << "Index for encrypted text = " << I << endl << endl;

    IndexForD(text);

    int key_length;

    cout << "Enter the key character range: ";
    cin >> key_length;
    cout << endl;

    OutputTextInBlocks(text, key_length);
    FindKey(text, key_length);

    cout << endl;
    
    cout << "Enter the key:";
    cin.ignore();
    getline(cin, key);
    key = whitepaper(key);
    int keySize = key.length();
    cout << "Your key: " << key << endl;

    int* keyInNumbers = textToNumbers(key);
    int* encryptedNumbers = textToNumbers(text);
    int* textInNumbers = decryption(encryptedNumbers, keyInNumbers, textSize, keySize);

    string decryptedText;
    decryptedText = numbersToText(textInNumbers, textSize);

    for (int i = 0; i < textSize; i++)
    {
        cout << decryptedText[i];
    }
    system("pause");
    return 0;
}