use crate::rsa::*;
use num::{bigint::*, Zero};

#[derive(Default, Debug)]
pub struct Server {
    rsa: Option<Rsa>,
}
impl Server {
    #[allow(non_snake_case)]
    pub fn Encrypt(public: &Key, text: &BigUint) -> BigUint {
        public.transform(text)
    }
    #[allow(non_snake_case)]
    pub fn Sign(&self, text: &BigUint) -> Option<BigUint> {
        self.rsa.as_ref().map(|rsa| rsa.secret.transform(text))
    }
    #[allow(non_snake_case)]
    pub fn Verify(public: &Key, data: &BigUint, signature: &BigUint) -> bool {
        *data == public.transform(signature)
    }
    #[allow(non_snake_case)]
    pub fn GenerateKeyPair(&mut self, bit_size: u32) -> Key {
        let rsa = Rsa::new(bit_size);
        let ret = rsa.public.clone();
        self.rsa = Some(rsa);
        ret
    }
    #[allow(non_snake_case)]
    pub fn Decrypt(&self, text: &BigUint) -> Option<BigUint> {
        self.rsa.as_ref().map(|rsa| rsa.secret.transform(text))
    }
    #[allow(non_snake_case)]
    pub fn RecieveKey(&self, key: &BigUint, sign: &BigUint, public: &Key) -> Option<BigUint> {
        let key_decr = self.Decrypt(key)?;
        let sign_decr = self.Decrypt(sign)?;
        if Self::Verify(public, &key_decr, &sign_decr) {
            Some(key_decr)
        } else {
            None
        }
    }
    #[allow(non_snake_case)]
    pub fn SendKey(&self, public: &Key) -> Option<(BigUint, BigUint)> {
        //key,sign
        let mut rng = rand::thread_rng();
        let k = rng.gen_biguint_range(&BigUint::zero(), &BigUint::from(2u8).pow(64));
        println!("отправленный ключ: {}", to_str(&k));
        let sign = self.Sign(&k)?;
        let k_enc = Self::Encrypt(public, &k);
        let sign_enc = Self::Encrypt(public, &sign);

        Some((k_enc, sign_enc))
    }
}
