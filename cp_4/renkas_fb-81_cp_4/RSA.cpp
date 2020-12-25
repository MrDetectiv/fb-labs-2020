#include "RSA.h"

//PUBLIC FUNCTIONS______________________________________________________________________
RSA::RSA()
{
	cout << "RSA Class created" << endl;
}

RSA::~RSA(){}

KeyPair RSA::GenerateKeyPair()
{
	KeyPair keypair;
	uint256_t p = get_256bit_prime();
	uint256_t q = get_256bit_prime();
	while (p == q)
	{
		q = get_256bit_prime();
	}
	cout << "RSA Data:" << endl;
	cout << "p: " << p << endl;
	cout << "q: " << q << endl;
	keypair.publicPart.n = (uint512_t)p * (uint512_t)q;
	keypair.privatePart.n = keypair.publicPart.n;

	uint512_t fi_n = ((uint512_t)p - 1) * ((uint512_t)q - 1);
	uint512_t test_e = random_in_range<uint512_t>((uint512_t)2, fi_n - 1); //(uint512_t)pow(2, 16) + 1;
	while (Euclidean_GCD<uint512_t>(test_e, fi_n) != 1)
	{
		test_e = random_in_range<uint512_t>((uint512_t)2, fi_n - 1);
	}
	keypair.publicPart.e = test_e;
	keypair.privatePart.d = (uint512_t)mod_inverse<int1024_t>((int1024_t)keypair.publicPart.e, (int1024_t)fi_n);
	return keypair;
}

Message RSA::GenerateMessage(uint512_t data, KeyPair myKey, PublicKey recievedKey)
{
	return SendKey(data, myKey, recievedKey);
}

uint512_t RSA::RecieveMessage(Message msg, KeyPair ownKey)
{
	return ReceiveKey(msg, ownKey);
}

uint512_t RSA::Encrypt(uint512_t data, PublicKey recivedKey)
{
	return powm(data, recivedKey.e, recivedKey.n);
}

uint512_t RSA::Decrypt(uint512_t data, PrivateKey ownKey)
{
	return powm(data, ownKey.d, ownKey.n);
}

uint512_t RSA::Sign(uint512_t data, PrivateKey ownKey)
{
	return powm(data, ownKey.d, ownKey.n);
}

bool RSA::Verify(uint512_t k, uint512_t S, PublicKey recivedKey)
{
	uint512_t k1 = powm(S, recivedKey.e, recivedKey.n);
	if (k == k1) return true;
	else return false;
}

Message RSA::SendKey(uint512_t k, KeyPair myKey, PublicKey recievedKey)
{
	Message msg;
	msg.publicKey = myKey.publicPart;
	msg.data = Encrypt(k, recievedKey);
	msg.Sign = Sign(k, myKey.privatePart);
	msg.Sign = Encrypt(msg.Sign, recievedKey);
	return msg;
}

uint512_t RSA::ReceiveKey(Message msg, KeyPair ownKey)
{
	uint512_t decrypted_k = Decrypt(msg.data, ownKey.privatePart);
	uint512_t decrypted_S = Decrypt(msg.Sign, ownKey.privatePart);
	if (Verify(decrypted_k, decrypted_S, msg.publicKey) == true)
		cout << "Sign VERIFIED!" << endl;
	else
		cout << "Sign NOT verified!" << endl;
	return decrypted_k;
}


//PRIVATE FUNCTIONS______________________________________________________________________
uint256_t RSA::get_256bit_prime()
{
	uint256_t n1 = ~((uint256_t)0);						//n1 = MAX 256bit number
	uint256_t n0 = ((uint256_t)(1)) << 255;				//n0 = MIN 256bit number
	uint256_t x = random_in_range<uint256_t>(n0, n1);	//Generating num = random 256bit number
	x = x | 1;											//num is neparne  
	uint256_t m0 = x;

	bool can_be_prime;
	cout << "Generating prime number" << endl;
	for (uint256_t i = 1; i < (n1 - m0) / 2; i++)		//i = 1, 2 ... (n1 - m0) / 2
	{
		can_be_prime = true;
		cout << "Testing " << x << endl;
		for (int j = 0; j < 25; j++)					//Check on prime numbers (first 25)
		{
			if (x % PRIME_NUMBERS[j] == 0)
			{
				can_be_prime = false;
				cout << "Not prime, can be divided by " << PRIME_NUMBERS[j] << endl;
				break;
			}
		}
		if (can_be_prime == true)
		{
			if (Miller_Rabin_check(x, 20) == true)		//Miller Rabin check (k = 20)
			{
				break;
			}
		}
		x += 2;
	}
	//cout << endl;
	return x;
}

bool RSA::Miller_Rabin_check(uint256_t p, int k)
{
	uint256_t d = p - 1;
	uint256_t s = 0;
	uint256_t x;
	uint256_t gcd;
	uint256_t powm_result;

	// Finding p - 1 = d * 2^s
	while (d % 2 == 0)
	{
		d /= 2;
		s++;
	}

	//k iterations of random checks
	for (int i = 0; i < k; i++)
	{
		x = random_in_range<uint256_t>(1, p);												//(Step 1) Random 1 < x < p
		gcd = Euclidean_GCD<uint256_t>(p, x);												//Calculating GCD p and x
		if (gcd > 1)																		//(Step 1) gcd > 1 ---> p is not prime
		{
			cout << "gcd(x, p) > 1, p is not prime" << endl;
			return false;
		}
		powm_result = powm(x, d, p);														//powm_result = x^d mod p
		if (powm_result == 1 || powm_result == p - 1)										//(Step 2.1) x^d mod p = +-1 ---> p - strongly sudo-prime
		{
			cout << "x^d mod p = +-1, p - strongly sudo-prime" << endl;
			return true;
		}

		for (size_t r = 1; r < s; r++)														//(Step 2.2) r iterations 
		{
			powm_result = powm(x, d * (uint256_t)pow(2, r), p);								//powm_result = x ^ (d * 2 ^ ri) mod p
			if (powm_result == p - 1)														//(Step 2.2.1) powm_result = -1 ---> p - strongly sudo-prime
			{
				cout << "x ^ (d * 2 ^ ri) mod p = -1, p - strongly sudo-prime" << endl;
				return true;
			}
			else if (powm_result == 1)														//(Step 2.2.2) powm_result = 1 ----> p - not strongly sudo-prime
			{
				cout << "x ^ (d * 2 ^ ri) mod p = 1, p - not strongly sudo-prime" << endl;
				return false;
			}
		}
	}
	cout << "Iterations ended, p maybe prime, or maybe not" << endl;
	return false;																			// Here is no precise answer (better 0)
}


