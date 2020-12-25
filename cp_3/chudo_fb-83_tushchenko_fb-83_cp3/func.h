#include "sidefunc.h"


int bigram_to_int(string& bigr)
{
	string a, b;
	a = bigr.at(0);
	b = bigr.at(1);

	int an, bn;

	an = AlphNum[a];
	bn = AlphNum[b];

	return an * alpha_size + bn;
}

string int_to_bigram(int& bi)
{
	int a, b;
	a = bi / alpha_size;
	b = bi % alpha_size;

	string ab;
	ab += NumAlph[a];
	ab += NumAlph[b];

	return ab;
}

//linear
 //a* x = b (mod m)
vector<int> linear(int a, int b, int m)
{	
	vector<int> res;
//	int a_inv = inverse_mod(a, m);
	
	
	int d = gcd(a, m);

	if (d == 1)
	{
		int x = mod(inverse_mod(a,m) * b, m);
		res.push_back(x);
	}
	else 
		if (d > 1)
		{
			if (b % d != 0)
			{
				cout << "No Solutions for equation:  " << a << " * x = " << b << " (mod " << m << ")" << endl;
				
			}
			else
			{
				int a1 = a / d;
				int b1 = b / d;
				int m1 = m / d;
				int x = mod(inverse_mod(a1, m1) * b1, m1);
				res.push_back(x);
				for (int i = 0; i < d ; i++)
				{
					x += m1;
					if (x < m)
					{
						res.push_back(x);
					}
				}
			}
		}

	return res;
}


//encode
vector<int> encode(string& text, pair<int, int> &key)
{
	int a = key.first;
	int b = key.second;
	string let1, let2;
		int x,y, y1, y2;
		vector<int> encnum;
	for (int i = 0; i+1 < text.length(); i+=2)
	{
		//get 2 letters
		let1 = text.substr(i, 1); // x1
		let2 = text.substr(i + 1, 1); //x2
		// X = x1 * m + x2
		x = AlphNum[let1] * alpha_size + AlphNum[let2];
		// Y = a*X + b mod m^2
		y = mod(x * a + b, pow(alpha_size, 2));
		// Y = y1*m + y2
		y1 = y / alpha_size;
		y2 = y % alpha_size;
		encnum.push_back(y1);
		encnum.push_back(y2);
		let1.clear(); let2.clear();
		y1 = 0; y2 = 0;
	}

	if (text.length() % 2 != 0)
	{
		let1 = text.substr(text.length()-1, 1);
		x = AlphNum[let1] * alpha_size;
		y = mod(x * a + b, pow(alpha_size, 2));
		y1 = y / alpha_size;
		y2 = y % alpha_size;
		encnum.push_back(y1);
		encnum.push_back(y2);
	}



	return encnum;
}

//string encode(string& text, pair<int, int> &key)
//{
//	vector<int> encrnum = encode(text, key);
//	return num_to_text(encrnum);
//}


//decode

vector<int> decode(vector<int>& textnum, pair<int, int>& key)
{
	/*
	linear() returns vector<int>
	*/
	int a = key.first;
	int b = key.second;
	string let1, let2;
	int x, y, x1, x2;
	vector<int> decnum;
	vector<int> cur;
	vector<int> X;
	int a_inv = inverse_mod(a, pow(alpha_size,2));
	int d = gcd(a, pow(alpha_size, 2));

	if (d == 1)
	{

		for (int i = 0; i + 1 < textnum.size(); i += 2)
		{
			// Y = y1 * m + y2
			// textnum.at(i) = y1
			// textnum.at(i+1) = y2
			y = textnum.at(i) * alpha_size + textnum.at(i + 1);
			// X = a^-1 * (Y - b) mod m
			////x = mod(a_inv * (y - b), pow(alpha_size,2));


			X = linear(a, (y - b), pow(alpha_size, 2));		//linear returns vector<int>

			
				x = X.at(0);

				// X = x1 * m + x2
				x1 = x / alpha_size;
				x2 = x % alpha_size;

				decnum.push_back(x1);
				decnum.push_back(x2);

			}
		

		if (textnum.size() % 2 != 0)
		{
			y = textnum.back() * alpha_size;
			x = mod(a_inv * (y - b), alpha_size);
			x1 = x / alpha_size;
			x1 = x % alpha_size;
			decnum.push_back(x1);
			decnum.push_back(x2);
		}
	}

	if (d > 1)
	{	}

		

	return decnum;
}


//vector<int> decode(string& text, pair<int, int> &key)
//{
//	vector<int> textnum = text_to_num(text);
//	return decode(textnum, key);
//}
//
//string decodestr(vector<int>& textnum, pair<int, int>& key)
//{
//	vector<int> decnum = decode(textnum, key);
//	return num_to_text(decnum);
//}
//
//string decodestr(string& text, pair<int, int>& key)
//{
//	vector<int> decnum = decode(text, key);
//	return num_to_text(decnum);
//}


