#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <iomanip>
#include <vector>
#include <windows.h>
#include <stdio.h>
using namespace std;
using boost::multiprecision::cpp_int;

int whoami = -1;
bool message = 0;

cpp_int p1;
cpp_int p2;
cpp_int q1;
cpp_int q2;
cpp_int n1;
cpp_int n2;
cpp_int e1;
cpp_int e2;
cpp_int d1;
cpp_int d2;

void SwitchUser(string who)
{
	if (who == "Admin")
	{
		whoami = -1;
		cout << "User switched to Admin ..." << endl;
	}
	else if (who == "Alice")
	{
		whoami = 0;
		cout << "User switched to Alice ..." << endl;
	}
	else if (who == "Bob")
	{
		whoami = 1;
		cout << "User switched to Bob ..." << endl;
	}
	else
	{
		cout << "ERROR: Unknown user" << endl;
	}
}

void TellWhoami()
{
	if (whoami == -1)
	{
		cout << "You are Admin now ..." << endl;
	}
	else if (whoami == 0)
	{
		cout << "You are Alice now ..." << endl;
	}
	else if (whoami == 1)
	{
		cout << "You are Bob now ..." << endl;
	}
}

string Whoami()
{
	if (whoami == -1)
	{
		return "Admin";
	}
	else if (whoami == 0)
	{
		return "Alice";
	}
	else if (whoami == 1)
	{
		return "Bob";
	}
}

void find_random_bin(int bin_mas[], int sz)
{
	srand(time(NULL));
	for (int i = 0; i < sz; i++)
	{
		bin_mas[i] = rand() % 2;
	}
}

cpp_int bin_to_int(int bin_mas[], int sz)
{
	cpp_int answer = 0;
	for (int i = 0; i < sz; i++)
	{
		answer += (cpp_int)(pow(2, i)*bin_mas[i]);
	}
	return answer;
}

int * int_to_bin(cpp_int a)
{
	int counter = 1;
	cpp_int temp = a;
	while (temp / 2 != 0)
	{
		counter++;
		temp = temp / 2;
	}
	int * mas = new int[counter+1];
	temp = a;
	counter = 0;
	while (temp / 2 != 0)
	{
		mas[counter] = (int)(temp % 2);
		counter++;
		temp = temp / 2;
	}
	mas[counter] = 1;
	return mas;
}

cpp_int pow(cpp_int x, cpp_int d)
{
	cpp_int answer = 1;
	for (cpp_int i = 0; i < d; i++)
	{
		answer *= x;
	}
	return answer;
}

cpp_int a_pow_b_mod_c_bin(cpp_int a, cpp_int b, cpp_int c)
{
	int * mas = new int[4096];
	mas = int_to_bin(b);
	int counter = 0;
	while (mas[counter+1] == 1 || mas[counter+1] == 0)
	{
		counter++;
	}
	counter++;
	cpp_int answer = 1;


	for (int i = counter-1; i >= 0; i--)
	{
		//cout << answer << endl;
		answer = answer * answer;
		if (answer > c)
		{
			answer = (answer - ((answer / c)*c));
		}
		//cout << answer << endl;
		answer = answer * pow(a, mas[i]);
		if (answer > c)
		{
			answer = (answer - ((answer / c)*c));
		}
		//cout << answer << endl;
		//cout << endl;
	}
	return answer;
}


cpp_int a_pow_b_mod_c(cpp_int a, cpp_int b, cpp_int c)
{
	cpp_int answer = 1;
	for (cpp_int i = 0; i < b; i++)
	{
		answer *= a;
		if (answer > c)
		{
			answer = (answer -((answer/c)*c));
		}
	}
	return answer;
}


cpp_int pow_mod(cpp_int x, cpp_int d, cpp_int p)
{
	cpp_int answer = 1;
	for (cpp_int i = 0; i < d; i++)
	{
		//cout << "kek";
		answer *= x;
		if (answer >= p)
		{
			//answer = answer % p;
			//answer = mod(answer, p);
			answer = (answer - ((answer / p)*p));
		}
	}
	return answer;
}

cpp_int mod(cpp_int x, cpp_int p)
{

	int counter = 0;
	cpp_int answer = 0;
	cpp_int temp = x;
	do
	{
		temp = temp / 10;
		counter++;
	} while (temp!= 0);
	int *mas = new int[counter];
	temp = x;
	for (int i = 0; i < counter; i++)
	{
		mas[i] = (int)(temp - (temp / 10) * 10);
		temp = temp / 10;
	}
	temp = x;
	cpp_int r = 0;
	for (int i = 0; i < counter; i++)
	{
		r = pow_mod((cpp_int)10, (cpp_int)i, p);
		answer =answer + mas[i] * r;
		if (answer >= p)
		{
			answer = (answer - ((answer / p)*p));
		}
	}

	return answer;
}

