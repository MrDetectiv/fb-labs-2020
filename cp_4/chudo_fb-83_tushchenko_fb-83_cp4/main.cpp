#include "func.h"

int main()
{
		size_t gen_sz;

		cout << "Enter generator size:	" << endl;
		cin >> gen_sz;
		cout << endl << endl;




	Pers Chris(gen_sz);
	cout << "***************************************************************************" << endl;
	cout << endl << "Chris" << endl;
	Chris.printpublickey();
	cout  << "---------------" << endl;
	Chris.printprivatekey();
	cout << "***************************************************************************" << endl;
	cout << endl << endl;
	pair <cpp_int, cpp_int> chris_key = Chris.getpublickey();

	Pers Den(gen_sz);
	cout << "***************************************************************************" << endl;
	cout << endl << "Den" << endl;
	Den.printpublickey();
	cout  << "---------------" << endl;
	Den.printprivatekey();
	cout << "***************************************************************************" << endl;
	cout << endl << endl;
	pair <cpp_int, cpp_int> den_key = Den.getpublickey();

	cpp_int message = 0x123456;
	pair<cpp_int, cpp_int> chrissign = Chris.sign_message(message);
	cout << "Chris signes a message" << endl;
	cout << "(" << message << ", " << chrissign.second << ")" << endl;
	cout << "Den verifies Chris` signature" << endl;
	Den.check_signature(chrissign.first, chrissign.second, chris_key);
	cout << endl << endl;

	cout << "Chris encodes a message for Den" << endl;
	cpp_int d_enc = Chris.encrypt(message, den_key);
	cout << "Encoded message:	" << d_enc << endl;
	cout << "Den decodes message" << endl;
	cpp_int d_dec = Den.decrypt(d_enc);
	cout << "Decoded message:	" << d_dec << endl << endl;


	cpp_int k = 0x21122019;
	cout << "Chris sends key "<< k << " to Den" << endl;
		pair<cpp_int, cpp_int> sentkey = Chris.RSA_sender(Den, k);
	cout << "Chris` message:	(" << sentkey.first << ", " << sentkey.second << ")" << endl;
	cout << "Den receives key" << endl;
	cpp_int rec_k = Den.RSA_reciever(Chris, sentkey.first, sentkey.second);
	cout << "Den received key " << rec_k << endl << endl;




	//pair<cpp_int, cpp_int> servk = Server.getpublickey();
	//pair<cpp_int, cpp_int> chrisk = Chris.getpublickey();
	
	/*			//decrypt
	cout << endl << "Encryption" << endl;
	cpp_int mes = 0x12345;
	cout << "Message: " << mes << endl;
	cpp_int encr = Server.encrypt(mes, chrisk);
	cout <<"Encrypted by Server: " << encr << endl;
	cout << "Decryption by Chris" << endl;
	cpp_int decr = Chris.decrypt(encr);
	cout << "Message: " << decr << endl;
	

			//encrypt
	cout << endl << "Encryption for Server" << endl;
	cout << "Message: " << mes << endl;
	cpp_int serv_encr = Chris.encrypt(mes, servk);
	cout << "Encrypted by Chris: " << hex << serv_encr << endl;

		//server ReceiveKey
	cout << endl << "Sending key for server:" << endl;
	cout << "Original key: " << mes << endl;
	pair< cpp_int, cpp_int> sentkey = Chris.RSA_sender(Server, mes);
	cout << "Sent key:" << sentkey.first << endl;
	cout << "Sent key signature: " << sentkey.second << endl;


		//server SendKey
/*	cout << endl << "Receiving key from Server" << endl;
	cpp_int k, S;
	cout << "Enter key:	";
	cin >> hex >> k;
	cout << endl << "Enter signature:	";
	cin >> hex >> S;
	cpp_int key = Chris.RSA_reciever(Server, k, S);
	cout << endl << "Received key:	" << key << endl;*/


	return 0;
}