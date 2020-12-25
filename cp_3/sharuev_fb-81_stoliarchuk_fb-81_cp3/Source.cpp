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
    ifstream fin("Q:\\prest.txt");
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
        if (text[i] >= '¿' && text[i] <= 'ˇ' || text[i] == '∏')
        {
            if (text[i] >= '¿' && text[i] <= 'ﬂ')
            {
                text[i] += 32;
            }
            if (text[i] == '∏')
            {
                text[i] = 'Â';
            }
            newText += text[i];
        }
    }
    return newText;
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

void NumberOfEach—oupleLetter(string& text, map <string, double>& table)
{
    string cell;

    for (int i = 0; i < text.length() && i + 2 != text.length() - 1; i += 2)
    {
        cell = text.substr(i, 2);
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

int CharToNumber(char symbol)
{
    if (symbol == '‡') return 0;
    if (symbol == '·') return 1;
    if (symbol == '‚') return 2;
    if (symbol == '„') return 3;
    if (symbol == '‰') return 4;
    if (symbol == 'Â') return 5;
    if (symbol == 'Ê') return 6;
    if (symbol == 'Á') return 7;
    if (symbol == 'Ë') return 8;
    if (symbol == 'È') return 9;
    if (symbol == 'Í') return 10;
    if (symbol == 'Î') return 11;
    if (symbol == 'Ï') return 12;
    if (symbol == 'Ì') return 13;
    if (symbol == 'Ó') return 14;
    if (symbol == 'Ô') return 15;
    if (symbol == '') return 16;
    if (symbol == 'Ò') return 17;
    if (symbol == 'Ú') return 18;
    if (symbol == 'Û') return 19;
    if (symbol == 'Ù') return 20;
    if (symbol == 'ı') return 21;
    if (symbol == 'ˆ') return 22;
    if (symbol == '˜') return 23;
    if (symbol == '¯') return 24;
    if (symbol == '˘') return 25;
    if (symbol == '¸') return 26;
    if (symbol == '˚') return 27;
    if (symbol == '˝') return 28;
    if (symbol == '˛') return 29;
    if (symbol == 'ˇ') return 30;
}

char NumberToChar(int number)
{
    if (number == 0) return '‡';
    if (number == 1) return '·';
    if (number == 2) return '‚';
    if (number == 3) return '„';
    if (number == 4) return '‰';
    if (number == 5) return 'Â';
    if (number == 6) return 'Ê';
    if (number == 7) return 'Á';
    if (number == 8) return 'Ë';
    if (number == 9) return 'È';
    if (number == 10) return 'Í';
    if (number == 11) return 'Î';
    if (number == 12) return 'Ï';
    if (number == 13) return 'Ì';
    if (number == 14) return 'Ó';
    if (number == 15) return 'Ô';
    if (number == 16) return '';
    if (number == 17) return 'Ò';
    if (number == 18) return 'Ú';
    if (number == 19) return 'Û';
    if (number == 20) return 'Ù';
    if (number == 21) return 'ı';
    if (number == 22) return 'ˆ';
    if (number == 23) return '˜';
    if (number == 24) return '¯';
    if (number == 25) return '˘';
    if (number == 26) return '¸';
    if (number == 27) return '˚';
    if (number == 28) return '˝';
    if (number == 29) return '˛';
    if (number == 30) return 'ˇ';
}


int gcd(int a, int b) {
    while (a != 0 && b != 0) {
        if (a > b) {
            a = a % b;
        }
        else b = b % a;
    }
    return a + b;
}

int ReverseElement(int a, int m) {

    int pm = m, pu = 1, pv = 0, u = 0, v = 1, q, t1, t2, t3;
    if (gcd(a, m) != 1) {
        return 0;
    }
    else {
        while (m != 0)
        {
            q = a / m;
            t1 = u;
            u = pu - q * u;
            pu = t1;

            t2 = v;
            v = pv - q * v;
            pv = t2;

            t3 = a;
            a = m;
            m = t3 % m;

        }
        while (pu < 0)
        {
            pu += pm;
        }
        pu = pu % pm;
        return pu;
    }
}

int LinearComparison(int a, int b, int m, int solution[]) {

    int a1, b1, m1, x0;

    if (a < 0)
    {
        a += m;
    }
    if (b < 0)
    {
        b += m;
    }

    if (gcd(a, m) == 1)
    {
        return (ReverseElement(a, m) * (b)) % m;
    }
    if (gcd(a, m) > 1) {

        if (b % gcd(a, m) != 0)
        {
            return -1;
        }
        else
        {
            a1 = a / gcd(a, m);
            b1 = b / gcd(a, m);
            m1 = m / gcd(a, m);
            x0 = (ReverseElement(a1, m1) * b1) % m1;
            for (int i = 0; i < gcd(a, m); i++)
            {
                solution[i] = x0 + i * m1;
            }
            return -2;
        }
    }
}

int BigramToNumber(string bigram)
{
    int X, x1, x2;

    x1 = CharToNumber(bigram[0]);
    x2 = CharToNumber(bigram[1]);
    X = x1 * 31 + x2;
    return X;
}

int FindB(int X1, int Y1, int a)
{
    int b;

    b = (Y1 - a * X1) % 961;
    while (b < 0)
    {
        b += 961;
    }
    return b;
}

string Decrypt(string ch, int a, int b)
{

    string de;
    int x1, x2;
    int y1, y2;

    for (int i = 0; i < ch.length() && i + 2 != ch.length() - 1; i += 2)
    {
        int Y, X;

        y1 = CharToNumber(ch[i]);
        int k = i + 1;
        y2 = CharToNumber(ch[k]);

        Y = y1 * 31 + y2;
        X = ReverseElement(a, 961) * (Y - b) % 961;

        while (X < 0)
        {
            X += 961;
        }

        x1 = X / 31;
        x2 = X % 31;

        char x = NumberToChar(x1);
        char y = NumberToChar(x2);

        de.append(1, x);
        de.append(1, y);

    }


    return de;
}

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);


    string text;

    text = textFileToString(text);
    text = whitepaper(text);
    cout << "—iphertext:\n" << text << endl << endl;


    map<string, double> bigram;
    NumberOfEach—oupleLetter(text, bigram);
    map<string, double> monogram;
    NumberOfEachLetter(text, monogram);
    map<string, double> Bigram_Freq_WIn = Frequency(text.length() / 2, bigram);

    string bi_ch[5];

    const int N = Bigram_Freq_WIn.size();
    double* Array = new double[N];

    int z = 0;

    for (auto itr = Bigram_Freq_WIn.begin(); itr != Bigram_Freq_WIn.end(); ++itr)
    {
        Array[z] = itr->second;
        z++;
    }

    for (int i = 1; i < (int)N; i++)
    {
        for (int j = (int)N - 1; j >= i; j--)
        {
            if (Array[j] < Array[j - 1])
            {
                double x = Array[j - 1];
                Array[j - 1] = Array[j];
                Array[j] = x;
            }
        }
    }
    cout << "5 most common bigram:" << endl;
    z = 1;
    for (int i = (int)N - 1 ; i > (int)N - 6; i--)
    {
        for (auto itr = Bigram_Freq_WIn.begin(); itr != Bigram_Freq_WIn.end(); ++itr)
        {
            if (Array[i] == itr->second)
            {
                cout << z << ") " << itr->first << "" << "| ";
                cout << fixed;
                cout.precision(5);
                cout << itr->second << endl;

                bi_ch[z - 1] = itr->first;

                z++;
            }
        }
    }
    delete[] Array;
    cout << endl;

    int X[5];
    string bi_de[5] = { "ÒÚ", "ÌÓ", "ÚÓ", "Ì‡", "ÂÌ" };
    int Y[5];
    cout << "Value of bigram: " << endl;
    for (int i = 0; i < 5; i++)
    {

        X[i] = BigramToNumber(bi_de[i]);
        cout << "X[" << i + 1 << "] = " << X[i] << endl;

    }
    cout << endl;
    for (int i = 0; i < 5; i++)
    {
        Y[i] = BigramToNumber(bi_ch[i]);
        cout << "Y[" << i + 1 << "] = " << Y[i] << endl;
    }


    cout << endl << "Most possible keys: " << endl;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (i == j)
            {
                j++;
            }
            else
            {
                for (int k = 0; k < 5; k++)
                {
                    for (int l = 0; l < 5; l++)
                    {
                        if (k == l)
                        {
                            l++;
                        }
                        else
                        {
                            int a, b, m = 961;
                            a = X[i] - X[j];
                            b = Y[k] - Y[l];

                            int A, B;

                            if (a < 0)
                            {
                                a = a + m;
                            }

                            if (b < 0)
                            {
                                b = b + m;
                            }


                            int* solution = new int[gcd(a, m)];
                            int x;

                            x = LinearComparison(a, b, m, solution);

                            if (x == -1)
                            {
                                //cout << "No solution"<< endl;
                            }
                            else if (x == -2)
                            {
                                for (int p = 0; p < gcd(a, m); p++)
                                {
                                    A = solution[p];

                                    if (A != 0)
                                    {
                                        B = FindB(X[i], Y[k], A);
                                        string de = Decrypt(text, A, B);
                                        map<string, double> lettersD;
                                        NumberOfEachLetter(de, lettersD);
                                        double I = IndexOfCoincidence(de.length(), lettersD);
                                        if (I > 0.055 && I < 1)
                                        {
                                            cout << "{" << A << ", " << B << "}" << "\t| Index of coincidence: " << I << endl;
                                        }


                                    }

                                }
                            }
                            else
                            {
                                A = x;
                                if (A != 0)
                                {
                                    B = FindB(X[i], Y[k], A);
                                    string de = Decrypt(text, A, B);
                                    map<string, double> lettersD;
                                    NumberOfEachLetter(de, lettersD);
                                    double I = IndexOfCoincidence(de.length(), lettersD);
                                    if (I > 0.055 && I < 1)
                                    {
                                        cout << "{" << A << ", " << B << "}" << "\t| Index of coincidence: " << I << endl;
                                    }

                                }
                            }


                            delete[] solution;
                        }
                    }
                }
            }
        }
    }



    int key_a, key_b;
    cout << endl << "Enter key: " << endl << "a = ";
    cin >> key_a;
    cout << "b = ";
    cin >> key_b;


    string de = Decrypt(text, key_a, key_b);

    cout << endl << "Decrypted text: " << endl << de << endl;

    system("pause");
    return 0;
}