use super::utils::*;
use num::{bigint::*};
use std::{
    convert::TryFrom,
    fmt::{Debug, Error, Formatter, Write},
};

#[derive(Clone)]
pub struct Key {
    pub exponent: BigUint,
    pub modulus: BigUint,
}
impl Key {
    pub fn transform(&self, data: &BigUint) -> BigUint {
        data.modpow(&self.exponent, &self.modulus)
    }
}

pub fn to_str(b: &BigUint) -> String {
    let mut out = String::new();
    let v = b.to_radix_be(16);
    for i in v {
        write!(out, "{:x?}", i).unwrap();
    }
    out
}

impl Debug for Key {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error> {
        f.debug_struct("Key")
            .field("exponent", &to_str(&self.exponent))
            .field("modulus", &to_str(&self.modulus))
            .finish()
    }
}

#[derive(Debug, Clone)]
pub struct Rsa {
    pub public: Key,
    pub secret: Key,
}

impl Rsa {
    pub fn new(bit_size: u32) -> Rsa {
        let q = get_rand_prime(bit_size);
        let p = get_rand_prime(bit_size);
        println!("p = {}", to_str(&p));
        println!("q = {}", to_str(&q));
        let n = &q * &p;
        let euler = (&p - 1u8) * (&q - 1u8);
        let e: BigUint = BigUint::from(2u8).pow(16) + 1u8;

        let d = reverse(BigInt::from(e.clone()), BigInt::from(euler.clone()));
        Rsa {
            public: Key {
                exponent: e.clone(),
                modulus: n.clone(),
            },
            secret: Key {
                exponent: BigUint::try_from(d).unwrap(),
                modulus: n,
            },
        }
    }
}
