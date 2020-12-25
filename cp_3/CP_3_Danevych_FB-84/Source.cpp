#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <math.h>

using namespace std;

map<int, char> ABC = { {0, 'а'}, {1, 'б'}, {2, 'в'}, {3, 'г'},{4, 'д'}, {5, 'е'}, {6, 'ж'}, {7, 'з'}, {8, 'и'}, {9, 'й'}, {10, 'к'},
					   {11, 'л'},{12, 'м'}, {13, 'н'}, {14, 'о'}, {15, 'п'}, {16, 'р'}, {17, 'с'}, {18, 'т'}, {19, 'у'}, {20, 'ф'},
					   {21, 'х'}, {22, 'ц'}, {23, 'ч'}, {24, 'ш'}, {25, 'щ'}, {26, 'ь'}, {27, 'ы'}, {28, 'э'}, {29, 'ю'}, {30, 'я'} };

int number_key = 0;

int gcd(int a, int b, int& size_mas)
{
	if (a != 0 && b != 0)
	{
		while (a != b)
		{
			if (a > b)
			{
				int tmp = a;
				a = b;
				b = tmp;
				size_mas++;
			}
			b = b - a;
		}
		return a;
	}
	return b;
}

void encoder(string file, int a, int b)
{
	ifstream in_encoder(file);
	ofstream out_encoder("encoder_text.txt");
	int X, x1, x2, Y, y1, y2, m = 31, m_2, size_mas = 2;
	char symbol1, symbol2;
	m_2 = m * m;

	if (gcd(a, m, size_mas) == 1)
	{
		while (!in_encoder.eof())
		{
			while (!in_encoder.eof())
			{
				symbol1 = in_encoder.get();

				if (symbol1 != '\n')
				{
					break;
				}
			}
			while (!in_encoder.eof())
			{
				symbol2 = in_encoder.get();

				if (symbol2 != '\n')
				{
					break;
				}
			}

			for (auto& abc : ABC)
			{
				if (symbol1 == abc.second)
					x1 = abc.first;
				if (symbol2 == abc.second)
					x2 = abc.first;
			}

			X = x1 * m + x2;
			Y = (X * a + b) % m_2;
			y1 = Y / m;
			y2 = Y % m;

			for (auto& abc : ABC)
			{
				if (y1 == abc.first)
					symbol1 = abc.second;
				if (y2 == abc.first)
					symbol2 = abc.second;
			}

			out_encoder << symbol1 << symbol2;
		}
	}
	else
		std::cout << "Числo а ключа не є взаємно просте з довжиною алфавіта, введіть інший ключ)" << endl;

	in_encoder.seekg(0, std::ios::beg);
	in_encoder.close();
	out_encoder.seekp(0, std::ios::beg);
	out_encoder.close();
}

int inverted_element(int a, int m, int size_mas)
{
	int* mas = new int[size_mas];
	
	int c = 0, i = 2,n=m;
	if (a != 0)
	{
		mas[0] = 0;
		mas[1] = 1;
		while (a != m)
		{
			if (a > m)
			{
				int tmp = a;
				a = m;
				m = tmp;
				mas[i] = c * (-1);
				i++;
				c = 0;
			}
			m = m - a;
			c++;
		}
		for (int j = 2; j < size_mas; j++)
		{
			mas[j] = mas[j] * mas[j - 1] + mas[j - 2];
		}

		a = mas[size_mas - 1];
		while (a > n) a = a - n;
		while (a < 0) a = a + n;
		size_mas = 2;
		delete[] mas;
		return a;
	}
	else
		size_mas = 2;
		delete[]mas;
		return 0;
}

