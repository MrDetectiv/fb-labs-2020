#include <iostream>
#include <Windows.h>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

string encrypted_text; // змінна, в яку буде записуватися зашифрований текст
string decrypted_text;
string alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя";
string temp_1[32][2];

string ReadText(string FilePath)
{
    // вхідний потік для роботи з обраним файлом
    ifstream text_file(FilePath);
    // якщо файл вдалося відкрити
    if (text_file.is_open())
    {
        // stringstream - це потік, аналогічний до cin, тільки його вміст береться з заданого йому рядка
        stringstream string_stream;
        // rdbuf() - отримання буфера потоку (найпростіший спосіб отримати весь вміст файлу для подальшої обробки)
        // вставка буфера потоку rdbuf() файлу в рядок потоку - string_stream
        string_stream << text_file.rdbuf();
        // виводимо вміст файлу в один єдиний рядок encrypted_text
        encrypted_text = string_stream.str();
        text_file.close();
    }
    return encrypted_text;
}

// російський алфавіт з нумерацією літер в ньому (ё == е)
void AlphaNumeration()
{
    for (int i = 0; i < 32; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (j == 0) temp_1[i][j] = alphabet[i];
            else temp_1[i][j] = to_string(i);
        }
    }
}

double IndexEncrypted(string text)
{
    int n = text.length();
    double N = 0;
    double sum_N = 0;
    string temp_alphabet = alphabet;

    for (int j = 0; j < 32; j++)
    {
        for (int i = 0; i < n; i++)
        {
            if (text[i] == temp_alphabet[j]) N++;
        }
        if (N > 1) sum_N = sum_N + N*(N - 1);
        else sum_N = sum_N + 0;
        N = 0;
    }

    double I = 1/((double)n*((double)n - 1)) * (double)sum_N;

    ofstream out;
    out.open("C:\\Users\\OKSI\\Desktop\\proga\\results_index_4.txt", ios::app);
    if (out.is_open())
    {
        out << '\n' << "Блок тексту: " << text << '\n';
        out << '\n' << "Індекс відповідності для блоку шифрованого тексту: " << I << '\n';
    }
    out.close();

    return I;
}

int FoundKeyLength(int key)
{
    int k = key;
    int answer;
    int m = encrypted_text.length();
    string *blocks = new string [m];

    for (int i = 0; i < k; i++)
    {
        for (int j = i; j < m; j = j + k)
        {
            blocks[i] = blocks[i] + encrypted_text[j];
        }
    }

    ofstream out;
    out.open("C:\\Users\\OKSI\\Desktop\\proga\\results_index_4.txt", ios::app);
    if (out.is_open()) out << '\n' << "- - - - - - - > " << "Довжина ключа: " << k << '\n';
    out.close();

    for (int i = 0; i < k; i++)
    {
        if (IndexEncrypted(blocks[i]) >= 0.05) answer = k;
        else answer = 0;
    }

    delete []blocks;

    return answer;
}

string LetterFrequency(int key, string text)
{
    int N = 0;
    int m = text.length();
    string temp_alphabet = alphabet;
    string temp_2[32][2];

    for (int j = 0; j < 32; j++)
    {
        for (int i = 0; i < m; i++)
        {
            if (text[i] == temp_alphabet[j]) N++;
        }
        temp_2[j][0] = temp_alphabet[j];
        temp_2[j][1] = to_string((float)N / (float)m);
        N = 0;
    }

    int n = 0;
    string max_frequency = temp_2[0][1];

    for (int i = 0; i < 32; i++)
    {
        if (temp_2[i][1] > max_frequency)
        {
            max_frequency = temp_2[i][1];
            n = i;
        }
    }

    string letter = temp_2[n][0];

    return letter;
}

string FindKey(int key, int position)
{
    AlphaNumeration();

    int M = encrypted_text.length();
    string *blocks = new string [M];

    for (int i = 0; i < key; i++)
    {
        for (int j = i; j < M; j = j + key)
        {
            blocks[i] = blocks[i] + encrypted_text[j];
        }
    }

    string letter, letter_decrypted, letter_number, key_string;
    int x, y, letter_number_int;

    for (int i = 0; i < key; i++)
    {
        letter = LetterFrequency(key, blocks[i]);
        for (int j = 0; j < 32; j++)
        {
            if (letter == temp_1[j][0]) letter_number = temp_1[j][1];
        }
        istringstream(letter_number) >> letter_number_int;
        if(letter_number_int >= position) x = letter_number_int - position;
        else x = (letter_number_int + 32) - position;
        for (int k = 0; k < 32; k++)
        {
            istringstream(temp_1[k][1]) >> y;
            if (x == y) letter_decrypted = temp_1[k][0];
        }
        key_string = key_string + letter_decrypted;
    }

    delete []blocks;

    return key_string;
}

void VigenereDecipher(string key_string, int key_length)
{
    AlphaNumeration();
    cout << '\n' << "Розшифрування тексту, зашифрованого шифром Віженера..." << '\n';

    int n = encrypted_text.length(); // довжина тексту

    string** temp_2 = new string*[n];
    for (int i = 0; i < n; i++)
    {
        temp_2[i] = new string[2];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 32; j++)
        {
            if (encrypted_text[i] == alphabet[j])
            {
                temp_2[i][0] = encrypted_text[i];
                temp_2[i][1] = temp_1[j][1];
            }
        }
    }

    string** temp_3 = new string*[key_length];
    for (int i = 0; i < key_length; i++)
    {
        temp_3[i] = new string[2];
    }
    for (int i = 0; i < key_length; i++)
    {
        for (int j = 0; j < 32; j++)
        {
            if (key_string[i] == alphabet[j])
            {
                temp_3[i][0] = key_string[i];
                temp_3[i][1] = temp_1[j][1];
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        decrypted_text += alphabet[(stoi(temp_2[i][1]) - stoi(temp_3[i % key_length][1]) + 32) % 32];
    }

    ofstream out;
    out.open("C:\\Users\\OKSI\\Desktop\\proga\\words_variant_decrypted.txt");
    if (out.is_open())
    {
        out << "Ключ: " << key_string << '\n' << "Розшифрований текст:" << '\n';
        for (int i = 0; i < decrypted_text.length(); i++)
        {
            out << decrypted_text[i];
        }
    }
    out.close();

    for (int k = 0; k < n; k++)
    {
        delete []temp_2[k];
    }
    delete []temp_2;

    for (int k = 0; k < key_length; k++)
    {
        delete []temp_3[k];
    }
    delete []temp_3;

    cout << '\n' << "Розшифрування пройшло успішно!" << '\n';
}


int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    ReadText("C:\\Users\\OKSI\\Desktop\\proga\\words_variant.txt");
    int key_length;
    cout << '\n' << "Пошук довжини ключа..." << '\n';

    for (int i = 2; i <= 30; i++)
    {
        if (FoundKeyLength(i) != 0)
        {
            key_length = FoundKeyLength(i);
            cout << "Довжина шуканого ключа: " << FoundKeyLength(i) << '\n';
        }
    }

    cout << "Для літери *о*: " << FindKey(key_length, 14) << '\n';
    cout << "Для літери *е*: " << FindKey(key_length, 5) << '\n';
    cout << "Для літери *а*: " << FindKey(key_length, 0) << '\n';
    cout << "Для літери *и*: " << FindKey(key_length, 8) << '\n';
    cout << "Для літери *н*: " << FindKey(key_length, 13) << '\n';

    string key_string = "конкистадорыгермеса";

    VigenereDecipher(key_string, key_length);

    return 0;
}
