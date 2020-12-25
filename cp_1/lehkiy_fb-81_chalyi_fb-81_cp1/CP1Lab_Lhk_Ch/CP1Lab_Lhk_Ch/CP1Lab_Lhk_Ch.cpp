// CP1Lab_Lhk_Ch.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include "pch.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>


using namespace std;

void remove_symbols(char* ftext, char* wtext,int mode);
void count_freq_monogr(char* wtext, float* cont, int mode);
void count_freq_bigr(char* wtext, float** cont, float** cont2, int mode);
float entrophy_for_monogr(float* cont);
float entrophy_for_bigr(float** cont);


int main()
{
	setlocale(LC_ALL, "");

	char *filetext = new char[10000000];
	char *worktext = new char[10000000];
	char *worktext_without_spaces = new char[10000000];
	char *worktext_step1 = new char[10000000];
	float *freq_mono = new float[32];
	float **freq_bi_cross = new float*[32];
	float **freq_bi = new float*[32];

	for (int i = 0; i < 32; i++)
	{
		freq_mono[i] = 0.0;
	}
	for (int k = 0; k < 32; k++)
	{
		freq_bi_cross[k] = new float[32];
		freq_bi[k] = new float[32];
		for (int i = 0; i < 32; i++)
		{
			freq_bi_cross[k][i] = 0.0;
			freq_bi[k][i] = 0.0;
		}
	}

	ifstream fin("text.txt");

	fin.read(filetext, 10000000);
	fin.close();
	remove_symbols(filetext, worktext,0);
	remove_symbols(filetext, worktext_without_spaces, 1);
	count_freq_monogr(worktext, freq_mono, 1);
	count_freq_bigr(worktext, freq_bi_cross, freq_bi ,1);
	ofstream fout1("monograms_with_spaces.txt");
	for (int i = 0; i < 32; i++)
	{
		if ((char)('а' + i) == 'ъ')
		{
			fout1 << ' ' << '=';
			fout1 << freq_mono[i] << endl;
		}
		else {
			fout1 << (char)('а' + i) << '=';
			fout1 << freq_mono[i] << endl;
		}

	}
	fout1.close();
	ofstream fout2("bigrams_with_spaces_crossed.txt");
	
	for (int k = 0; k < 32; k++)
	{
		for (int j = 0; j < 32; j++)
		{
			if (freq_bi_cross[k][j] != 0) {
				if ((char)('а' + k) == 'ъ')
					fout2 << ' ';
				else
					fout2 << (char)('а' + k);
				if ((char)('а' + j) == 'ъ')
				{
					fout2 << ' ' << '=';
					fout2 << freq_bi_cross[k][j] <<  endl;
				}
				else {
					fout2 << (char)('а' + j) << '=';
					fout2 << freq_bi_cross[k][j] << endl;
				}
			}
		}
	}
	fout2.close();
	ofstream fout5("bigrams_with_spaces_not_crossed.txt");

	for (int k = 0; k < 32; k++)
	{
		for (int j = 0; j < 32; j++)
		{
			//if (freq_bi[k][j] != 0) {
				if ((char)('а' + k) == 'ъ')
					fout5 << ' ';
				else
					fout5 << (char)('а' + k);
				if ((char)('а' + j) == 'ъ')
				{
					fout5 << ' ' << '=';
					fout5 << freq_bi[k][j] << endl;
				}
				else {
					fout5 << (char)('а' + j) << '=';
					fout5 << freq_bi[k][j] << endl;
				//}
			}
		}
	}
	fout5.close();
	float entr1 = entrophy_for_monogr(freq_mono);
	float entr2 = entrophy_for_bigr(freq_bi_cross);
	float entr5 = entrophy_for_bigr(freq_bi);

	count_freq_monogr(worktext_without_spaces, freq_mono, 0);
	count_freq_bigr(worktext_without_spaces, freq_bi_cross, freq_bi, 0);
	ofstream fout3("monograms_without_spaces.txt");
	for (int i = 0; i < 32; i++)
	{
		if ((char)('а' + i) == 'ъ')
		{
			fout3 << ' ' << '=';
			fout3 << freq_mono[i] << endl;
		}
		else {
			fout3 << (char)('а' + i) << '=';
			fout3 << freq_mono[i] << endl;
		}

	}
	fout3.close();
	ofstream fout4("bigrams_without_spaces_crossed.txt");
	
	for (int k = 0; k < 32; k++)
	{
		for (int j = 0; j < 32; j++)
		{
			if (freq_bi_cross[k][j] != 0) {
				if ((char)('а' + k) == 'ъ')
					fout4 << ' ';
				else
					fout4 << (char)('а' + k);
				if ((char)('а' + j) == 'ъ')
				{
					fout4 << ' ' << '=';
					fout4 << freq_bi_cross[k][j] << endl;
				}
				else {
					fout4 << (char)('а' + j) << '=';
					fout4 << freq_bi_cross[k][j] << endl;
				}
			}
		}
	}
	fout4.close();
	ofstream fout6("bigrams_without_spaces_not_crossed.txt");

	for (int k = 0; k < 32; k++)
	{
		for (int j = 0; j < 32; j++)
		{
			//if (freq_bi[k][j] != 0) {
				if ((char)('а' + k) == 'ъ')
					fout6 << ' ';
				else
					fout6 << (char)('а' + k);
				if ((char)('а' + j) == 'ъ')
				{
					fout6 << ' ' << '=';
					fout6 << freq_bi[k][j] << endl;
				}
				else {
					fout6 << (char)('а' + j) << '=';
					fout6 << freq_bi[k][j] << endl;
				}
			//}
		}
	}
	fout6.close();
	float entr3 = entrophy_for_monogr(freq_mono);
	float entr4 = entrophy_for_bigr(freq_bi_cross);
	float entr6 = entrophy_for_bigr(freq_bi);
	ofstream fout7("entrophy.txt");
	fout7 << "H1 с пробелами = " << entr1 << endl;
	fout7 << "H2 сплошная с пробелами = " << entr2 << endl;
	fout7 << "H2 с шагом с пробелами = " << entr5 << endl;
	fout7 << "H1 без пробелов = " << entr3 << endl;
	fout7 << "H2 сплошная без пробелов  = " << entr4 << endl;
	fout7 << "H2 с шагом без пробелов  = " << entr6 << endl;
	fout7.close();
	int a = 0;
	
	
}

