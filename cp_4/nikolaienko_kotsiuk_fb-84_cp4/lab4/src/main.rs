
mod rsa;
mod utils;

use rsa::*;

mod interface;
use interface::*;



fn main() {
    let mut a = Server::default();
    let mut b = Server::default();
    let a_pub = a.GenerateKeyPair(256);
    let b_pub = b.GenerateKeyPair(256);
    println!("A {:#?}", a);
    println!("B {:#?}", b);
    let (encr_key, sign) = a.SendKey(&b_pub).unwrap();
    println!("зашифрованный ключ {}, сигнатура {}", to_str(&encr_key), to_str(&sign));
    let key = b.RecieveKey(&encr_key, &sign, &a_pub).unwrap();
    println!("полученный ключ:   {}", to_str(&key));
}
