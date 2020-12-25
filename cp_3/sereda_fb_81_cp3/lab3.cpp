#include <iostream>
#include <stdio.h>
#include <cmath>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

char alphabet[31] = {'а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я'};

// m > a
int gcd (int m, int a)
{
    if (a == 0)
    {
        return m;
    }
    else
    {
        return gcd(a, m%a);
    }
}

// m > a
int q_mas_gcd (int m, int a, int q_mas[], int i)
{
    if (a == 0)
    {
        return m;
    }
    else
    {
        q_mas[i] = m/a;
        return q_mas_gcd(a, m%a, q_mas, i+1);
    }
}

// m > a
int revers_a (int a, int m)
{
    int q_mas[m];
    int v_mas[m];
    for (int i = 0; i < m; i++)
    {
        q_mas[i] = 0;
        v_mas[i] = 0;
    }
    v_mas[1] = 1;

    int gcd = q_mas_gcd(m,a,q_mas,0);
    if (gcd != 1)
    {
        /*cout << "Imposible to find revers_a because gcd(m,a) != 1" << endl;*/
        return 0;
    }
    else
    {
        int h = 1;
        int v_max = 0;
        while (q_mas[h]!=0)
        {
            v_mas[h+1] = v_mas[h-1] + (-1)*q_mas[h-1]*v_mas[h];
            v_max = v_mas[h+1];
            h++;
        }

        if (v_max < 0 )
        {
            v_max = v_max + m;
        }

        return v_max;
    }
}

//  a*x=b mod(n)      n > a    n > b
int find_x_linear (int a, int b, int n, int x_mas[])
{

    if (gcd(n,a) != 1)
    {
        return -1;
    }

    for(int i = 0; i < gcd(n,a); i++)
    {
        x_mas[i] = 0;
    }

    if (gcd(n,a) == 1)
    {
        int x;
        int reverse_a = revers_a(a, n);
        x = (reverse_a * b)%n;
        return x;
    }
    else
    {
        if (b%gcd(n,a) != 0)
        {
            return -1;
        }
        else
        {
            int x0;
            int a1 = a/gcd(n,a);
            int b1 = b/gcd(n,a);
            int n1 = n/gcd(n,a);
            int reverse_a1 = revers_a(a1, n1);
            x0 = (reverse_a1 * b1)%n1;
            for (int  i = 0; i < gcd(n,a); i++)
            {
                x_mas[i] = x0 + i*n1;
            }
            return -2;
        }
    }

}

void decryption (string text, int a, int b, char decrypted[])
{
    int y,y1,y2;
    int x,x1,x2;
    for (int i = 0; i < text.length()-1; i=i+2)
    {
        y1 = (int)text[i]+32;
        y2 = (int)text[i+1]+32;
        if (y1 > 26)
        {
            y1 = y1 - 1;
        }

        if (y2 > 26)
        {
            y2 = y2 - 1;
        }

        y = y1*31 + y2;

        x = ((revers_a(a,31*31))*(y-b))%(31*31);

        if (x < 0)
        {
            x = x + 31*31;
        }

        x1 = x/31;
        x2 = x%31;

        if (x1 >= 26)
        {
            x1 = x1 + 1;
        }

        if (x2 >= 26)
        {
            x2 = x2 + 1;
        }

        decrypted[i] = (char)(x1-32);
        decrypted[i+1] = (char)(x2-32);

        if (decrypted[i]=='ь')
        {
            decrypted[i]='ы';
        }
        else if (decrypted[i]=='ы')
        {
            decrypted[i]='ь';
        }
    }

    for (int  j = 0; j <= text.length(); j++)
    {
        if (decrypted[j]=='ь')
        {
            decrypted[j]='ы';
        }
        else if (decrypted[j]=='ы')
        {
            decrypted[j]='ь';
        }
    }
}

