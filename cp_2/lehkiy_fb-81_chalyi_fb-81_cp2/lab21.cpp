#include <iostream>
#include <fstream>
#include <time.h>
using namespace std;

//функція в якій відбувається шифрування тексту за доп. шифру Віженера
void viznr(const char *text, const int r, const int n)
{
	srand(time(0)); // Потрібно для більш точного виводу
	int x=0;
	float indx=0;
	float frequency[32]={0};
	int *key=new int[100];
	for (int i=0; i<n; ++i)
	{
		key[i]=rand()%32; // Вибирає випадкову букву
		cout<<(char)(key[i]-32);
	}
	cout<<endl;
	for (int i=0; i<r; ++i)
		if (text[i]!=' ')
		{
			cout<<(char)(((text[x]+32)+key[x%n])%32-32);
			frequency[((text[x]+32)+key[x%n])%32]+=1;
			++x;
		}
	cout<<endl;
	for (int i=0; i<32; ++i)
	{
		indx +=(frequency[i]/x)*(frequency[i]/(x)); // В нас текст осмислений, тому викор іншу формулу ніж в методичці 
	}
	cout<<"index="<<indx<<endl; // Вивід індексу відповідності 
	delete []key;
}
int main()
{
	FILE* in = fopen("input.txt", "r"); // Відкриваємо файл з потрібним для шифрування текстом
	int r = 0;
	char c;
	char* text = new char[50000000];
	while (fscanf(in, "%c", &c) != EOF) // Зчитуємо файл до кінця. Працюємо с російським алфавітом 
	{
		if ('а' <= c && c <= 'я')
			text[r++] = c;
		if ('А' <= c && c <= 'Я')
			text[r++] = c + 32;
		if ((c == ' ' || c == '\t' || c == '\n') && text[r - 1] != ' ')
		{
			text[r++] = ' ';
		}
	}

	fclose(in);
	//Створення або видозмінення файлів з використанням певної довжини ключа
	freopen("r2.txt", "w", stdout);
	viznr(text, r, 2);
	freopen("r3.txt", "w", stdout);
	viznr(text, r, 3);
	freopen("r4.txt", "w", stdout);
	viznr(text, r, 4);
	freopen("r5.txt", "w", stdout);
	viznr(text, r, 5);
	freopen("r10.txt", "w", stdout);
	viznr(text, r, 10);
	freopen("r11.txt", "w", stdout);
	viznr(text, r, 11);
	freopen("r12.txt", "w", stdout);
	viznr(text, r, 12);
	freopen("r13.txt", "w", stdout);
	viznr(text, r, 13);
	freopen("r14.txt", "w", stdout);
	viznr(text, r, 14);
	freopen("r15.txt", "w", stdout);
	viznr(text, r, 15);
	freopen("r16.txt", "w", stdout);
	viznr(text, r, 16);
	freopen("r17.txt", "w", stdout);
	viznr(text, r, 17);
	freopen("r18.txt", "w", stdout);
	viznr(text, r, 18);
	freopen("r19.txt", "w", stdout);
	viznr(text, r, 19);
	freopen("r20.txt", "w", stdout);
	viznr(text, r, 20);
	return 0;
}
