#include <iostream>
#include <stdio.h>
#include <cmath>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

int main (void)
{
    //считываем текст и переводим его в одну строку
    setlocale(LC_ALL,"Russian"); //что бы не біло абра кадабры вместо букв (хотя возможно єто и не надо и кодировка сама все исправила)
    string line;
    string fullstring;
    ifstream in2("C:\\Users\\User\\Desktop\\Учеба 5 семестр\\Криптография\\ЛР\\fb-labs-2020\\cp_1\\sereda_fb-81_cp1\\text.txt");
    while (getline(in2, line))
    {
        fullstring = fullstring + line;
    }
    in2.close();


    //редактируем текст убираем знаки препинания
    for (int i = 0; i <= fullstring.length(); i++)
    {
        if (fullstring[i]=='1' || fullstring[i]=='2' || fullstring[i]=='3' || fullstring[i]=='4' || fullstring[i]=='5' || fullstring[i]=='6' || fullstring[i]=='7' || fullstring[i]=='8' || fullstring[i]=='9' || fullstring[i]=='0' || fullstring[i]=='.' || fullstring[i]==',' || fullstring[i]=='–' || fullstring[i]=='?' || fullstring[i]=='!' || fullstring[i]==')' || fullstring[i]=='(' || fullstring[i]=='-' || fullstring[i]=='"' || fullstring[i]==':')
        {
            fullstring[i]=' ';
        }
    }


    //редактируем текст убираем двойные пробелы
    //флаг для того что бы если мы вдруг не стерли ничего при последней попытке, то и дальше прогонять нет смысла
    int flag = 1;
    while (flag == 1)
    {
        flag = 0;
        for (int i = 0; i <= fullstring.length(); i++)
        {
            if (fullstring[i]==' ' && fullstring[i+1]==' ')
            {
                fullstring.erase(i,1);
                flag = 1;
                break;
            }
        }
    }


    //редактируем текст превращаем большие буквы в маленькие
    for (int i = 0; i <= fullstring.length(); i++)
    {
        switch (fullstring[i])
        {
        case 'А':
            fullstring[i] = 'а';
            break;
        case 'Б':
            fullstring[i] = 'б';
            break;
        case 'В':
            fullstring[i] = 'в';
            break;
        case 'Г':
            fullstring[i] = 'г';
            break;
        case 'Д':
            fullstring[i] = 'д';
            break;
        case 'Е':
            fullstring[i] = 'е';
            break;
        case 'Ё':
            fullstring[i] = 'е';
            break;
        case 'Ж':
            fullstring[i] = 'ж';
            break;
        case 'З':
            fullstring[i] = 'з';
            break;
        case 'И':
            fullstring[i] = 'и';
            break;
        case 'Й':
            fullstring[i] = 'й';
            break;
        case 'К':
            fullstring[i] = 'к';
            break;
        case 'Л':
            fullstring[i] = 'л';
            break;
        case 'М':
            fullstring[i] = 'м';
            break;
        case 'Н':
            fullstring[i] = 'н';
            break;
        case 'О':
            fullstring[i] = 'о';
            break;
        case 'П':
            fullstring[i] = 'п';
            break;
        case 'Р':
            fullstring[i] = 'р';
            break;
        case 'С':
            fullstring[i] = 'с';
            break;
        case 'Т':
            fullstring[i] = 'т';
            break;
        case 'У':
            fullstring[i] = 'у';
            break;
        case 'Ф':
            fullstring[i] = 'ф';
            break;
        case 'Х':
            fullstring[i] = 'х';
            break;
        case 'Ц':
            fullstring[i] = 'ц';
            break;
        case 'Ч':
            fullstring[i] = 'ч';
            break;
        case 'Ш':
            fullstring[i] = 'ш';
            break;
        case 'Щ':
            fullstring[i] = 'щ';
            break;
        case 'Ъ':
            fullstring[i] = 'ъ';
            break;
        case 'Ы':
            fullstring[i] = 'ы';
            break;
        case 'Ь':
            fullstring[i] = 'ь';
            break;
        case 'Э':
            fullstring[i] = 'э';
            break;
        case 'Ю':
            fullstring[i] = 'ю';
            break;
        case 'Я':
            fullstring[i] = 'я';
            break;
        case 'ё':
            fullstring[i] = 'е';
            break;
        default:
            break;
        }
    }
    /*cout << "Текст" << endl;
    cout << fullstring << endl;*/


    //пора считать буквы
    int letters_with_space [33];
    int total1 = 0;
    for (int i = 0; i <= 32; i++)
    {
        letters_with_space[i] = 0;
    }
    for (int i = 0; i<= 31; i++)
    {
        for (int j = 0; j <= fullstring.length(); j++)
        {
            if ((int)fullstring[j]==(int)'а'+i)
            {
                letters_with_space[i]=letters_with_space[i]+1;
                total1 = total1 + 1;
            }
        }
    }
    //отдельно считаем пробел
    for (int j = 0; j <= fullstring.length(); j++)
        {
            if ((int)fullstring[j]==32)
            {
                letters_with_space[32]=letters_with_space[32]+1;
                total1 = total1 + 1;
            }
        }
    cout << endl;
    /*cout << "Колличество букв с пробелом" << endl;
    for (int i = 0; i <= 32; i++)
    {
        cout << (char)(-32+i) << " " << letters_with_space[i] << endl;
    }
    cout << endl << "Total symbols " << total1 << endl;*/


    //теперь считаем их частоты
    double chastota_bukv_probel[33];
    for (int i = 0; i <= 32; i++)
    {
        chastota_bukv_probel[i] = (double)letters_with_space[i]/(double)fullstring.length();
    }
    cout << endl;
    cout << "Частота букв с пробелом" << endl;
    for (int i = 0; i <= 32; i++)
    {
        cout /*<< (char)(-32+i) << " "*/ << chastota_bukv_probel[i] << endl;
    }
    cout << endl;


    //теперь без пробелов
    //тут все почти как с пробелами, но до самого пробела в массиве letters_with_space мы не доходим, и от общего колличества букв отнимаем колличество пробелов
    double chastota_bukv[32];
    int total2 = total1 - letters_with_space[32];
    for (int i = 0; i <= 31; i++)
    {
        chastota_bukv[i] = (double)letters_with_space[i]/(double)(fullstring.length()-letters_with_space[32]);
    }
    cout << endl;
    cout << "Частота букв без пробелом" << endl;
    for (int i = 0; i <= 31; i++)
    {
        cout /*<< (char)(-32+i) << " "*/ << chastota_bukv[i] << endl;
    }
    cout << endl;


    //теперь выведем эти же массивы, но в отсортированом виде
    //уже написав всё ето я вспомнил что можно выводить и в алфоыитном порядке, поетому решил это пока закоментить
    /*cout << "Частота букв с пробелом отсортирована" << endl;
    double max1=0.0;
    int max1_index=0;
    cout << (char)(32) << " " << chastota_bukv_probel[32] << endl;
    for (int j = 0; j<=31; j++)
    {
        for (int i = 0; i <= 31; i++)
        {
            if (chastota_bukv_probel[i] >= max1)
            {
                max1 = chastota_bukv_probel[i];
                max1_index = i;
            }
        }
        cout << (char)(-32+max1_index) << " " << max1 << endl;
        chastota_bukv_probel[max1_index]=-1.0;
        max1 = 0.0;
        max1_index = 0;
    }
    cout << endl;

    cout << "Частота букв без пробелом отсортирована" << endl;
    double max2=0.0;
    int max2_index=0;
    for (int j = 0; j<=31; j++)
    {
        for (int i = 0; i <= 31; i++)
        {
            if (chastota_bukv[i] >= max2)
            {
                max2 = chastota_bukv[i];
                max2_index = i;
            }
        }
        cout << (char)(-32+max2_index) << " " << max2 << endl;
        chastota_bukv[max2_index]=-1.0;
        max2 = 0.0;
        max2_index = 0;
    }
    cout << endl;*/


    //считаем колличество биграмм
    int bigrams1_with_space [33*33];
    int total3 = 0;
    for (int i = 0; i <= 33*33-1; i++)
    {
        bigrams1_with_space[i] = 0;
    }
    for (int i = 0; i <= 32; i++)
    {
        int a = -32;
        if (i==32)
        {
            a=0; //это пробел
        }
        for (int j = 0; j <= 32; j++)
        {
            int b = -32;
            if (j==32)
            {
                b=0; //это пробел
            }
            for (int l = 0; l <= fullstring.length(); l++)
            {
                if (fullstring[l]==(char)(a+i))
                {
                    if (fullstring[l+1]==(char)(b+j))
                    {
                        bigrams1_with_space[33*i+j]=bigrams1_with_space[33*i+j]+1;
                        total3 = total3 + 1;
                    }
                }
            }
        }
    }
    cout << endl;

    /*cout << "Колличество биграмм с пробелом" << endl;
    for (int i = 0; i <= 32; i++)
    {
        int a = -32;
        if (i == 32)
        {
            a=0;
        }
        for (int j = 0; j <= 32; j++)
        {
            int b = -32;
            if (j == 32)
            {
                b = 0;
            }
            cout << (char)(a+i) << (char)(b+j) << " " << bigrams1_with_space[33*i+j] << endl;
        }
    }*/
    /*cout << "Всего биграмм с пробелом " << total3 << endl;*/


    double chastota_bigram1_probel[33*33];
    for (int i = 0; i <= 32; i++)
    {
        for (int j = 0; j <= 32; j++)
        {
            chastota_bigram1_probel[33*i+j] = (double)bigrams1_with_space[33*i+j]/(double)total3;
        }
    }

    cout << "Частота биграмм с пробелом" << endl;
    for (int i = 0; i <= 32; i++)
    {
        /*cout << endl << char(-32+i) << endl;*/
        int a = -32;
        if (i == 32)
        {
            a=0;
        }
        for (int j = 0; j <= 32; j++)
        {
            int b = -32;
            if (j == 32)
            {
                b = 0;
            }
            cout << (char)(a+i) << (char)(b+j) << " " << chastota_bigram1_probel[33*i+j] << endl;
        }
    }
    cout << endl;


    // теперь считаем биграммы без пересечений, пока тоже с пробелом
    int bigrams2_with_space [33*33];
    int total4 = 0;
    for (int i = 0; i <= 33*33-1; i++)
    {
        bigrams2_with_space[i] = 0;
    }
    for (int i = 0; i <= 32; i++)
    {
        int a = -32;
        if (i==32)
        {
            a=0; //это пробел
        }
        for (int j = 0; j <= 32; j++)
        {
            int b = -32;
            if (j==32)
            {
                b=0; //это пробел
            }
            for (int k = 0; k <= fullstring.length(); k=k+2)
            {
                if (fullstring[k]==(char)(a+i))
                {
                    if (fullstring[k+1]==(char)(b+j))
                    {
                        bigrams2_with_space[33*i+j]=bigrams2_with_space[33*i+j]+1;
                        total4 = total4 + 1;
                    }
                }
            }
        }
    }
    cout << endl;

    /*cout << "Колличество биграмм без пересечений с пробелом" << endl;
    for (int i = 0; i <= 32; i++)
    {
        int a = -32;
        if (i == 32)
        {
            a=0;
        }
        for (int j = 0; j <= 32; j++)
        {
            int b = -32;
            if (j == 32)
            {
                b = 0;
            }
            cout << (char)(a+i) << (char)(b+j) << " " << bigrams2_with_space[33*i+j] << endl;
        }
    }
    cout << "Всего биграмм без пересечений с пробелом " << total4 << endl;*/


    double chastota_bigram2_probel[33*33];
    for (int i = 0; i <= 32; i++)
    {
        for (int j = 0; j <= 32; j++)
        {
            chastota_bigram2_probel[33*i+j] = (double)bigrams2_with_space[33*i+j]/(double)(total4);
        }
    }

    cout << "Частота биграмм без пересечений с пробелом" << endl;
    for (int i = 0; i <= 32; i++)
    {
        /*cout << endl << char(-32+i) << endl;*/
        int a = -32;
        if (i == 32)
        {
            a=0;
        }
        for (int j = 0; j <= 32; j++)
        {
            int b = -32;
            if (j == 32)
            {
                b = 0;
            }
            cout << (char)(a+i) << (char)(b+j) << " " << chastota_bigram2_probel[33*i+j] << endl;
        }
    }
    cout << endl;


    // пришло время убрать пробелы
    for (int i = 0; i <= fullstring.length(); i++)
    {
        if (fullstring[i]== ' ')
        {
            fullstring.erase(i,1);
        }
    }
    /*cout << endl << fullstring << endl;*/


    //считаeм биграммы
    int bigrams1_without_space [32*32];
    int total5 = 0;
    for (int i = 0; i <= 32*32-1; i++)
    {
        bigrams1_without_space[i] = 0;
    }
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {

            for (int l = 0; l <= fullstring.length(); l++)
            {
                if (fullstring[l]==(char)(-32+i))
                {
                    if (fullstring[l+1]==(char)(-32+j))
                    {
                        bigrams1_without_space[32*i+j]=bigrams1_without_space[32*i+j]+1;
                        total5 = total5 + 1;
                    }
                }
            }
        }
    }
    cout << endl;

    /*cout << "Колличество биграмм без пробела" << endl;
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {
            cout << (char)(-32+i) << (char)(-32+j) << " " << bigrams1_without_space[32*i+j] << endl;
        }
    }
    cout << "Всего биграмм без пробела " << total5 << endl;*/


    double chastota_bigram1_bes_probel[32*32];
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {
            chastota_bigram1_bes_probel[32*i+j] = (double)bigrams1_without_space[32*i+j]/(double)(total5);
        }
    }
    cout << endl;

    cout << "Частота биграмм без пробела" << endl;
    for (int i = 0; i <= 31; i++)
    {
        /*cout << endl << char(-32+i) << endl;*/
        for (int j = 0; j <= 31; j++)
        {
            cout << (char)(-32+i) << (char)(-32+j) << " " << chastota_bigram1_bes_probel[32*i+j] << endl;
        }
    }
    cout << endl;

    //теперь без пересечений
    int bigrams2_without_space [32*32];
    int total6 = 0;
    for (int i = 0; i <= 32*32-1; i++)
    {
        bigrams2_without_space[i] = 0;
    }
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {

            for (int l = 0; l <= fullstring.length(); l=l+2)
            {
                if (fullstring[l]==(char)(-32+i))
                {
                    if (fullstring[l+1]==(char)(-32+j))
                    {
                        bigrams2_without_space[32*i+j]=bigrams2_without_space[32*i+j]+1;
                        total6 = total6 + 1;
                    }
                }
            }
        }
    }
    cout << endl;

    /*cout << "Колличество биграмм без пересечений без пробела" << endl;
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {
            cout << (char)(-32+i) << (char)(-32+j) << " " << bigrams2_without_space[32*i+j] << endl;
        }
    }
    cout << "Всего биграмм без пересечений без пробела " << total6 << endl;*/


    double chastota_bigram2_bes_probel[32*32];
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {
            chastota_bigram2_bes_probel[32*i+j] = (double)bigrams2_without_space[32*i+j]/(double)(total6);
        }
    }
    cout << endl;

    cout << "Частота биграмм без пересечений без пробела" << endl;
    for (int i = 0; i <= 31; i++)
    {
        /*cout << endl << char(-32+i) << endl;*/
        for (int j = 0; j <= 31; j++)
        {
            cout << (char)(-32+i) << (char)(-32+j) << " " << chastota_bigram2_bes_probel[32*i+j] << endl;
        }
    }
    cout << endl;

    cout << endl;
    cout << "Букв с пробелом: " << total1 << endl;
    cout << "Букв без пробела: " << total2 << endl;
    cout << "Биграмм с пробелом: " << total3 << endl;
    cout << "Биграмм без пробела: " << total5 << endl;
    cout << "Биграмм через один с пробелом: " << total4 << endl;
    cout << "Биграмм через один без пробела: " << total6 << endl;
    cout << endl;


    //пришло время считать ентропию
    double entropy1 = 0;
    for (int i = 0; i <= 32; i ++)
    {
        if (chastota_bukv_probel[i] != 0)
        {
            entropy1 = entropy1 + (chastota_bukv_probel[i]*(log(chastota_bukv_probel[i])/log(2)));
        }
    }
    cout << endl << "Ентропия унограмм с пробелом: "<< (-1)*entropy1 << endl << "Максимальная ентропия: " << log(33)/log(2);

    double entropy2 = 0;
    for (int i = 0; i <= 31; i ++)
    {
        if (chastota_bukv[i] != 0)
        {
            entropy2 = entropy2 + (chastota_bukv[i]*(log(chastota_bukv[i])/log(2)));
        }
    }
    cout << endl << "Ентропия унограмм без пробела: "<< (-1)*entropy2 << endl << "Максимальная ентропия: " << log(32)/log(2);



    double entropy3 = 0;
    for (int i = 0; i <= 32; i++)
    {
        for (int j = 0; j <= 32; j++)
        {
            if (chastota_bigram1_probel[33*i+j] != 0)
            {
                entropy3 = entropy3 + (chastota_bigram1_probel[33*i+j]*(log(chastota_bigram1_probel[33*i+j])/log(2)));
            }
        }
    }
    cout << endl << "Ентропия биграмм с пробелом: "<< (-0.5)*entropy3 << endl << "Максимальная ентропия: " << log(33*33)/log(2);

    double entropy4 = 0;
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {
            if (chastota_bigram1_bes_probel[32*i+j] != 0)
            {
                entropy4 = entropy4 + (chastota_bigram1_bes_probel[32*i+j]*(log(chastota_bigram1_bes_probel[32*i+j])/log(2)));
            }
        }
    }
    cout << endl << "Ентропия биграмм без пробела: "<< (-0.5)*entropy4 << endl << "Максимальная ентропия: " << log(32*32)/log(2);

    double entropy5 = 0;
    for (int i = 0; i <= 32; i++)
    {
        for (int j = 0; j <= 32; j++)
        {
            if (chastota_bigram2_probel[33*i+j] != 0)
            {
                entropy5 = entropy5 + (chastota_bigram2_probel[33*i+j]*(log(chastota_bigram2_probel[33*i+j])/log(2)));
            }
        }
    }
    cout << endl << "Ентропия биграмм через один с пробелом: "<< (-0.5)*entropy5 << endl << "Максимальная ентропия: " << log(33*33)/log(2);

    double entropy6 = 0;
    for (int i = 0; i <= 31; i++)
    {
        for (int j = 0; j <= 31; j++)
        {
            if (chastota_bigram2_bes_probel[32*i+j] != 0)
            {
                entropy6 = entropy6 + (chastota_bigram2_bes_probel[32*i+j]*(log(chastota_bigram2_bes_probel[32*i+j])/log(2)));
            }
        }
    }
    cout << endl << "Ентропия биграмм через один без пробела: "<< (-0.5)*entropy6 << endl << "Максимальная ентропия: " << log(32*32)/log(2);


    //считаем избточность
    double R1 = 0, R2 = 0, R3 = 0, R4 = 0, R5 = 0, R6 = 0;
    cout << endl << endl << "R1 = " << 1-(-1)*entropy1/(log(33)/log(2));
    cout << endl << "R2 = " << 1-(-1)*entropy2/(log(32)/log(2));
    cout << endl << "R3 = " << 1-(-0.5)*entropy3/(log(33)/log(2));
    cout << endl << "R4 = " << 1-(-0.5)*entropy4/(log(32)/log(2));
    cout << endl << "R5 = " << 1-(-0.5)*entropy5/(log(33)/log(2));
    cout << endl << "R6 = " << 1-(-0.5)*entropy6/(log(32)/log(2));

    /*cout << endl << endl << 1-(1.7547)/(log(32)/log(2)) << " " << 1-(2.4529)/(log(32)/log(2));
    cout << endl << 1-(2.5119)/(log(32)/log(2)) << " " << 1-(3.093)/(log(32)/log(2));
    cout << endl << 1-(1.2676)/(log(32)/log(2)) << " " << 1-(2.0552)/(log(32)/log(2));*/


    return 0;
}
// у нас есть 32 буквы (без Ё) и 33й пробел
