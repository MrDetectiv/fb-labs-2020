// Visioner.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<fstream>
#include<string>
#include<cmath>
#include <sstream>
#include <windows.h>

using namespace std;
const int n = 255;

int symbol_count;
char *symbol_array = new char[symbol_count];

void encrypt(string key, string text_string, ofstream &out)
{

	int j = 0, z;
	for (int i = 0; i < text_string.length(); i++)
	{
		if (int(text_string[i]) == 32 || int(text_string[i]) == 10)
			out << text_string[i];
		else {
			if (j < key.length())
			{
				z = (int(text_string[i]) + int(key[j])) % 32;
				if (z == 0)
				{
					z = -32;
					out << char(z);

				}
				else
				{
					out << char(z);
				}
			}

			if (j == key.length())
			{
				j = 0;
				z = (int(text_string[i]) + int(key[j])) % 32;
				if (z == 0)
				{
					z = -32;
					out << char(z);

				}
				else
				{
					out << char(z);
				}

			}
			j++;
		}
	}
}


void fun_in(ifstream &myfile, ofstream &out)
{

		stringstream string_stream;
		string_stream << myfile.rdbuf();
		string text_string = string_stream.str();
		myfile.close();
		int symbol_count;
		symbol_count = text_string.length();
		symbol_array = new char[symbol_count];
		text_string.copy(symbol_array, symbol_count);


		char symbols[n];     // масив символів без повторень
		double chance[n];   // частота символів
		int symbolsLenth = 0;


	
		for (int i = 0; i < symbol_count; i++)
		{
			int flg = 0;
			for (int j = 0; j < symbolsLenth; j++) {
				if (symbol_array[i] == symbols[j]) {
					chance[j]++; //якщо символи однакові збільчуємо частоту
					flg = 1;
					break;
				}
			}
			if (!flg)
			{
				chance[symbolsLenth] = 1.0;
				symbols[symbolsLenth] = symbol_array[i];
				symbolsLenth++;
			}
		}

	
		int z = 0;
		for (int i = 0; i < symbol_count; i++)
		{
			if (symbol_array[i] == ' ')
				z++;

		}
		int count = symbol_count - z;
		
			float  I, sum = 0;

			for (int i = 0; i < symbolsLenth; i++)
			{

				if (symbols[i] != ' ')
				{
					sum = sum + chance[i] * (chance[i]- 1)/(count*(count-1));
				}
			}
		
			I = sum;
			out << "Индекс = " <<  I << '\n' << '\n';
	
}


void fun_oi( ofstream &out, string text_string)
{

	
	int symbol_count;
	symbol_count = text_string.length();
	symbol_array = new char[symbol_count];
	text_string.copy(symbol_array, symbol_count);


	char symbols[n];     // масив символів без повторень
	double chance[n];   // частота символів
	int symbolsLenth = 0;



	for (int i = 0; i < symbol_count; i++)
	{
		int flg = 0;
		for (int j = 0; j < symbolsLenth; j++) {
			if (symbol_array[i] == symbols[j]) {
				chance[j]++; //якщо символи однакові збільчуємо частоту
				flg = 1;
				break;
			}
		}
		if (!flg)
		{
			chance[symbolsLenth] = 1.0;
			symbols[symbolsLenth] = symbol_array[i];
			symbolsLenth++;
		}
	}


	int z = 0;
	for (int i = 0; i < symbol_count; i++)
	{
		if (symbol_array[i] == ' ')
			z++;

	}
	int count = symbol_count - z;
	cout << count;
	float sum = 0;
	
	out << "Частота символов:\n";
	for (int i = 0; i < symbolsLenth; i++)
	{ 
		if (symbols[i] != ' ') 
		{
			sum = sum + (chance[i] / count)*(chance[i] / count);
		
		}
	}
	out << sum << endl;





	
}



int main()
{
	
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "rus");
	
	
	cout << "Укажите имя файла: " << endl;
	char name[40];
	cin.getline(name, 40);
	string key2,key3,key4,key5, key15;
	key2 = "дн"; key3 = "рим";
	key4 = "море"; key5 = "хорош";
	key15 = "всебудедобретут";
	ifstream myfile(name, ios::app);
	ofstream out2,out3,out4, out5,out15, i1;
	out2.open("key2.txt");
	out3.open("key3.txt");
	out4.open("key4.txt");
	out5.open("key5.txt");
	out15.open("key15.txt");
	i1.open("index1.txt");
	string text_string;

	if (myfile.is_open())
	{
		stringstream string_stream;

		string_stream << myfile.rdbuf();
		text_string = string_stream.str();
		myfile.close();
		encrypt(key2,  text_string, out2);
		encrypt(key3,  text_string, out3);
		encrypt( key4, text_string, out4);
		encrypt(key5, text_string, out5);
		encrypt(key15, text_string, out15);
		fun_oi( i1, text_string);
	}
	out2.close();
	out3.close();
	out4.close();
	out5.close();
	out15.close();
	
	ifstream file;
	ofstream i2, i3, i4, i5, i15;
	i2.open("index2.txt");
	i3.open("index3.txt");
	i4.open("index4.txt");
	i5.open("index5.txt");
	i15.open("index15.txt");
	file.open("key2.txt");
	fun_in(file, i2);
	file.close();
	file.open("key3.txt");
	fun_in(file, i3);
	file.close();
	file.open("key4.txt");
	fun_in(file, i4);
	file.close();
	file.open("key5.txt");
	fun_in(file, i5);
	file.close();
	file.open("key15.txt");
	fun_in(file, i15);
	file.close();
	i2.close();
	i3.close();
	i4.close();
	i5.close();
    i15.close();

	
	




	return 0;
}

