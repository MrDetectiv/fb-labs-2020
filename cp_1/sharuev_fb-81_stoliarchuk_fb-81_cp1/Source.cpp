#include <iostream>
#include <string>
#include <fstream>
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
		if (text[i] >= 'А' && text[i] <= 'я' || text[i] == 'ё' || text[i] == ' ')
		{
			if (text[i] >= 'А' && text[i] <= 'Я')
			{
				text[i] += 32;
			}
			if (text[i] == 'ъ')
			{
				text[i] = 'ь';
			}
			if (text[i] == 'ё')
			{
				text[i] = 'е';
			}
			if (text[i] == ' ' && text[i + 1] == ' ')
			{
				continue;
			}
			newText += text[i];
		}
	}
	return newText;
}

string whitepaperWithoutSpaces(string text)
{
	string newText;
	for (int i = 0; i < text.length(); i++)
	{
		if (text[i] >= 'а' && text[i] <= 'я' || text[i] == 'ё')
		{
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

	cout << endl << endl << "Number of each letter:" << endl;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		cout << " " << itr->first << "| " << itr->second << endl;
	}
	cout << endl;
}

void NumberOfEachСoupleLetter(string& text, map <string, double>& table)
{
	string cell;

	for (int i = 0; i < text.length() && i + 2 != text.length() - 1; i++)
	{
		cell = text.substr(i, 2);
		table[cell] ++;
		cell.clear();
	}

	cout << endl << endl << "Number of each couple letter:" << endl;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		cout << " " << itr->first << "| " << itr->second << endl;
	}
	cout << endl;
}

void NumberOfEachСoupleLetterWin(string& text, map <string, double>& table)
{
	string cell;
	for (int i = 0; i < text.length() && i + 2 != text.length() - 1; i += 2)
	{
		cell = text.substr(i, 2);
		table[cell] ++;
		cell.clear();
	}

	cout << endl << endl << "Number of each couple letter:" << endl;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		cout << " " << itr->first << "| " << itr->second << endl;
	}
	cout << endl;
}

map<string, double> Frequency(int length, map<string, double>& table)
{
	map<string, double> frequency;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		frequency.insert({ itr->first, (itr->second / length) });
	}

	cout << endl << endl << "Frequency:" << endl;

	for (auto itr = frequency.begin(); itr != frequency.end(); ++itr)
	{
		cout << " " << itr->first << "" << "| ";
		cout << fixed;
		cout.precision(5);
		cout << itr->second << endl;
	}
	cout << endl;
	return frequency;
}


double Enthropy_H1(map<string, double>& table)
{
	double H = 0;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		H -= itr->second * log2(itr->second);
	}

	return H;
}

double Enthropy_H2_in(map<string, double>& table)
{
	double H = 0;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		H -= itr->second * log2(itr->second) / 2;
	}

	return H;
}

double Enthropy_H2_win(map<string, double>& table)
{
	double H = 0;

	for (auto itr = table.begin(); itr != table.end(); ++itr)
	{
		H -= itr->second * log2(itr->second) / 2;
	}

	return H;
}


int main()
{
	setlocale(LC_ALL, "rus");

	string text, text_ws;
	text = textFileToString(text);
	cout << text << endl;
	cout << "==========Whitelist with spaces==========" << endl;
	text = whitepaper(text);
	cout << text << endl;

	cout << "==========Whitelist without spaces==========" << endl;
	text_ws = whitepaperWithoutSpaces(text);
	cout << text_ws << endl;


	map<string, double> letters;
	map<string, double> letters_ws;

	map<string, double> bigram_in;
	map<string, double> bigram_in_ws;

	map<string, double> bigram_win;
	map<string, double> bigram_win_ws;

	// количество монограм
	NumberOfEachLetter(text, letters);
	NumberOfEachLetter(text_ws, letters_ws);
	// количество биграмм с пересечениями
	NumberOfEachСoupleLetter(text, bigram_in);
	NumberOfEachСoupleLetter(text_ws, bigram_in_ws);
	// количество биграмм без пересечений
	NumberOfEachСoupleLetterWin(text, bigram_win);
	NumberOfEachСoupleLetterWin(text_ws, bigram_win_ws);

	double H1, H1_ws, H2_in, H2_in_ws, H2_win, H2_win_ws;


	// частота монограмы с пробелами
	map<string, double> Let_Freq = Frequency(text.length(), letters);

	// частота монограмы без пробелов
	map<string, double> Let_Freq_WS = Frequency(text_ws.length(), letters_ws);

	// частота биграм в тексте с пробелами и с пересечениями
	map<string, double> Bigram_Freq_In = Frequency(text.length() - 1, bigram_in);

	// частота биграм в тексте без пробелов и с пересечениями
	map<string, double> Bigram_Freq_In_WS = Frequency(text_ws.length() - 1, bigram_in_ws);

	// частота биграм в тексте с пробелами и без пересечений
	map<string, double> Bigram_Freq_WIn = Frequency(text.length() / 2, bigram_win);

	// частота биграм в тексте без пробелов и без пересечений
	map<string, double> Bigram_Freq_WIn_WS = Frequency(text_ws.length() / 2, bigram_win_ws);




	// энтропия монограмы с пробелами
	H1 = Enthropy_H1(Let_Freq);
	cout << endl << "Enthropy H1: " << H1 << endl;

	// энтропия монограмы без пробелов
	H1_ws = Enthropy_H1(Let_Freq_WS);
	cout << endl << "Enthropy H1 without spaces: " << H1_ws << endl;

	// энтропия биграмы с пробелами и с пересечениями
	H2_in = Enthropy_H2_in(Bigram_Freq_In);
	cout << endl << "Enthropy H2_in: " << H2_in << endl;

	// энтропия биграмы без пробелов и с пересечениями
	H2_in_ws = Enthropy_H2_in(Bigram_Freq_In_WS);
	cout << endl << "Enthropy H2_in_ws: " << H2_in_ws << endl;

	// энтропия биграмы с пробелами и без пересечений
	H2_win = Enthropy_H2_win(Bigram_Freq_WIn);
	cout << endl << "Enthropy H2_win: " << H2_win << endl;

	// энтропия биграмы без пробелов и без пересечений
	H2_win_ws = Enthropy_H2_win(Bigram_Freq_WIn_WS);
	cout << endl << "Enthropy H2_win_ws: " << H2_win_ws << endl;

	system("pause");
	return 0;
}