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
#include <tuple>

#include <boost/random.hpp> //rand
#include <boost/random/independent_bits.hpp>
#include <boost/multiprecision/cpp_int.hpp> // cpp_int

using namespace std;
using namespace boost::multiprecision;
using namespace boost::random;

ifstream fin;
ofstream fout;

vector<int> dividers = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59 };


class Pers
{
public:

	Pers(); //constructor
	Pers(size_t size);
	Pers(pair<cpp_int, cpp_int> publ); //constructor
	Pers(/*cpp_int e, cpp_int p, cpp_int q, cpp_int d, cpp_int n*/string path);

	pair<cpp_int, cpp_int> getpublickey();
	//tuple<cpp_int, cpp_int, cpp_int> getprivatekey();
	void printpublickey();

	void printprivatekey();

	pair< cpp_int, cpp_int> sign_message(cpp_int& M/*, tuple<cpp_int, cpp_int, cpp_int>& privatekey*/);
	//bool check_signature(pair< cpp_int, cpp_int> sign_mes, pair< cpp_int, cpp_int> publickey);
	bool check_signature(/*pair< cpp_int, cpp_int> sign_mes*/cpp_int M, cpp_int S, pair< cpp_int, cpp_int> publickey);
	
	cpp_int encrypt(cpp_int M, pair<cpp_int, cpp_int>& publkey);
	cpp_int decrypt(cpp_int C/*, tuple<cpp_int, cpp_int, cpp_int>& privatekey*/);

	void setkey(size_t size);

	pair< cpp_int, cpp_int> RSA_sender(Pers &B, cpp_int k);
	//cpp_int RSA_reciever(Pers &A, pair<cpp_int, cpp_int> mes);
	cpp_int RSA_reciever(Pers& A, /*pair<cpp_int, cpp_int> mes*/cpp_int& M, cpp_int& S);

	Pers cr_s(string path);

private:


	pair<cpp_int, cpp_int> publickey; //pbk value
	tuple<cpp_int, cpp_int, cpp_int> privatekey; //pvk value


	pair<cpp_int, cpp_int> gen_publickey(cpp_int& p, cpp_int& q, cpp_int& phi_n, size_t &size); // generate pbk
	pair< tuple<cpp_int, cpp_int, cpp_int>, pair<cpp_int, cpp_int>> gen_keyset(size_t &size); // generate pbk and prk



};


#endif