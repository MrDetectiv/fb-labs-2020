#include "sidefunc.h"


/********************************************KEY GENERATOR*********************************************************/
pair <cpp_int, cpp_int> Pers::gen_publickey(cpp_int &p, cpp_int &q, cpp_int &phi_n, size_t &size)
{
	cpp_int e;
	bool flag = false;
	
	while (!flag)
	{
		e = 2 + gen_num(size) % (phi_n - 3);
		flag = (gcd(e, phi_n) == 1);
	}

	//(n, e)
	return make_pair(p * q, e);

}

pair< tuple<cpp_int, cpp_int, cpp_int>, pair<cpp_int, cpp_int>> Pers::gen_keyset(size_t &size)
{
	cout << "Key pair generating..." << endl;
	cpp_int p = gen_prime(size);
	cpp_int q = gen_prime(size);

	cpp_int phi_n = prime_euler(p, q);

	pair<cpp_int, cpp_int> publickey = gen_publickey(p, q, phi_n, size);

	cpp_int d = inverse_mod(publickey.second, phi_n);

	tuple<cpp_int, cpp_int, cpp_int> privatekey = make_tuple(d, p, q);

	pair< tuple<cpp_int, cpp_int, cpp_int>, pair<cpp_int, cpp_int>> keyset = make_pair(privatekey, publickey);
	cout << "Key pair generated" << endl;
	return keyset; 
}

void Pers::setkey(size_t size = 256)
{
	pair< tuple<cpp_int, cpp_int, cpp_int>, pair<cpp_int, cpp_int>> keyset = gen_keyset(size);
	this->publickey = keyset.second;
	this->privatekey = keyset.first;
}


/****************************************************CONSTRUCTOR****************************************************/
Pers::Pers(size_t size = 256)
{
	//pair< tuple<cpp_int, cpp_int, cpp_int>, pair<cpp_int, cpp_int>> keyset = gen_keyset();
	//this->publickey = keyset.second;
	//this->privatekey = keyset.first;
	this->setkey(size);
}

Pers::Pers(pair<cpp_int, cpp_int> publ)
{
	this->publickey = publ;
}

Pers::Pers(string path/*cpp_int n, cpp_int e, cpp_int d, cpp_int p, cpp_int q*/)
{
	ifstream fin;
	fin.open(path);
	pair <cpp_int, cpp_int> ne;
	tuple<cpp_int, cpp_int, cpp_int> dpq;
	cpp_int n, e, d, p, q;
	//check for file open failure
	if (fin.fail())
	{
		cout << "Error opening user key file" << endl;
		fin.close();
		
		ne = make_pair(0, 0);
	}
	else
	{
		cout << "User key file is opened successfully" << endl;

		fin >> hex >> n;
		fin >> hex >> e;
		fin >> hex >> d;
		fin >> hex >> p;
		fin >> hex >> q;


		ne = make_pair(n,e);
		dpq = make_tuple(d, p, q);
	}

	ne = make_pair(n, e);
	this->publickey = ne;

	dpq = make_tuple(d, p, q);
	this->privatekey = dpq;
}

/****************************************************GETTERS********************************************************/
pair<cpp_int, cpp_int> Pers::getpublickey()
{
	return this->publickey;
}

//tuple<cpp_int, cpp_int, cpp_int> Pers::getprivatekey()
//{
//	return this->privatekey;
//
//}


/******************************************************ENCRYPTION****************************************************/
cpp_int Pers::encrypt(cpp_int M, pair<cpp_int, cpp_int> & publkey)
{	
	//n = publickey.first;
	//e = publickey.second;
	// 0 <= M <= n-1

	if (M > publkey.first - 1 || M < 0)
	{
		return 0;
	}

	// C = M^e mod n

	return horner_pow(M, publkey.second, publkey.first);
}

cpp_int Pers::decrypt(cpp_int C)
{
	// d = privatekey<0>
	// n = publickey.first
	cout << "Decrypting..." << endl;

	cpp_int d;
	tie(d, ignore, ignore) = this->privatekey;
	
	//cout << "d=" << d << endl;

	// M = C^d mod n
	return horner_pow(C, d, this->publickey.first);
}


/******************************************************SIGNATURE****************************************************/
pair< cpp_int, cpp_int> Pers::sign_message(cpp_int& M)
{
	// d = privatekey<0>
	// n = publickey.first
	cout << "Signing message..." << endl;
	cpp_int d;
	tie(d, ignore, ignore) = this->privatekey;
//	cout << "Message: " << M << endl;
//	cout << "d = " << d << endl;

	// S = M^d mod n
	cpp_int S = horner_pow(M, d, this->publickey.first);

	//cout << "S = M^d mod n = " << S << endl;
	cout << "Message signed" << endl;
	return make_pair(M, S);

}