bool decoder(string file, int a, int b)
{
	ifstream in_decoder("08.txt");
	ofstream out_decoder("decoder_text.txt");
	int X, x1, x2, Y, y1, y2, m = 31, m_2, a_1, size_mas = 2;
	char symbol1, symbol2;
	m_2 = m * m;

	if (gcd(a, m_2, size_mas) == 1)
	{
		while (!in_decoder.eof())
		{
			while (!in_decoder.eof())
			{
				symbol1 = in_decoder.get();

				if (symbol1 != '\n')
				{
					break;
				}
			}
			while (!in_decoder.eof())
			{
				symbol2 = in_decoder.get();

				if (symbol2 != '\n')
				{
					break;
				}
			}

			for (auto& abc : ABC)
			{
				if (symbol1 == abc.second)
					y1 = abc.first;
				if (symbol2 == abc.second)
					y2 = abc.first;
			}

			Y = y1 * m + y2;
			a_1 = inverted_element(a, m_2, size_mas);
			X = ((Y - b) * a_1) % m_2;
			while (X > m_2) X = X - m_2;
			while (X < 0) X = X + m_2;
			x1 = X / m;
			x2 = X % m;

			for (auto& abc : ABC)
			{
				if (x1 == abc.first)
					symbol1 = abc.second;
				if (x2 == abc.first)
					symbol2 = abc.second;
			}

			out_decoder << symbol1 << symbol2;
		}
		in_decoder.seekg(0, std::ios::beg);
		in_decoder.close();

		out_decoder.close();
		return true;
	}
	else
	{
		std::cout << "Числo а ключа не є взаємно просте з довжиною алфавіта, спробуйте інший ключ)" << endl;
		return false;
	}


}

void pop_bigrams(string file, int size)
{
	ifstream in_pop(file);
	ofstream out_pop("pop_big.txt");
	char symbol1, symbol2;
	int number_big = 0;
	float number = 0;

	map<string, float> container_bigrams;

	while (!in_pop.eof())
	{
		while (!in_pop.eof())
		{
			symbol1 = in_pop.get();

			if (symbol1 != '\n')
			{
				break;
			}
		}
		while (!in_pop.eof())
		{
			symbol2 = in_pop.get();

			if (symbol2 != '\n')
			{
				break;
			}
		}
		string bigram;
		bigram += symbol1;
		bigram += symbol2;

		container_bigrams[bigram] += 1;
		number_big++;
	}

	for (auto& bi : container_bigrams)
		bi.second = bi.second / number_big;
	for (int i = 0; i < size; i++)
	{
		for (auto& bi : container_bigrams)
			if (bi.second > number) number = bi.second;
		for (auto& bi : container_bigrams)
		{
			if (bi.second == number)
			{
				out_pop << bi.first;
				bi.second = 0;
				number = 0;
				break;
			}
		}
	}

	in_pop.seekg(0, std::ios::beg);
	in_pop.close();
	out_pop.seekp(0, std::ios::beg);
	out_pop.close();
}

void pop_monograms(string file, int size)
{
	ifstream in_mono(file);
	ofstream out_mono("pop_mono.txt");
	char symbol;
	int number_mono = 0;
	float number = 1;

	map<char, float> container_monograms_for_pop;
	map<char, float> container_monograms_for_not_pop;

	while (!in_mono.eof())
	{
		while (!in_mono.eof())
		{
			symbol = in_mono.get();

			if (symbol != '\n')
			{
				break;
			}
		}
		container_monograms_for_pop[symbol] += 1;
		container_monograms_for_not_pop[symbol] += 1;
		number_mono++;
	}

	for (auto& mono : container_monograms_for_not_pop)
		mono.second = mono.second / number_mono;
	for (int i = 0; i < size; i++)
	{
		for (auto& mono : container_monograms_for_not_pop)
			if (mono.second < number) number = mono.second;
		for (auto& mono : container_monograms_for_not_pop)
		{
			if (mono.second == number)
			{
				out_mono <<  mono.first;
				mono.second = 1;
				number = 1;
				break;
			}
		}
	}

	number = 0;
	for (auto& mono : container_monograms_for_pop)
		mono.second = mono.second / number_mono;
	for (int i = 0; i < size;i++)
	{
		for (auto& mono : container_monograms_for_pop)
			if (mono.second > number) number = mono.second;
		for (auto& mono : container_monograms_for_pop)
		{
			if (mono.second == number)
			{
				out_mono << mono.first;
				mono.second = 0;
				number = 0;
				break;
			}
		}
	}

	out_mono.close();
	in_mono.seekg(0, std::ios::beg);
	in_mono.close();
}