bool is_sensed (char encrypted[], string text)
{
    int a = 0;
    int o = 0;
    int e = 0;
    for (int i = 0; i < text.length(); i++)
    {
        if ((int)encrypted[i]== -32 )
        {
            a++;
        }
        else if ((int)encrypted[i]== -18)
        {
            o++;
        }
        else if ((int)encrypted[i]== -27)
        {
            e++;
        }
    }
    double ch_a, ch_o, ch_e;
    ch_a = (double)a/(double)text.length();
    ch_o = (double)o/(double)text.length();
    ch_e = (double)e/(double)text.length();

    if (ch_a >= 0.045 && ch_a <= 0.115 && ch_o >= 0.065 && ch_o <= 0.125 && ch_e >= 0.045 && ch_e <= 0.115)
    {
        cout << "Text may have meaning" << endl;
        cout << "A Frequency = " << ch_a << endl;
        cout << "O Frequency = " << ch_o << endl;
        cout << "E Frequency = " << ch_e << endl;
        return 1;
    }
    else
    {
        if (ch_a < 0.05 || ch_a > 0.11)
        {
            cout << "i am sory, but A Frequency = " << ch_a << endl;
        }
        else if (ch_o < 0.07 || ch_o > 0.12)
        {
            cout << "i am sory, but O Frequency = " << ch_o << endl;
        }
        else if (ch_e < 0.05 || ch_e > 0.11)
        {
            cout << "i am sory, but E Frequency = " << ch_e << endl;
        }
        return 0;
    }
}




