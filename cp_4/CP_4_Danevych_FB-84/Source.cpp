#include <boost/multiprecision/cpp_int.hpp>
#include <boost/random.hpp>
#include <boost/random/random_device.hpp>
#include <fstream>

using namespace boost::multiprecision;
using namespace boost::random;



cpp_int ChooseRandomNumber(int bit)
{ 
    cpp_int max = ((cpp_int)(1)) << bit;
    cpp_int min = ((cpp_int)(1)) << bit - 1;
    cpp_int x;
            
    typedef boost::mt19937 RNGType;
    boost::random::random_device rd;
    RNGType rng(rd());
    uniform_int_distribution<cpp_int> ui(min, max);
    x = ui(rng);
   
    return x;
}

cpp_int RandomNumberWithin(cpp_int x, cpp_int y)
{
    typedef mt19937 RNGType;
    random_device rd;
    RNGType mt(rd());
    uniform_int_distribution<cpp_int> ui(x, cpp_int(y));
    return ui(mt);
}

cpp_int gcd(cpp_int a, cpp_int b)
{
    if (a != 0 && b != 0)
    {
        while (a != b)
        {
            if (a > b)
            {
                cpp_int tmp = a;
                a = b;
                b = tmp;
            }
            b = b - a;

        }
        return a;
    }
    else
        return 1;
}

cpp_int binpow(cpp_int a, cpp_int n, cpp_int m)
{
    cpp_int res = 1;
    while (n)
    {
        if (n & 1)
        {
            res *= a;
            res %= m;
        }
        a *= (a % m);
        a %= m;
        n >>= 1;
    }
    return res % m;
}

bool test(cpp_int X)
{
    std::ofstream out("test.txt", std::ios::app);
    out << "Number: " << X << std::endl;

    int mas[5] = { 2, 3, 5, 7, 11 };

    for (int i = 0; i < 5; i++)
    {
        if (X % mas[i] == 0)
        {
           out << "Ділиться націло на " << mas[i] << std::endl;
            return false;
        }
    }

    //Крок 0
    cpp_int d = X - 1, s = 0;
    while (d % 2 == 0)
    {
        d = d / 2;
        s++;
    }
    bool TF = false;
    for (int i = 0; i < 5; i++)
    {
        //Крок 1
        cpp_int x = RandomNumberWithin(2, X - 1);

        if (gcd(x, X) > 1)
            return false;

        //Крок 2
        cpp_int xd = x;

        if (binpow(x, d, X) == 1 || binpow(x, d, X) == -1)
            TF = true;
        else
        {
            for (cpp_int r = 1; r < s; r++)
            {
                TF = false;
                cpp_int step = 1, steptwo;
                for (int j = 0; j < r; j++)
                    step *= 2;
                step *= d;
                cpp_int xr = binpow(x, step, X);
                if (xr == -1)
                {
                    TF = true;
                    break;
                }
                else if (xr == 1)
                    return false;
            }
        }
    }
    if (TF == true)
    {
       out << "Просте число " << std::endl;
       out.close();
        return true;
    }
    else
    {
        out << "Закінчились ітерації " << std::endl;
        out.close();
        return false;
    }
}

cpp_int evk(cpp_int a, cpp_int m)
{
    cpp_int x = a, y = m;
    long long int size_mas = 2;
    while (x != y)
    {
        if (x > y)
        {
            cpp_int tmp = x;
            x = y;
            y = tmp;
            size_mas++;
        }
        y = y - x;
    }
    y = m;
    cpp_int* mas = new cpp_int[size_mas];

    cpp_int  c = 0; long long int i = 2;
    if (a != 0 && m != 0)
    {
        mas[0] = 0;
        mas[1] = 1;
        while (a != m)
        {
            if (a > m)
            {
                cpp_int tmp = a;
                a = m;
                m = tmp;
                mas[i] = c * (-1);
                i++;
                c = 0;
            }
            m = m - a;
            c++;
        }
        for (long long int j = 2; j < size_mas; j++)
        {
            mas[j] = mas[j] * mas[j - 1] + mas[j - 2];
        }
        a = mas[size_mas - 1];
        delete[] mas;
        while (a < 0)
            a = a + y;
        return a;
    }
    else
        delete[]mas;
    return 0;
}

void GenerateKeyPair(cpp_int mas[])
{
    cpp_int d, p, q, n, e, f;

    bool b = false;
    while (b == false)
    {
        p = ChooseRandomNumber(256);
       // std::cout << "p: " << p << std::endl;
        b = test(p);

    }
    b = false;
    while (b == false)
    {
        q = ChooseRandomNumber(256);
        //std::cout << "q: " << q << std::endl;
        b = test(q);

    }
    n = p * q;
   // std::cout << "n: " << n << std::endl;
    f = (p - 1) * (q - 1);
   // std::cout << "f: " << f << std::endl;

    do
    {
        e = RandomNumberWithin(2, f - 1);
    } while (gcd(e, f) != 1);
   // std::cout << "e: " << e << std::endl;
    d = evk(e, f);
    //std::cout << "d: " << d << std::endl;
    mas[0] = d;
    mas[1] = p;
    mas[2] = q;
    mas[3] = n;
    mas[4] = e;
    mas[5] = 0;
    mas[6] = 0;

}  