bool text_check(string file)
{
	ifstream in_check("pop_mono.txt");
	ifstream in("pop_big.txt");
	int size = 4;
	bool rez = false;
	int a = 0, i = 0;
	char symbol, symbol1, symbol2;
	char pop_leter[5] = { 'о','е','а','и','н' };
	char pop_leter_in_text[4];
	char not_pop_leter[5] = { 'ф','э','щ','ц','ю' };
	char not_pop_leter_in_text[4];
	string pop_big[10] = { "ст","но","ен","то","на","ов","ни","ра","во","ко" };
	string pop_big_in_text[1];


	pop_monograms("decoder_text.txt", size);

	while (!in_check.eof())
	{
		while (!in_check.eof())
		{
			symbol = in_check.get();

			if (symbol != '\n')
			{
				break;
			}
		}
		if (a < size)
		not_pop_leter_in_text[a] = symbol;
		a++;

		if (a > size)
		{
			pop_leter_in_text[i] = symbol;
			i++;
			if (i >= size)break;
		}
	}
	size = 1;
	a = 0;
	in_check.seekg(0, std::ios::beg);
	in_check.close();

	pop_bigrams(file, size);

	while (!in.eof())
	{
		while (!in.eof())
		{
			symbol1 = in.get();

			if (symbol1 != '\n')
			{
				break;
			}
		}
		while (!in.eof())
		{
			symbol2 = in.get();

			if (symbol2 != '\n')
			{
				break;
			}
		}
		string bigram;
		bigram += symbol1;
		bigram += symbol2;
		pop_big_in_text[a] = bigram;
		a++;
		if (a >= 1)break;
	}
	in.close();

	for (int i = 0; i < 4; i++)
	{
		rez = false;
		for (int j = 0; j < 5; j++)
		{
			if (pop_leter_in_text[i] == pop_leter[j]) rez = true;
		}
		if (rez == false)
		{
			std::cout << "Не пройшло перевірку на найчастіші монограми" << endl;
			std::cout << "Найпопулярніші монограми:";
			for (int j = 0; j < 4; j++)
				std::cout << " " << pop_leter_in_text[j];
			std::cout << endl;
			in_check.clear();
			in_check.close();

			return rez;
		}
	}

	rez = false;
	for (int i = 0; i < 4; i++)
	{
		rez = false;
		for (int j = 0; j < 5; j++)
		{
			if (not_pop_leter_in_text[i] == not_pop_leter[j]) rez = true;
		}
		if (rez == false)
		{
			std::cout << "Не пройшло перевірку на найрідші монограми" << endl;
			std::cout << "Найрідші моногрaми:";
			for (int j = 0; j < 4; j++)
				std::cout << " " << not_pop_leter_in_text[j];
			std::cout << endl;
			in_check.clear();
			in_check.close();

			return rez;
		}
	}

	rez = false;
	for (int i = 0; i < 1; i++)
	{
		rez = false;
		for (int j = 0; j < 10; j++)
		{
			if (pop_big_in_text[i] == pop_big[j]) rez = true;
		}
		if (rez == false)
		{
			std::cout << "Не пройшло перевірку на найчастіші біграми" << endl;
			in_check.clear();
			in_check.close();

			return rez;
		}
	}
	std::cout << "Пройшло перевірку, наш ключ" << endl;
	std::cout << "Найпопулярніші монограми:";
	for (int j = 0; j < 4; j++)
		std::cout << " " << pop_leter_in_text[j];
	std::cout << endl;
	std::cout << "Найрідші моногрaми:";
	for (int j = 0; j < 4; j++)
		std::cout << " " << not_pop_leter_in_text[j];
	std::cout << endl;
	std::cout << "Найчастіша монограма:";
	for (int j = 0; j < 1; j++)
		std::cout << " " << pop_big_in_text[j];
	std::cout << endl;
		in_check.close();
		a = 0; i = 0;
		return rez;

}