//test lang
bool test_forbidden_bigrams(string& text)
{
	vector<string> forbidden;
	{
	forbidden.push_back("àü");
	forbidden.push_back("îü");
	forbidden.push_back("åü");
	forbidden.push_back("èü");
	forbidden.push_back("óü");
	forbidden.push_back("ıü");
	forbidden.push_back("şü");
	forbidden.push_back("ÿü");
	forbidden.push_back("éü");

	forbidden.push_back("àû");
	forbidden.push_back("îû");
	forbidden.push_back("åû");
	forbidden.push_back("èû");
	forbidden.push_back("óû");
	forbidden.push_back("ıû");
	forbidden.push_back("şû");
	forbidden.push_back("ÿû");
	forbidden.push_back("éû");


	forbidden.push_back("ôá");
	forbidden.push_back("ôé");
	forbidden.push_back("ôâ");
	forbidden.push_back("ôã");
	forbidden.push_back("ôæ");
	forbidden.push_back("õæ");
	forbidden.push_back("õû");
	forbidden.push_back("øû");
	forbidden.push_back("æû");
	forbidden.push_back("øô");
	forbidden.push_back("ûû");
	forbidden.push_back("ôù");


	}

	for (int i = 0; i < forbidden.size(); i++)
	{
		size_t found = text.find(forbidden.at(i));
		if (found != string::npos)
		{
			cout << "found '" << forbidden.at(i) << "' in the text" << endl;
			return false;
		}
	}
	cout << "key is ok" << endl;
	return true;
}



//evaluate key
vector<pair<int, int>> evalkey(string& text)
{
	vector < pair<int, int>> checked;
	map<string, float> bigr = most_freq_bigr(text);
	vector<string> bigram;
	while (bigr.size() !=0)
	{
		string maxkey = getmax(bigr);
		bigram.push_back(maxkey);
		bigr.erase(maxkey);
	}

	//«ñò», «íî», «òî», «íà», «åí»
	string Y1, Y2, X1, X2;
	int Y1n, Y2n, X1n, X2n;
	int a, b;
	vector<pair<int, int>> keypairs;

	/*
	Y1 = aX1 + b (mod m^2)
	Y2 = aX2 + b (mod m^2)

	=> Y1-Y2 = a(X1 - X2)  (mod m^2)  // a(X1 - X2) = Y1-Y2  (Aa=B, a = A^-1 *B)
	b = (Y1 - aX1) (mod m^2)
	*/


	for (int i = 0; i < 5; i++)
	{
		
		X1 = top5bigr.at(i);	//«ñò», «íî», «òî», «íà», «åí»
		X1n = bigram_to_int(X1);

		for (int ii = 0; ii < 5; ii++)
		{

		Y1 = bigram.at(ii); //my conted top 5
		Y1n = bigram_to_int(Y1);



		for (int j = 0; j < bigram.size(); j++)
		{
			X2 = top5bigr.at(j); //get next in top5
			X2n = bigram_to_int(X2);
			for (int h = i + 1; h < 5; h++)
			{

				Y2 = bigram.at(h); //get next in mytop5
				Y2n = bigram_to_int(Y2);


				/*
				Y1-Y2 = a (X1 - X2) mod m^2
				*/
				vector<int> linearres;
				if (X1n - X2n != 0 && Y1n - Y2n != 0)
				{
					linearres = linear(X1n - X2n, Y1n - Y2n, pow(alpha_size, 2));
				} //get a value

				if (linearres.size() == 0) continue;

				for (int k = 0; k < linearres.size(); k++)
				{
					a = linearres.at(k);
					if (a == 0) continue;
					/*
					Y = aX + b mod m^2
					b = Y - aX
					*/
					b = mod(Y1n - a * X1n, pow(alpha_size, 2));
					pair <int, int> K = makekey(a, b);
					vector<pair<int, int>>::iterator it = find(checked.begin(), checked.end(), K);
					if (it != checked.end())
					{
						continue;
					}
					else
					{
						vector<int> textnum = text_to_num(text);
						vector<int> decnum = decode(textnum, K);
						string decoded = num_to_text(decnum);
						cout << "Key: (" << a << ", " << b << ")" << endl;
						bool test = test_forbidden_bigrams(decoded);
						if (test)
						{
							keypairs.push_back(K);
						}
						checked.push_back(K);
					}
				}

			}
		}

			}

		}


		return keypairs;
	}




//vector<pair<int, int>> testkeys(vector<pair<int, int>>& keys, string& text)
//{
//	pair<int, int> key;
//	vector<pair<int, int>> suitablekeys;
//	vector<int> textnum = text_to_num(text);
//	for (int i = 0; i < keys.size(); i++)
//	{
//		key = keys.at(i);
//		
//		vector<int> decnum = decode(textnum, key);
//		string decoded = num_to_text(decnum);
//		bool test = test_forbidden_bigrams(decoded);
//		if (test)
//		{
//			suitablekeys.push_back(key);
//		}
//	}
//
//	return suitablekeys;
//}



///////////////////////////////////////////////////////////////////////////