void KeyExchange(cpp_int Key[], cpp_int n, cpp_int e)
{
    Key[5] = n;
    Key[6] = e;
}

cpp_int Sign(cpp_int S, cpp_int n, cpp_int e)
{
    return binpow(S, e, n);
}

cpp_int Encrypt(cpp_int k, cpp_int e, cpp_int n)
{
     return binpow(k, e, n);
}

void Verify(cpp_int k,cpp_int S, cpp_int n, cpp_int e )
{
    cpp_int K = binpow(S, e, n);
    if (K == k)
        std::cout <<"Автентифікація пройдена успішно"<<std::endl;
    else
        std::cout << "Автентифікацію не було пройдено" << std::endl;
}

cpp_int Decrypt(cpp_int k, cpp_int d, cpp_int n)
{
    return binpow(k, d, n);
}

void SendKey(cpp_int key[], cpp_int message[])
{
    cpp_int k = 123456789;
    std::cout << "k " << k << std::endl;
    message[0] = Encrypt(k, key[6], key[5]);
    cpp_int S = binpow(k, key[0], key[3]);
    message[1] = Sign(S, key[5], key[6]);
}

void ReceiveKey(cpp_int key[], cpp_int message[], int x)
{
    cpp_int k = Decrypt(message[0], key[0], key[3]);
    cpp_int S = binpow(message[1], key[0], key[3]);
    Verify(k, S, key[5], key[6]);
    if (x == 1)
    {
        std::cout << std::hex << std::showbase;
        std::cout << "k " << k << std::endl;
    }
    else
        std::cout << "k " << k << std::endl;
}

int main()
{
   setlocale(LC_CTYPE, "rus");
    cpp_int AKey[7];
    cpp_int BKey[7];
    cpp_int message[2];
    GenerateKeyPair(AKey);
    do { GenerateKeyPair(BKey); } 
    while (AKey[3] > BKey[3]);
    KeyExchange(AKey, BKey[3], BKey[4]);
    KeyExchange(BKey, AKey[3], AKey[4]);
    std::cout << "KeyA " << std::endl;
    std::cout << "d " << AKey[0] << std::endl;
    std::cout << "p " << AKey[1] << std::endl;
    std::cout << "q " << AKey[2] << std::endl;
    std::cout << "n " << AKey[3] << std::endl;
    std::cout << "e " << AKey[4] << std::endl;
    std::cout << "nb " << AKey[5] << std::endl;
    std::cout << "eb " << AKey[6] << std::endl;
    std::cout << "KeyB " << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;

    std::cout << "d " << BKey[0] << std::endl;
    std::cout << "p " << BKey[1] << std::endl;
    std::cout << "q " << BKey[2] << std::endl;
    std::cout << "n " << BKey[3] << std::endl;
    std::cout << "e " << BKey[4] << std::endl;
    std::cout << "na " << BKey[5] << std::endl;
    std::cout << "ea " << BKey[6] << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    SendKey(AKey, message);
    std::cout << "k1 " << message[0] << std::endl;
    std::cout << "S1 " << message[1] << std::endl;
    ReceiveKey(BKey, message,0);

    cpp_int MKey[7];
    MKey[0] = 0;
    MKey[1] = 0;
    MKey[2] = 0;

    std::cin >> MKey[3];
    std::cin >> MKey[4];
    while (MKey[3] < AKey[3])
        GenerateKeyPair(AKey);
    KeyExchange(AKey, MKey[3], MKey[4]);
    KeyExchange(MKey, AKey[3], AKey[4]);
    std::cout << "KeyA " << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "d " << AKey[0] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "p " << AKey[1] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "q " << AKey[2] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "n " << AKey[3] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "e " << AKey[4] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "nm " << AKey[5] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "em " << AKey[6] << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "KeyM " << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "d " << MKey[0] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "p " << MKey[1] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "q " << MKey[2] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "n " << MKey[3] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "e " << MKey[4] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "na " << MKey[5] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "ea " << MKey[6] << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    SendKey(AKey, message);
    std::cout << std::hex << std::showbase;
    std::cout << "k1 " << message[0] << std::endl;
    std::cout << std::hex << std::showbase;
    std::cout << "S1 " << message[1] << std::endl;
    ReceiveKey(MKey, message,1);
    return 0;
}