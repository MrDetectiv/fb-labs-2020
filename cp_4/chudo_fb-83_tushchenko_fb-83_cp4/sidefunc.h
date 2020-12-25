#include "Header.h"

// a mod b
cpp_int mod(cpp_int a, cpp_int b)
{
	return (a % b + b) % b;
}

// x^m mod p
cpp_int horner_pow(cpp_int x, cpp_int m, cpp_int p)
{
	x = x % p;
	cpp_int y = 1;
	vector<cpp_int> e_s;
	// m = e0 + e1*2+e2*2^2 +...
	//cout << "binary of " << m << endl;
	while (m != 0)
	{
		e_s.push_back(m % 2);
			m /= 2;
	}
	//e_s basicly stores reversed binary of m
	
	
	
	/*for (int i = e_s.size() - 1; i >= 0; i--)
	{
		cout << e_s.at(i);
	}
	cout << endl;*/

	for (int i = e_s.size() - 1; i >=0 ; i--)
	{
		// y = y * x^ei
		// y = y * y

		//cout << "step" << i << "	y=" << y << "	e=" << e_s.at(i) <<endl;
		if (e_s.at(i) == 1)
		{
			y = (y * x) % p;
		//	cout << "y = (y * x) % p = " << y<< endl;
		}

		if (i == 0)
		{
			break;
		}

		y = (y * y) % p;
		//cout << "y = (y * y) % p = " << y << endl;
	}


	return y;
}

//eea for gcd and inverse
pair<cpp_int, cpp_int> eea(cpp_int a, cpp_int b)
{
	pair<cpp_int, cpp_int> res; //gcd, inv

	vector<cpp_int> Rvalues;
	Rvalues.push_back(a);
	Rvalues.push_back(b);

	vector<cpp_int> Uvalues;
	Uvalues.push_back(1);
	Uvalues.push_back(0);

	vector<cpp_int> Vvalues;
	Vvalues.push_back(0);
	Vvalues.push_back(1);

	bool flag = false;

	cpp_int r, q, u, v;

	for (int i = 2; !flag; i++)
	{

		r = Rvalues.at(i - 2) % Rvalues.at(i - 1);

		if (r == 0)
		{
			flag = true;
			break;
		}

		q = Rvalues.at(i - 2) / Rvalues.at(i - 1);

		u = Uvalues.at(i - 2) - q * Uvalues.at(i - 1);

		v = Vvalues.at(i - 2) - q * Vvalues.at(i - 1);

		Uvalues.push_back(u);
		Vvalues.push_back(v);
		Rvalues.push_back(r);

	}

	r = Rvalues.back();
	u = Uvalues.back();

	res = make_pair(r, u);

	return res;
}

//gcd (a, m)
cpp_int gcd(cpp_int a, cpp_int m)
{
	pair<cpp_int, cpp_int> ee = eea(a, m);
	return ee.first;
}

// a^-1 mod m
cpp_int inverse_mod(cpp_int a, cpp_int m)
{
	pair <cpp_int, cpp_int> ee; //gcd, inv
	ee = eea(a, m);

	if (ee.first != 1)
	{
		cout << a << "^-1  (mod " << m << ")  doesn`t exist" << endl;
		return 0;
	}

	else
	{
		return mod(ee.second, m);
	}

}

/////////////////////////////////////////////////////////////

cpp_int gen_num(size_t size)
{
//documentation in comments below

//generator
//mt19937
//length of cycle
//2^19937 - 1
//approx. memory requirements
//625 * sizeof(uint32_t)
//approx. speed compared to fastest
//93 %
//comment
//good uniform distribution in up to 623 dimensions

//distribution
//uniform_int_distribution
//explanation
//discrete uniform distribution on a set of integers; the underlying generator may be called several times to gather enough randomness for the output
//example
//drawing from an urn


	cpp_int b = 1;
	cpp_int maxval = b << size; 
	cpp_int minval = b << (size - 1);

	mt19937 gen((static_cast<unsigned int>(std::time(0)))); //seeding with time
	uniform_int_distribution<cpp_int> unidistr(minval, maxval);

	return unidistr(gen);
}

////////////////////////////////////////////////////////////

bool trial_division(cpp_int num)
{

	for (int i=0; i<dividers.size(); i++)
	{
		if (num % dividers.at(i) == 0)
		{
			//cout << "divisible to " << dividers.at(i) << endl;
			return false;
		}
	}

	return true;
}

bool miller_rabin(cpp_int p, size_t &size)
{
	cpp_int k = 100;//1000 + rand() % 9000;
	vector<cpp_int> used_x;
	cpp_int x = 0;
	cpp_int d, s;
	int	counter = 0;
	s = 0;
	d = p - 1;



	//find d and s values
	// p-1 = d * 2^s
	while (d % 2 == 0)
	{
		d /= 2;
		s++;
	}

	for (counter; counter < k; counter++)
	{
		bool flag = false;
		//generate x
		while (!flag)
		{
			//generate x
			 x = 2 + gen_num(size) % (p - 4); // 1<x<p
			//check if this x value was already chosen
			vector<cpp_int>::iterator it = find(used_x.begin(), used_x.end(), x);
			if (it == used_x.end())
			{ //if not in used_x go next step
				flag = true;
				used_x.push_back(x);
			}
		}

		// check if p is pseudo prime for x
		if (gcd(x, p) > 1)
		{
			return false;
		}

		else
		{

			// p is strongly pseudo prime for x
			if (horner_pow(x, d, p)== 1 || horner_pow(x, d, p) == p-1)
			{
				continue;
			}
			
			else
				//x_r = x^(d*2^r)
			{
				// xrc = x^d mod p
				cpp_int xrc = x;/*= /*mod(pow(x, d), p) power(x, /*d2, p)*/
							
				bool prime_flag = false;
				for (int r = 1; r <= s-1; r++)
				{
					//x_r = x_r-1 ^2
					xrc = /*mod(pow(xrc, 2), p)*/horner_pow(xrc, d, p);

					// p is strongly pseudo prime for x
					if (xrc == p-1) 
					{
						prime_flag = true;
						break;
					}
					else 
						 // p is not strongly pseudo prime for x
						if (xrc == 1)
						{
							return false;
						}

				}
				if (!prime_flag)
				{
					return false;
				}

			}

		}
	}
	return true;
}

bool try_prime(cpp_int num, size_t &size)
{
	//cout <<hex << num;
	if (!trial_division(num))
	{
		//cout << "	failed trial division" << endl;
		return false;
	}
	else if (!miller_rabin(num, size))
	{
	//	cout << "	failed miller rabin" << endl;
		return false;
	}
	
	else
	{
	//	cout << "	is pseudo prime" << endl;
		return true;
	}

}

///////////////////////////////////////////////////////////


 cpp_int gen_prime(size_t size = 256)
{
	
	bool flag = false;
	cpp_int p;
	while (!flag)
	{
		//if (size == 256)
		//{
		//	p = gen256();
		//}
		//else if (size == 512)
		//{
		//	p = gen512();
		//}
		//else if (size == 1024)
		//{
		//	p = gen1024();
		//}
		p = gen_num(size);
	//	cout << p << endl;
		flag = try_prime(p, size);

	}
	return p;
}

cpp_int prime_euler(cpp_int &num1, cpp_int &num2)
{
	return (num1 - 1) * (num2 - 1);
}