bool Pers::check_signature(/*pair< cpp_int, cpp_int> sign_mes*/cpp_int M, cpp_int S, pair< cpp_int, cpp_int> publickey)
{
	// M = sign_mes.first
	// S = sign_mes.second
	// n = publickey.first
	// e = publickey.second

	// M = S^e mod n

	cout << "Checking signature" << endl;

	cout << "Message: " << /*sign_mes.first */M<< endl;
	cout << "M = S^e mod n = " << horner_pow(/*sign_mes.second*/S, publickey.second, publickey.first) << endl;


	if (horner_pow(/*sign_mes.second*/S, publickey.second, publickey.first) == /*sign_mes.first*/M)
	{
		cout << "Signature verified" << endl;
		return true;
	}

	else
	{
		cout << "Signature not verified" << endl;
		return false;
	}

}


/******************************************************RSA PROTOCOL***************************************************/
pair< cpp_int, cpp_int> Pers::RSA_sender(Pers &B, cpp_int k)
{

	{////pair<cpp_int, cpp_int> Apublic = this->publickey;
	

	//// public key: (n,e)

	//// An = Apublic.first
	//// Ae = Apublic.second
	//// Bn = Bpublic.first
	//// Be = Bpublic.second

	//// private key: (d, p, q)
	//// Apriv = this->privatekey
	//// A_d = get<0>this->privatekey
	}

	pair<cpp_int, cpp_int> Bpublic = B.getpublickey();
	if (this->publickey.first > Bpublic.first)
	{
		cout << "Unable to send key, another sender key needed" << endl;
		this->setkey();
		this->printpublickey();

		/*cout << "***************************************************************************" << endl;
		cout << endl << "Chris" << endl;
		this->printpublickey();
		cout << "---------------" << endl;
		this->printprivatekey();
		cout << "***************************************************************************" << endl;
		cout << endl << endl;*/

		return RSA_sender(B, k);
	}

	cpp_int S = sign_message(k).second;

	cout << "Signature for key " << k << ":	" << S << endl;

	S = encrypt(S, Bpublic);

	cout << "Encrypted signature:	" << S << endl;

	k = encrypt(k, Bpublic);

	cout << "Encrypted key:	" << k << endl;

	return make_pair(k, S);

}

cpp_int Pers::RSA_reciever(Pers &A, /*pair<cpp_int, cpp_int> mes*/cpp_int &M, cpp_int &S)
{
	pair<cpp_int, cpp_int> Apublic = A.getpublickey();

	// mes = (k1, S1)
	// k = k1 ^ Bd mod Bn
	// S = S1 ^ Bd mod Bn

	// An = Apublic.first
	// Ae = Apublic.second

	// B_d = get<0>this->privatekey
	// B_n = this->publickey.first

	cpp_int k = /*mes.first*/M;
	cpp_int Ss = /*mes.second*/S;
	/*cout << endl << k << endl;*/
	k = decrypt(k);
	cout << "Decrypted key:	" << k << endl;
	/*cout << k << endl << Ss << endl;*/
	Ss = decrypt(Ss);
	cout << "Decrypted signature:	" << Ss << endl;
	/*cout << Ss << endl << endl;*/

	//// k == S^ A_e mod A_n
	//pair<cpp_int, cpp_int> sign = make_pair(k, Ss);
	if (check_signature(/*sign*/k, Ss, Apublic))
	{
		cout << "Key recieved" << endl;
		return k;
	}

	else
	{
		cout << "Authentication failed" << endl;
		return 0;
	}

}


/**********************************************************PRINT****************************************************/
void Pers::printpublickey()
{
	cout << "Modulus:" << endl;
	cout << hex << this->publickey.first << endl;
	cout << "Public exponent: " << endl;
	cout << hex<< this->publickey.second << endl;
}


void Pers::printprivatekey()
{
	// d p q
	cout << "d:" <</* hex <<*/ get<0>(this->privatekey) << endl;
	cout << "p:" <</* hex <<*/ get<1>(this->privatekey) << endl;
	cout << "q:" <</* hex <<*/ get<2>(this->privatekey) << endl;
}

/******************************************************SERVER*******************************************************/

Pers Pers::cr_s(string path/*="serv_k.txt"*/)
{
	ifstream fin;
	fin.open(path);
	pair <cpp_int, cpp_int> server_key;
	//check for file open failure
	if (fin.fail())
	{
		cout << "Error opening server key file" << endl;
		fin.close();
		//system("PAUSE");
		server_key = make_pair(0, 0);

		//Pers Server(server_key);
		//return Server;

	}
	else
	{
		cout << "Server key file is opened successfully" << endl;

		cpp_int serv_key_n, serv_key_e;

		//for (int i = 0; i < 2; i++)
		//{
		//	if (i == 0)
		//	{
		fin >> hex >> serv_key_n;
		//}

		//if (i == 1)
		//{
		fin >> hex >> serv_key_e;
		//	}

		//}

		server_key = make_pair(serv_key_n, serv_key_e);
	}

	Pers Server(server_key);
	return Server;
	}