int main (void)
{
    //считываем текст и переводим его в одну строку
    setlocale(LC_ALL,"Russian"); //что бы не біло абра кадабры вместо букв (хотя возможно єто и не надо и кодировка сама все исправила)
    string line;
    string encryptedtext;
    ifstream in2("C:\\Users\\User\\Desktop\\Учеба 5 семестр\\Криптография\\ЛР\\fb-labs-2020\\cp_3\\sereda_fb_81_cp3\\text.txt");
    while (getline(in2, line))
    {
        encryptedtext = encryptedtext + line;
    }
    in2.close();

    cout << encryptedtext << endl;

    for (int i = 0; i <= encryptedtext.length(); i++)
    {
        if (encryptedtext[i]=='ь')
        {
            encryptedtext[i]='ы';
        }
        else if (encryptedtext[i]=='ы')
        {
            encryptedtext[i]='ь';
        }
    }
    cout << encryptedtext << endl;


    int bigrams[32*32];
    for (int i = 0; i < 32*32; i++)
    {
        bigrams[i] = 0;
    }
    for (int i = 0; i < 32; i++)
    {
        for (int j = 0; j < 32; j++)
        {

            for (int l = 0; l <= encryptedtext.length(); l++)
            {
                if (encryptedtext[l]==(char)(-32+i))
                {
                    if (encryptedtext[l+1]==(char)(-32+j))
                    {
                        bigrams[32*i+j]=bigrams[32*i+j]+1;
                    }
                }
            }
        }
    }

    cout << "Колличество биграмм" << endl;
    for (int i = 0; i < 32; i++)
    {
        for (int j = 0; j < 32; j++)
        {
            cout << (char)(-32+i) << (char)(-32+j) << " " << bigrams[32*i+j] << endl;
        }
    }
    cout << "Всего биграмм " << encryptedtext.length() - 1  << endl;
    cout << endl;

    int max_bigram = 0;
    int max_i = 0;
    int max_j = 0;
    int cypher_bigrams[5];
    int open_bigrams[5] = {17*31+18,13*31+14,18*31+14,13*31+0,5*31+13};

    for (int l = 0; l < 5; l++)
    {
        max_bigram = 0;
        max_i = 0;
        max_j = 0;
        for (int i = 0; i < 32; i++)
        {
            for (int j = 0; j < 32; j++)
            {
                if (bigrams[32*i+j] >= max_bigram)
                {
                    max_bigram = bigrams[32*i+j];
                    max_i = i;
                    max_j = j;
                }
            }
        }
        cout << (char)(-32+max_i) << (char)(-32+max_j) << " " << max_bigram << endl;
        bigrams[32*max_i + max_j] = 0;

        if (max_i > 26)
        {
            max_i = max_i -1;
        }

        if (max_j > 26)
        {
            max_j = max_j -1;
        }

        cypher_bigrams[l] = max_i * 31 + max_j;
    }

    for (int i = 0; i < 5; i++)
    {
        cout << cypher_bigrams[i] << "   " << open_bigrams[i] << endl;
    }


    int ab_mas[31*31][2];
    for (int i = 0; i < 31*31; i++)
    {
        ab_mas[i][0] = 0;
        ab_mas[i][1] = 0;
    }

    cout << endl;
    int a, b, b1, m, x, counter = 0;
    for (int i1 = 0; i1 < 5; i1++)
    {
        for (int i2 = 0; i2 < 5; i2++)
        {
            if (i1 == i2)
            {
                i2++;
            }
            for (int j1 = 0; j1 < 5; j1++)
            {
                for (int j2 = 0; j2 < 5; j2++)
                {
                    if (j1 == j2)
                    {
                        j2++;//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    }
                    b = cypher_bigrams[j1] - cypher_bigrams[j2];
                    a = open_bigrams[i1] - open_bigrams[i2];

                    if (a < 0)
                    {
                        a = a + 31*31;
                    }

                    if (b < 0)
                    {
                        b = b + 31*31;
                    }

                    m = 31*31;
                    int x_mas[gcd(m,a)];
                    x = find_x_linear (a,b,m,x_mas);

                    if (x > -1)
                    {
                        ab_mas[counter][0] = x;
                        ab_mas[counter][1] = (cypher_bigrams[j1] - x*open_bigrams[i1])%(31*31);
                        if (ab_mas[counter][1] < 0)
                        {
                            ab_mas[counter][1] = ab_mas[counter][1] + 31*31;
                        }
                        counter++;
                    }
                    else if (x == -2)
                    {
                        for (int  i = 0; i < gcd(m,a); i++)
                        {
                            ab_mas[counter][0] = x_mas[i];
                            ab_mas[counter][1] = (cypher_bigrams[j1] - x_mas[i]*open_bigrams[i1])%(31*31);
                            counter++;
                        }
                    }
                }
            }
        }
    }

    for (int i = 0; i < counter; i++)
    {
        for (int j = 0; j < counter; j++)
        {
            if(i==j)
            {
                j++;
            }

            if (ab_mas[i][0] == ab_mas[j][0] && ab_mas[i][1] == ab_mas[j][1])
            {
                ab_mas[j][0] = -1;
                ab_mas[j][1] = -1;
            }

            if (gcd(31*31,ab_mas[i][0]) != 1)
            {
                ab_mas[i][0] = -1;
                ab_mas[i][1] = -1;
            }
        }
    }


    cout << "a    b" << endl;
    for (int i = 0; i < counter; i++)
    {
        /*if (gcd(31*31, ab_mas[i][0])==1)
        {*/
            cout << ab_mas[i][0] << " " << ab_mas[i][1] << endl;
        /*}
        else
        {
            cout << "gcd(31*31," << ab_mas[i][0] << ") = " << gcd(31*31, ab_mas[i][0]) << " != 1" << endl;
        }*/
    }

    char decryptedtext[encryptedtext.length()];
    bool flag;
    for (int i = 0; i < counter; i++)
    {
        /*if (gcd(31*31,ab_mas[i][0]) != 1)
        {
            i++;
        }*/
        if (ab_mas[i][0] != -1 && ab_mas[i][1] != -1)
        {
            decryption(encryptedtext, ab_mas[i][0], ab_mas[i][1], decryptedtext);
            flag = is_sensed(decryptedtext, encryptedtext);
            if (flag == 1)
            {
                cout << "a = " << ab_mas[i][0] << "  b = " << ab_mas[i][1] << endl;
                for (int j = 0; j < encryptedtext.length(); j++)
                {
                    cout << decryptedtext[j];
                }
                cout << endl << endl;
            }
        }
    }

    return 0;
}