bool is_simple(cpp_int p, int sz)
{
	//cout << "Simple check has begun ..." << endl;
	int mas[8] = {3,5,7,11,13,17,19,23};
	for (int i = 0; i < 8; i++)
	{
		cpp_int modul = mod(p, mas[i]);
		//cout << "p mod" << mas[i] << " = " << modul << endl;
		if (modul == 0)
		{
			//cout << "p mod" << mas[i] << " = " << modul << endl;
			//cout << "Simple check end 01." << endl;
			return 0;
		}
	}

	int k = 4;

	//cout << "KROK 0" << endl;
	cpp_int s = 0;
	cpp_int d = p-1;
	while (mod(d,2) == 0)
	{
		d = d / 2;
		s++;
	}
	cpp_int counter = 0;
	//cout << "s = " << s << endl;
	//KROK 1
	int *x_bin_mas = new int[sz];
	cpp_int x = p + 1;
	while (counter < k)
	{
		//cout << "KROK 1" << endl;
		x = p + 1;
		while (x >= p)
		{
			find_random_bin(x_bin_mas, sz);
			x = bin_to_int(x_bin_mas, sz);
		}
		if (gcd(x, p) > 1)
		{
			//cout << "Simple check end 02." << endl;
			return 0;
		}

		//cout << "KROK 2" << endl;
		//cpp_int xr = a_pow_b_mod_c_bin(x, d, p);
		cpp_int xr = powm(x, d, p);
		/*cout << "x = " << x << endl;
		cout << "d = " << d << endl;
		cout << "p = " << p << endl;
		cout << "xr = " << xr << endl;*/
		bool is_pseudo_simple = 0;
		if (xr == 1 || xr == p-1)
		{
			is_pseudo_simple = 1;
		}
		else
		{
			for (cpp_int r = 1; r < s; r++)
			{
				//xr = a_pow_b_mod_c_bin(xr, 2, p);
				cpp_int xr = powm(xr, 2, p);
				//cout << "r = " << r << endl;
				//cout << "xr = " << xr << endl;
				if (xr == p-1)
				{
					is_pseudo_simple = 1;
				}
				else if (xr == 1)
				{
					//cout << "Simple check end 03." << endl;
					return 0;
				}
			}
		}

		if (is_pseudo_simple == 0)
		{
			//cout << "Simple check end 04." << endl;
			return 0;
		}
		counter++;
		//cout << "KROK 3" << endl;
	}

	//cout << "Simple check end 1." << endl;
	return 1;
}


cpp_int find_random_simple(int bin_mas[], int sz)
{
	cout << "Searching random simple has begun ..." << endl;
	srand(time(NULL));
	for (int i = 1; i < sz-1; i++)
	{
		bin_mas[i] = rand() % 2;
	}
	bin_mas[0] = 1;
	bin_mas[sz-1] = 1;

	cpp_int p = bin_to_int(bin_mas, sz);
	cout << "First candidate: " << p << endl;
	while (is_simple(p, sz) == 0)
	{
		//cout << p << endl;
		p += 2;
		cout << /*"candidate: " <<*/ p << endl;
	}
	cout << "Сhousen number: " << p << endl;
	cout << "Searching random simple end." << endl;
	return p;
}

cpp_int q_mas_gcd(cpp_int m, cpp_int a, cpp_int q_mas[], int i)
{
	if (a == 0)
	{
		return m;
	}
	else
	{
		q_mas[i] = m / a;
		return q_mas_gcd(a, m%a, q_mas, i + 1);
	}
}

cpp_int reverse(cpp_int a, cpp_int m)
{
	cpp_int *q_mas = new cpp_int[100000];
	cpp_int *v_mas = new cpp_int[100000];
	for (int i = 0; i < 100000; i++)
	{
		q_mas[i] = 0;
		v_mas[i] = 0;
	}
	v_mas[1] = 1;

	cpp_int gcd = q_mas_gcd(m, a, q_mas, 0);
	if (gcd != 1)
	{
		return 0;
	}
	else
	{
		int h = 1;
		cpp_int v_max = 0;
		while (q_mas[h] != 0)
		{
			v_mas[h + 1] = v_mas[h - 1] + (-1)*q_mas[h - 1] * v_mas[h];
			v_max = v_mas[h + 1];
			h++;
		}

		if (v_max < 0)
		{
			v_max = v_max + m;
		}

		return v_max;
	}
}

cpp_int * CreateKeys(cpp_int p, cpp_int q)
{
	//cout << "Keys generation has begun ..." << endl;
	cpp_int n = p * q;
	cpp_int fn = (p - 1)*(q - 1);
	cpp_int e = pow((cpp_int)2, (cpp_int)12) + 1;
	cpp_int d = reverse(e, fn);
	cpp_int *key_mas = new cpp_int[3];// n e d
	key_mas[0] = n;
	key_mas[1] = e;
	key_mas[2] = d;
	//cout << "Keys were generated." << endl;
	return key_mas;
}

