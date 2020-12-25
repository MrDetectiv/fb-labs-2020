// decipher.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include<fstream>
#include<string>
#include<cmath>
#include <sstream>
#include <windows.h>
#include <cstdio>

using namespace std;
const int n = 255;
int symbol_count;
char *symbol_array = new char[symbol_count];


void fun_clear(ifstream &myfile)
{
	ofstream out;
	out.open("temp.txt");
	stringstream string_stream;
	string_stream << myfile.rdbuf();
	string text_string = string_stream.str();
	myfile.close();
	int i = 0;
	while (i != text_string.length())
	{
		if (text_string[i] != ' ' || int(text_string[i]) != 10)
		{
			out << text_string[i];
		}
		i++;
	}
	out.close();
}

void fun_in(ifstream &myfile)
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
		for (int j = 0; j < symbolsLenth; j++)
		{
			if (symbol_array[i] == symbols[j])
			{
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


	int count = symbol_count;

	float  I, sum = 0;

	for (int i = 0; i < symbolsLenth; i++)
	{

		if (symbols[i] != ' ')
		{
			sum = sum + chance[i] * (chance[i] - 1) / (count*(count - 1));
		}
	}

	I = sum;
	//cout << "Индекс = " << I << '\n' << '\n';

}



void freq(string str)
{
	int symbol_count;
	symbol_count = str.length();
	symbol_array = new char[symbol_count];
	str.copy(symbol_array, symbol_count);


	char symbols[n];     // масив символів без повторень
	double chance[n];   // частота символів
	int symbolsLenth = 0;



	for (int i = 0; i < symbol_count; i++)
	{
		int flg = 0;
		for (int j = 0; j < symbolsLenth; j++)
		{
			if (symbol_array[i] == symbols[j])
			{
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

	// сортування
	int flg = 1;
	while (flg)
	{
		flg = 0;
		for (int i = 0; i < symbolsLenth - 1; i++)
		{
			if (chance[i] < chance[i + 1]) {
				double tmp = chance[i];
				chance[i] = chance[i + 1];
				chance[i + 1] = tmp;
				char ch = symbols[i];
				symbols[i] = symbols[i + 1];
				symbols[i + 1] = ch;
				flg = 1;
			}
		}
	}

	//cout << "Частота max freq символов:\n";
	//cout << symbols[0] << '\t' << chance[0] << endl;
	//cout << symbols[0] << endl;
	
	int temp_key, temp_key1,temp_key2;


	temp_key = (int(symbols[0]) - int('о'))%31;
	temp_key1 = (int(symbols[0]) - int('е')) % 31;
	temp_key2 = (int(symbols[0]) - int('р')) % 31;
	/*
	if (temp_key >= 0)
	{
		temp_key = temp_key - 32;
		cout << char(temp_key);
	}
	else
	{
		cout << char(temp_key);
	}
	
	//cout << endl;
	
	if (temp_key1 >= 0)
	{
		temp_key1 = temp_key1 - 32;
		cout << char(temp_key1);
	}
	else
	{
		cout << char(temp_key1);
	}
	
	
	cout << endl;
	*/
	if (temp_key2 >= 0)
	{
		temp_key2 = temp_key2 - 32;
		cout << char(temp_key2);
	}
	else
	{
		cout << char(temp_key2);
	}
	//cout << endl;

	
}

void text_cut(ifstream &myfile, int c, ofstream &out)
{
	stringstream string_stream;
	string_stream << myfile.rdbuf();
	string text_string = string_stream.str();
	myfile.close();
	int i = 0;

	while (i < text_string.length())
	{
		out << text_string[i];
		i = i + c;
	}
}

void fun_blocks(ifstream &myfile)
{
	stringstream string_stream;
	string_stream << myfile.rdbuf();
	string text_string = string_stream.str();
	myfile.close();
	int i;

	for (int j = 0; j < 13; j++)
	{
		i = j;
		string str;
		while (i < text_string.length())
		{
			str += text_string[i];
			i = i + 13;
		}

		//cout << j << endl;
		freq(str);

	}

}


void dec(ifstream &myfile, string key, ofstream &out)
{

	stringstream string_stream;
	string_stream << myfile.rdbuf();
	string text_string = string_stream.str();
	myfile.close();
	int j = 0, z;
	cout << key.length();
	for (int i = 0; i < text_string.length(); i++)
	{

			if (j < key.length())
			{
				z = (int(text_string[i]) - int(key[j])) % 32;
				if (z >= 0)
				{
					z =z -32;
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
				z = (int(text_string[i]) - int(key[j])) % 32;
				if (z >= 0)
				{
					z =z -32;
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


int main()
{

	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "rus");


	ifstream file;
	file.open("lab2.txt");
	for (int i = 2; i < 35; i++)
	{
		file.open("temp.txt");
		ofstream  out;
		out.open("1.txt");
		text_cut(file, i, out);
		//cout << i << " ";
		out.close();

		ifstream out1;
		out1.open("1.txt");

		fun_in(out1);
		out1.close();
		cout << endl;

	}
	file.open("temp.txt");
	fun_blocks(file);
	file.close();
	string key = "громыковедьма";
	ofstream out;
	file.open("temp.txt");
	out.open("dec.txt");
	dec(file, key, out);
	///cout << "HELO";

	return 0;
}