void remove_symbols(char* ftext, char* wtext, int mode)
{ 
	int64_t i = 0;
	int64_t j = 0;
	
	
	while (ftext[i] != 'Z' ){
		if (ftext[i] == 'ё') ftext[i] = 'е';
		if (ftext[i] == 'ъ') ftext[i] = 'ь';
		if (ftext[i] >= 'а' && ftext[i] <= 'я')
			wtext[j++] = ftext[i];

		else if (ftext[i] >= 'А' && ftext[i] <= 'Я')
			wtext[j++] = ftext[i] + 32;
		else if (mode == 0) {
		 if ((ftext[i] == ' ' || ftext[i] == '\t' || ftext[i] == '\n' ) && wtext[j - 1] != ' ')
			wtext[j++] = ' ';
		}
		i++;
	}
	wtext[j] = 'Z';
	
	
}

void count_freq_monogr(char* wtext, float* cont, int mode) {
	for (int a = 0; a < 32; a++)
	{
		cont[a] = 0.0;
	}
	int i = 0;
	int text_size = 0;
	while (wtext[i] != 'Z')
	{
		if (mode == 1) {
			if (wtext[i] == ' ') cont[26] += 1.0;
			else  cont[(int)wtext[i] + 32] += 1.0;

			text_size++;
		}
		else if (wtext[i] != ' ') {
			cont[(int)wtext[i] + 32] += 1.0;
			text_size++;
		}
		i++;
	}
	for (int j = 0; j < 32; j++)
	{
		cont[j] = cont[j] / text_size;
	}
}

void count_freq_bigr(char* wtext, float** cont, float** cont2, int mode) {
	for (int y = 0; y < 32; y++)
	{
		for (int b = 0; b < 32; b++)
		{
			cont[y][b] = 0.0;
			cont2[y][b] = 0.0;
		}
	}
	int i = 0;
	int text_size = 0;
	while (wtext[i + 1] != 'Z')
	{
		if (mode == 1) {
			if (wtext[i] == ' ') cont[26][(int)wtext[i + 1] + 32] += 1.0;
			else if (wtext[i + 1] == ' ') cont[(int)wtext[i] + 32][26] += 1.0;
			else  cont[(int)wtext[i] + 32][(int)wtext[i + 1] + 32] += 1.0;

			text_size++;
		}
		else if (wtext[i] != ' ')
		{
			cont[(int)wtext[i] + 32][(int)wtext[i + 1] + 32] += 1.0;
			text_size++;
		}
		i++;
	}
	int z = 2;
	int text_size2 = 0;
	while (wtext[z] != 'Z')
	{
		if (mode == 1) {
			if(wtext[z-2] == ' ' && wtext[z] == ' ') cont2[26][26] += 1.0;
			else if (wtext[z-2] == ' ') cont2[26][(int)wtext[z] + 32] += 1.0;
			else if (wtext[z] == ' ') cont2[(int)wtext[z-2] + 32][26] += 1.0;
			else  cont2[(int)wtext[z-2] + 32][(int)wtext[z] + 32] += 1.0;
			text_size2++;
		}
		else if (wtext[z] != ' ') {
			cont2[(int)wtext[z-2] + 32][(int)wtext[z] + 32] += 1.0;
			text_size2++;
		}	
		z++;
		
	}
	for (int k = 0; k < 32; k++)
	{
		for (int j = 0; j < 32; j++)
		{
			cont[k][j] = cont[k][j] / (float)text_size;
			cont2[k][j] = cont2[k][j] / (float)text_size2;
		}
	}
}

float entrophy_for_monogr(float* cont)
{
	float count = 0.0;
	for (int i = 0; i < 32; i++)
	{
		if (cont[i] != 0)
			count += cont[i] * log2(cont[i]);
	}
	return -count;
}
float entrophy_for_bigr(float** cont)
{
	float count = 0.0;
	for (int k = 0; k < 32; k++)
	{
		for (int i = 0; i < 32; i++)
		{
			if (cont[k][i] != 0)
				count += (cont[k][i] * log2(cont[k][i]))/2;
		}
	}
	return -count;
}


// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
