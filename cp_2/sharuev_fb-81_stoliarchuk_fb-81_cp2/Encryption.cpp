#include <iostream>
#include <string>
#include <fstream>
#include <Windows.h>

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
            if (text[i] == 'ú')
            {
                text[i] = 'ü';
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

string numbersToText(int* num, int size)
{
    string cipherText;
    cipherText.resize(size);

    for (int i = 0; i < size; i++)
    {
        cipherText[i] = 'à' + num[i];
    }

    return cipherText;
}

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    string text, key;

    text = textFileToString(text);
    text = whitepaper(text);

    cout << "Source text: \n" << text << endl << endl;

    cout << "Enter the key: ";
    getline(cin, key);
    key = whitepaper(key);
    cout << "Your key: " << key << endl;

    int textSize = text.length();
    int* textInNumbers = new int[textSize];
    textInNumbers = textToNumbers(text);

    int keySize = key.length();
    int* keyInNumbers = new int[keySize];
    keyInNumbers = textToNumbers(key);

    int* encryptedNumbers = new int[textSize];
    encryptedNumbers = encryption(textInNumbers, keyInNumbers, textSize, keySize);

    string encryptedText = numbersToText(encryptedNumbers, textSize);

    for (int i = 0; i < textSize; i++)
    {
        cout << encryptedText[i];
    }

    return 0;
}