cpp_int * GenerateKeyPair(int sz)
{
	//cout << "p, q generation has begun ..." << endl;
	int *bin_mas = new int[sz];
	cpp_int *simple_mas = new cpp_int[2];
	//cout << "Searching of p has begun ..." << endl;
	simple_mas[0] = find_random_simple(bin_mas, sz);
	//cout << "Searching of q has begun ..." << endl;
	simple_mas[1] = find_random_simple(bin_mas, sz);
	while (simple_mas[1] == simple_mas[0])
	{
		simple_mas[1] = find_random_simple(bin_mas, sz);
	}
	//cout << "p, q pair generation end." << endl;
	cpp_int *keys_mas = new cpp_int[3];
	keys_mas = CreateKeys(simple_mas[0], simple_mas[1]);
	cpp_int *all_keys_mas = new cpp_int[5]; //p q n e d
	all_keys_mas[0] = simple_mas[0];
	all_keys_mas[1] = simple_mas[1];
	all_keys_mas[2] = keys_mas[0];
	all_keys_mas[3] = keys_mas[1];
	all_keys_mas[4] = keys_mas[2];
	return all_keys_mas;
}

void PrintKeys(string a, string b)
{
	if (a == "Alice")
	{
		if (b == "Close")
		{
			cout << "Alice Close keys: " << "d = " << d1 << "; p = " << p1 << "; q = " << q1 << endl;
		}
		else if (b == "Open")
		{
			cout << "Alice Open keys: " << "e = " << e1 << "; n = " << n1 << endl;
		}
		else
		{
			cout << "ERROR: Unknown keys" << endl;
		}
	}
	else if (a == "Bob")
	{
		if (b == "Close")
		{
			cout << "Bob Close keys: " << "d = " << d2 << "; p = " << p2 << "; q = " << q2 << endl;
		}
		else if (b == "Open")
		{
			cout << "Bob Open keys: " << "e = " << e2 << "; n = " << n2 << endl;
		}
		else
		{
			cout << "ERROR: Unknown keys" << endl;
		}
	}
	else
	{
		cout << "ERROR: Unknown user" << endl;
	}
}

cpp_int Encrypt(cpp_int m, cpp_int key, cpp_int n)//key = e ИЛИ d
{
	cout << "Encryption has begun ..." << endl;
	cout << "Message = " << m << "; d = " << key << "; n = " << n << endl;
	cpp_int c1 = a_pow_b_mod_c_bin(m, key, n);
	cout << c1 << endl;
	cout << "Encypted message = " << c1 << endl;
	cout << "Encryption end." << endl;
	return c1;
}

cpp_int GetCloseKey()
{
	if (whoami == -1)
	{
		cout << "ERROR: You are admin" << endl;
	}
	else
	{
		if (whoami == 0)
		{
			return d1;
		}
		else if (whoami == 1)
		{
			return d2;
		}
	}
}

cpp_int * GetOpenKeys(string whos)
{
	cpp_int * open_keys = new cpp_int[2];
	if (whos == "Alice")
	{
		open_keys[0] = e1;
		open_keys[1] = n1;
	}
	else if (whos == "Bob")
	{
		open_keys[0] = e2;
		open_keys[1] = n2;
	}
	else
	{
		cout << "ERROR: Unknown user" << endl;
		return NULL;
	}
	return open_keys;
}

cpp_int Decrypt(cpp_int c, cpp_int key, cpp_int n)//key = e ИЛИ d
{
	cout << "Dencryption has begun ..." << endl;
	cout << "Encrypted message = " << c << "; e = " << key << "; n = " << n << endl;
	cpp_int m1 = a_pow_b_mod_c_bin(c, key, n);
	cout << "Decrypted message = " << m1 << endl;
	cout << "Dencryption end." << endl;
	return m1;
}

cpp_int * Sign(cpp_int m, cpp_int d, cpp_int n)
{
	cout << "Signing ..." << endl;
	cpp_int s = Encrypt(m, d, n);
	cpp_int * mssg = new cpp_int[2];
	mssg[0] = m;
	mssg[1] = s;
	return mssg;
}

