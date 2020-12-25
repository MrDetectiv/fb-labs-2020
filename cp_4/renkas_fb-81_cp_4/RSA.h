#pragma once
#ifndef RSA_H
# define RSA_H
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/integer/mod_inverse.hpp>
#include <boost/random.hpp>
#include <iostream>
#include <string>
#include <ctime>
#include <tuple>

using namespace boost::multiprecision;
using namespace boost::random;
using namespace boost::integer;
using namespace std;

const int PRIME_NUMBERS[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };

// Private key part
typedef struct	PrivateKeyStruct {
	uint512_t n;
	uint512_t d;
}				PrivateKey;

// Public key part
typedef struct	PublicKeyStruct {
	uint512_t n;
	uint512_t e;
}				PublicKey;

typedef struct	KeyPairStruct {
	PublicKey publicPart;
	PrivateKey privatePart;
}				KeyPair;

typedef struct	MessegeStruct {
	PublicKey	publicKey;
	uint512_t	data;
	uint512_t	Sign;
}				Message;

class RSA
{
public:
	RSA();
	~RSA();
	KeyPair GenerateKeyPair();
	Message GenerateMessage(uint512_t data, KeyPair myKey, PublicKey recievedKey);
	uint512_t RecieveMessage(Message msg, KeyPair ownKey);
	uint512_t Encrypt(uint512_t data, PublicKey recivedKey);
	uint512_t Decrypt(uint512_t data, PrivateKey ownKey);
	uint512_t Sign(uint512_t data, PrivateKey ownKey);
	bool Verify(uint512_t k, uint512_t S, PublicKey recivedKey);

	template <typename T>
	T random_in_range(T buttom, T top)
	{
		mt19937 gen(time(0));
		uniform_int_distribution<T> uniform_range(buttom, top);
		T generated_x = uniform_range(gen);

		return generated_x;
	}
private:
	Message SendKey(uint512_t k, KeyPair myKey, PublicKey recievedKey);
	uint512_t ReceiveKey(Message msg, KeyPair ownKey);
	uint256_t get_256bit_prime();
	bool Miller_Rabin_check(uint256_t p, int k);

	template <typename T>
	T Euclidean_GCD(T a, T b)
	{
		if (b == 0) return a;
		else return Euclidean_GCD(b, a % b);
	}
};

#endif