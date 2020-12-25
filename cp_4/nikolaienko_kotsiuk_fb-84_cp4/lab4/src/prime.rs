use num::{bigint::*, One, Zero};

fn check_div2357(n: &BigUint) -> bool {
    fn sum(n: &BigUint) -> BigUint {
        let mut temp = n.clone();
        let mut s = BigUint::zero();
        while temp > BigUint::zero() {
            s += &temp % 10u8;
            temp /= 10u8;
        }
        s
    }
    ((n % 10u8) % 2u8 == BigUint::zero())
        || (sum(n) % 3u8 == BigUint::zero())
        || ((n % 10u8) == BigUint::zero() || (n % 10u8) == BigUint::from(5u8))
}

fn is_prime(n: &BigUint, k: u16) -> bool {
    for i in &[1u8, 2, 3, 5] {
        if *n == BigUint::from(*i) {
            return true;
        }
    }
    if check_div2357(&n) {
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


pub fn get_rand_prime(bit_size:u32)->BigUint{
    let n1 = BigUint::from(2u8).pow(bit_size);
    let n0 = BigUint::from(2u8).pow(bit_size-1);
    let mut rng = rand::thread_rng();
    let x = rng.gen_biguint_range(&n0, &n1);
    let m0 = if &x%2u8 != BigUint::zero() {x} else {x+1u8};
    let mut i = BigUint::from(1u8);
    while i<=((&n1-&m0)/2u8){
        let candidate = &m0+2u8*&i;
        if is_prime(&candidate, 10){
            return candidate;
        }
        i+=1u8;
    }
    BigUint::zero()
}


fn reverse(mut x: i32, m: i32) -> Option<i32> {
    let mut y = m;
    let mut coefs: Vec<(i32, i32)> = vec![];
    while x != 0 {
        coefs.push((x, y));
        let temp_x = x;
        x = y.rem_euclid(x);
        y = temp_x;
    }
    if y != 1 {
        //gcd != 1
        None
    } else {
        for (a, b) in coefs.iter().rev() {
            let temp_x = x;
            x = y - (b / a) * x;
            y = temp_x;
        }
        Some(x.rem_euclid(m))
    }
}