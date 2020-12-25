#ifndef HEADER_H
#define HEADER_H

#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <Windows.h> //for 1251
#include <iomanip> // for setpresicion
#include <algorithm> // for remove replace
#include <cmath>
#include <utility> //pair


#define BASE_DIR "D:\\cryptolab3\\"

using namespace std;



map<string, int> AlphNum =
{
   {"а", 0},	{"б", 1},	{"в", 2},	{"г", 3},
   {"д", 4},	{"е", 5},	{"ж", 6},	{"з", 7},
   {"и", 8},	{"й", 9},	{"к", 10},	{"л", 11},
   {"м", 12},	{"н", 13},	{"о", 14},	{"п", 15},
   {"р", 16},	{"с", 17},	{"т", 18},	{"у", 19},
   {"ф", 20},	{"х", 21},	{"ц", 22},	{"ч", 23},
   {"ш", 24},	{"щ", 25},	{"ь", 26},	{"ы", 27},
   {"э", 28},	{"ю", 29},	{"я", 30},

};

map<int, string> NumAlph =
{
   {0,"а"},		{1,"б"},	{2,"в"},	{3,"г"},
   {4,"д"},		{5,"е"},	{6,"ж"},	{7,"з"},
   {8,"и"},		{9,"й"},	{10,"к"},	{11,"л"},
   {12,"м"},	{13,"н"},	{14,"о"},	{15,"п"},
   {16,"р"},	{17,"с"},	{18,"т"},	{19,"у"},
   {20,"ф"},	{21,"х"},	{22,"ц"},	{23,"ч"},
   {24,"ш"},	{25,"щ"},	{26,"ь"},	{27,"ы"},
   {28,"э"},	{29,"ю"},	{30,"я"},

};

vector<string> top5bigr = {
	{"ст"}, {"но"}, {"то"}, {"на"}, {"ен"}

};

int alpha_size = AlphNum.size();

ifstream fin;
ofstream fout;

#endif