bool Verify(cpp_int mssg[], cpp_int e, cpp_int n)
{
	cout << "Verifying ..." << endl;
	if (mssg[0] == Decrypt(mssg[1], e, n))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

//openkeys = {e,n}
cpp_int * SendKey(cpp_int k, string receiver)
{
	cout << "Key sending has begun ..." << endl;
	if (message == 1)
	{
		cout << "Unreceived message already exist, wait for receiving." << endl;
		return 0;
	}

	cpp_int * receiver_open_keys = new cpp_int[2];
	cpp_int * sender_open_keys = new cpp_int[2];
	cpp_int sender_close_key;
	sender_close_key = GetCloseKey();
	receiver_open_keys = GetOpenKeys(receiver);
	sender_open_keys = GetOpenKeys(Whoami());
	cpp_int k1 = Encrypt(k, receiver_open_keys[0], receiver_open_keys[1]);
	cpp_int * sign_mssg = new cpp_int[2];
	sign_mssg = Sign(k, sender_close_key, sender_open_keys[1]);
	cpp_int s1 = Encrypt(sign_mssg[1], receiver_open_keys[0], receiver_open_keys[1]);

	cout << "k1 = " << k1 << endl;
	cout << "s = " << sign_mssg[1] << endl;
	cout << "s1 = " << s1 << endl;

	cpp_int * mssg = new cpp_int[2];
	mssg[1] = s1;
	mssg[0] = k1;
	message = 1;
	cout << "Key sended." << endl;
	return mssg;
}

cpp_int * ReceiveKey(cpp_int mssg[], string sender)
{
	cout << "Key receiving has begun ..." << endl;
	if (message == 0)
	{
		cout << "No message to receive." << endl;
		return 0;
	}
	cpp_int * mssg2 = new cpp_int[2];
	cpp_int * receiver_open_keys = new cpp_int[2];
	cpp_int * sender_open_keys = new cpp_int[2];
	cpp_int receiver_close_key;
	receiver_close_key = GetCloseKey();
	sender_open_keys = GetOpenKeys(sender);
	receiver_open_keys = GetOpenKeys(Whoami());

	cpp_int k = Decrypt(mssg[0], receiver_close_key, receiver_open_keys[1]);
	cpp_int s = Decrypt(mssg[1], receiver_close_key, receiver_open_keys[1]);
	message = 0;
	mssg2[0] = k;
	mssg2[1] = s;
	cout << "k = " << k << endl;
	cout << "s = " << s << endl;
	if (Verify(mssg2, sender_open_keys[0], sender_open_keys[1]))
	{
		cout << "Message verified!" << endl;
	}
	else
	{
		cout << "ERROR Message is not verified" << endl;
	}
	cout << "Key receiving end." << endl;
	return mssg2;
}

int main()
{
	cout << "Beginning of program ..." << endl;
	int sz;
	cout << "Enter sz : ";
	cin >> sz;
	cpp_int *alice_keys = new cpp_int[5];
	alice_keys = GenerateKeyPair(sz);
	p1 = alice_keys[0];
	q1 = alice_keys[1];
	n1 = alice_keys[2];
	e1 = alice_keys[3];
	d1 = alice_keys[4];
	cout << "Alice keys generated." << endl;

	cpp_int *bob_keys = new cpp_int[5];
	bob_keys = GenerateKeyPair(sz);
	while (bob_keys[0] * bob_keys[1] <= alice_keys[0] * alice_keys[1])
	{
		bob_keys = GenerateKeyPair(sz);
	}
	p2 = bob_keys[0];
	q2 = bob_keys[1];
	n2 = bob_keys[2];
	e2 = bob_keys[3];
	d2 = bob_keys[4];
	cout << "Bob keys generated." << endl;

	cout << endl;
	PrintKeys("Alice", "Open");
	PrintKeys("Alice", "Close");
	PrintKeys("Bob", "Open");
	PrintKeys("Bob", "Close");
	cout << endl;

	int *bin_mas = new int[sz];
	find_random_bin(bin_mas, sz);
	cpp_int m = bin_to_int(bin_mas, sz);
	while (m >= n1)
	{
		find_random_bin(bin_mas, sz);
		m = bin_to_int(bin_mas, sz);
	}
	cout << "Message = " << m << endl;

	SwitchUser("Alice");
	cpp_int *mssg = new cpp_int[2];
	cpp_int *my_open_keys = new cpp_int[2];
	my_open_keys = GetOpenKeys(Whoami());
	cpp_int my_close_key = GetCloseKey();
	mssg = Sign(m, my_close_key, my_open_keys[1]);

	SwitchUser("Bob");
	cpp_int *alice_open_keys = new cpp_int[2];
	alice_open_keys = GetOpenKeys("Alice");
	if (Verify(mssg, alice_open_keys[0], alice_open_keys[1]))
	{
		cout << "Message verified!" << endl;
	}
	else
	{
		cout << "ERROR Message is not verified" << endl;
	}

	cout << endl;
	cpp_int *mssg1 = new cpp_int[2];
	mssg1 = SendKey(m, "Alice");
	SwitchUser("Alice");
	cpp_int *mssg2 = new cpp_int[2];
	mssg2 = ReceiveKey(mssg1, "Bob");

	return 0;
}
