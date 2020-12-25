#pragma once
#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

vector<int> MostPopulatBigram = { 545, 417, 572, 403, 168 };
int MODULE = 31;

int func(char ch);
char refunc(int n);
vector<int> Engramm(vector<int> fulltext);
vector<int> Degramm(vector<int> text);
vector<int> Monogram(vector<int> text);
vector<int> TopMonogram(vector<int> text);
vector<int> AntiTopMonogram(vector<int> text);
vector<int> bigram_ncross(vector<char> buff);
int Gcd(int a, int b);
int Gcd(int a, int b, int & x, int & y);
int BackElement(int a, int m);
vector<int> line(int a, int b, int m);
vector<int> TryKey(vector<int> ciphertext, int a, int b);
vector<pair<int, int>> GetKey(int x1, int x2, int y1, int y2);
vector<pair<int, int>> ActualKey(vector<int> ciphertext, vector<int> Y);
bool Filter(vector<int> btext);
void Decode(vector<int> ciphertext);