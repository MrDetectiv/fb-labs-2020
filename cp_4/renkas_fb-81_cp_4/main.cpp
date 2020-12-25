#include "RSA.h"

int main()
{
	RSA my_rsa;
	KeyPair B_pair;
	int choice;
	string input_str;

	cout << "Choose testing type:" << endl << "1. Local test" << endl << "2. Test with site" << endl;
	cin >> choice;
	if (choice == 1)
	{
		cout << endl << "--------------- Generating RSA data for Client B ---------------" << endl;
		B_pair = my_rsa.GenerateKeyPair();
		cout << "n: " << B_pair.publicPart.n << endl;
		cout << "e: " << B_pair.publicPart.e << endl;
		cout << "d: " << B_pair.privatePart.d << endl;
	}
	else
	{
		cout << "Enter public exponent: ";
		cin >> input_str;
		B_pair.publicPart.e = (uint512_t)("0x" + input_str);
		cout << "Enter modulus: ";
		cin >> input_str;
		B_pair.publicPart.n = (uint512_t)("0x" + input_str);
	}
	
	cout << "--------------- Generating RSA data for Client A ---------------" << endl;
	KeyPair A_pair = my_rsa.GenerateKeyPair();
	cout << "n: " << A_pair.publicPart.n << endl;
	cout << "e: " << A_pair.publicPart.e << endl;
	cout << "d: " << A_pair.privatePart.d << endl;

	while (A_pair.publicPart.n > B_pair.publicPart.n)					// Generete new pair if n > n1 
	{
		cout << "--------------- Re-generating RSA data for Client A ---------------" << endl;
		A_pair = my_rsa.GenerateKeyPair();
		cout << "n: " << A_pair.publicPart.n << endl;
		cout << "e: " << A_pair.publicPart.e << endl;
		cout << "d: " << A_pair.privatePart.d << endl;
	}

	cout << endl << ">>>>>>>>>>>>>>>>>>>> RSA ALGORYTHM <<<<<<<<<<<<<<<<<<<<" << endl;
	// A SIDE after receaved B_pair.publicPart
	uint512_t k = my_rsa.random_in_range<uint512_t>(1, A_pair.publicPart.n);

	Message msg_to_B = my_rsa.GenerateMessage(k, A_pair, B_pair.publicPart);
	cout << "Sended message from A -----------------------" << endl;
	cout << "k1:\t\t" << hex << msg_to_B.data << endl;
	cout << "S1:\t\t" << hex << msg_to_B.Sign << endl;
	cout << "Public key A:\tn = " << hex << msg_to_B.publicKey.n << endl << "\t\te = " << hex << msg_to_B.publicKey.e << endl;
	cout << "---------------------------------------------" << endl << endl;

	if (choice == 1)
	{
		// B SIDE
		uint512_t recieved_k = my_rsa.RecieveMessage(msg_to_B, B_pair);
		cout << "Recieved message to B -----------------------" << endl;
		cout << "k:\t\t" << recieved_k << endl;
		if (recieved_k == k)
		{
			cout << "Data is decrypted properly!" << endl;
		}
		else
		{
			cout << "Data NOT decrypted properly(" << endl;
		}
		cout << "---------------------------------------------" << endl;
	}
	else
	{
		cout << "Input message at site to verify" << endl;
	}
	cout << endl << ">>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<" << endl;
	system("pause");
	return 0;
}