int XY(string big, int m)
{
	char mus[2];
	int i = 0, x, y, rez;
	for (auto& b : big)
	{
		mus[i] = b;
		i++;
	}
	for (auto& abc : ABC)
	{
		if (mus[0] == abc.second) x = abc.first;
		if (mus[1] == abc.second) y = abc.first;
	}
	rez = x * m + y;
	return rez;
}
bool evk(int X, int Y, int Y1, int X1, int m, int size_mas, int d, string file )
{
	int a, b, x1, y1, n1, i;
	bool rez=false; 
	size_mas = 2;
	i = d;

		if (Y % d == 0)
		{
			n1 = m / d;
			x1 = X / d;
			y1 = Y / d;
			gcd(x1, n1, size_mas);
			x1 = inverted_element(x1, n1, size_mas);
			a = (y1 * x1) % n1;
			if (a < 0)a = a + m;

				for (i ; i > 0; i--)
				{
					a = a + ((d - i) * n1);
					b = (Y1 - a * X1) % m;
					if (b < 0)b = b + m;
					number_key++;
					std::cout << "Ключ " << number_key << ":  " << a << " " << b<<endl;

						rez = decoder(file, a, b);
						if (rez == true)
						{
							rez = text_check("decoder_text.txt");
							if (rez == true) return rez;
						}
					
				}
		}
		rez = false;
	return rez;
}

bool key(string rus_big1, string rus_big2, string big1, string big2, string file)
{
	int X1, X2, Y1, Y2, X, Y, m_2, m = 31, a, b, size_mas = 2, d;
	bool rez=true;

	m_2 = m * m;
	X1 = XY(rus_big1, m);
	X2 = XY(rus_big2, m);
	Y1 = XY(big1, m);
	Y2 = XY(big2, m);
	X = X1 - X2;
	Y = Y1 - Y2;
	while (X < 0) X = X + m_2;
	while (Y < 0) Y = Y + m_2;
	d = gcd(X, m_2, size_mas);

		if (d == 1)
		{
			X = inverted_element(X, m_2, size_mas);
			a = (Y * X) % m_2;
			b = (Y1 - a * X1) % m_2;
			if (a < 0)a = a + m_2;
			if (b < 0)b = b + m_2;
			number_key++;
			std::cout << "Ключ " << number_key << ":  " << a << " " << b << endl;

			rez = decoder(file, a, b);
			if (rez == true)
			{
				rez = text_check("decoder_text.txt");
				return rez;
			}
			else
				return rez;
		}

		else rez = evk(X, Y, Y1, X1, m_2, size_mas, d, file);
		return rez;

	
}

int main()
{
	setlocale(LC_CTYPE, "rus");
	int a=0, b, size = 5;
	string pop_in_rus[5] = { "ст","но","то","на","ен" };

	pop_bigrams("08.txt", size);
	ifstream in("pop_big.txt");

	char symbol1, symbol2;
	string pop[5];
	int i = 0;
	while (!in.eof())
	{

			while (!in.eof())
			{
				symbol1 = in.get();

				if (symbol1 != '\n')
				{
					break;
				}
			}
			while (!in.eof())
			{
				symbol2 = in.get();

				if (symbol2 != '\n')
				{
					break;
				}
			}
			string bigram;
			bigram += symbol1;
			bigram += symbol2;
			pop[i] = bigram;
			i++;
			if (i >= size)break;
	}
	in.close();

	bool true_kye;
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if (i != j)
			{
				for (int n = 0; n < 5; n++)
				{
					for (int t = 0; t < 5; t++)
					{
						if (n != t)
						{
							true_kye = key(pop_in_rus[i], pop_in_rus[j], pop[n], pop[t], "08.txt");
							if (true_kye == true) break;
						}
					}
					if (true_kye == true) break;
				}
				if (true_kye == true) break;
			}
		}
		if (true_kye == true) break;
	}
	//inverted_element(128, 961, 6);
	
	return 0;
}