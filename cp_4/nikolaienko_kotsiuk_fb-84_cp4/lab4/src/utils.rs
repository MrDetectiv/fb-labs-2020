use num::{bigint::*, Integer, One, Zero};
use std::{ops::*};
use super::rsa::*;

fn check_div2357<T>(n: &T) -> bool
where
    T: Zero + Clone + Ord + DivAssign<u8> + AddAssign<T> + Rem<u8, Output = T> + From<u8>,
    for<'a> &'a T: Rem<u8, Output = T>,
{
    fn sum<T>(n: &T) -> T
    where
        T: Zero + Clone + Ord + DivAssign<u8> + AddAssign<T>,
        for<'a> &'a T: Rem<u8, Output = T>,
    {
        let mut temp = n.clone();
        let mut s = T::zero();
        while temp > T::zero() {
            s += &temp % 10u8;
            temp /= 10u8;
        }
        s
    }
    ((n % 10u8) % 2u8 == T::zero())
        || (sum(n) % 3u8 == T::zero())
        || ((n % 10u8) == T::zero() || (n % 10u8) == T::from(5u8))
}

fn is_prime(n: &BigUint, k: u16) -> bool {
    for i in &[1u8, 2, 3, 5] {
        if *n == BigUint::from(*i) {
            return true;
        }
    }
    if check_div2357(n) {
        return false;
    }
    let until: BigUint = n - 1u8;
    let mut s = 0;
    let mut t = until.clone();
    while &t % 2u8 == BigUint::zero() {
        t /= 2u8;
        s += 1;
    }
    let mut rng = rand::thread_rng();
    'A: for _ in 0..k {
        let a = rng.gen_biguint_range(&BigUint::from(2u8), &until);
        let mut x = a.modpow(&t, &n);
        if x == BigUint::one() || x == until {
            continue 'A;
        }
        for _ in 0..s - 1 {
            x = x.modpow(&BigUint::from(2u8), &n);
            if x == BigUint::one() {
                return false;
            }
            if x == until {
                continue 'A;
            }
        }
        return false;
    }
    true
}

pub fn get_rand_prime(bit_size: u32) -> BigUint {
    let n1 = BigUint::from(2u8).pow(bit_size);
    let n0 = BigUint::from(2u8).pow(bit_size - 1);
    let mut rng = rand::thread_rng();
    let x = rng.gen_biguint_range(&n0, &n1);
    let m0 = if &x % 2u8 != BigUint::zero() {
        x
    } else {
        x + 1u8
    };
    let mut i = BigUint::from(1u8);
    while i <= ((&n1 - &m0) / 2u8) {
        let candidate = &m0 + 2u8 * &i;
        if is_prime(&candidate, 10) {
            return candidate;
        } else {
            println!("кандидат провалил тест на простоту {}", to_str(&candidate));
        }
        i += 1u8;
    }
    BigUint::zero()
}

pub fn reverse(mut x: BigInt, m: BigInt) -> BigInt {
    let mut y = m.clone();
    let mut coefs: Vec<(BigInt, BigInt)> = vec![];
    while x != BigInt::zero() {
        coefs.push((x.clone(), y.clone()));
        let temp_x = x.clone();
        x = y.mod_floor(&x);
        y = temp_x;
    }

    for (a, b) in coefs.iter().rev() {
        let temp_x = x.clone();
        x = y - (b / a) * x;
        y = temp_x;
    }
    x.mod_floor(&m)
}
