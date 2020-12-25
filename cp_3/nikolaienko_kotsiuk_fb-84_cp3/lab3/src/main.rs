#![feature(type_ascription)]
use std::{collections::*, convert::*, fs::*, io::Write};

fn main() {
    println!(
        "{:?}",
        decrypt(
            vec!["ст", "но", "то", "на", "ен"]
                .iter()
                .filter_map(|&x| Bigram::try_from(x).ok())
                .collect(),
            vec!["ве", "да", "эб", "рб", "чм"]
                .iter()
                .filter_map(|&x| Bigram::try_from(x).ok())
                .collect(),
            read_to_string("18.txt")
                .unwrap()
                .chars()
                .filter(|x| *x != '\n' && *x != '\r')
                .map(|x| if x == 'ы' {
                    'ь'
                } else if x == 'ь' {
                    'ы'
                } else {
                    x
                })
                .collect(),
            check
        )
    )
}

//'ве': 0.013176740189057576, 'да': 0.00859352621025494, 'эб': 0.008020624462904613, 'рб': 0.007734173589229447, 'чм': 0.007734173589229447,
//a = 425, b = 100
fn decrypt(no: Vec<Bigram>, yes: Vec<Bigram>, text: Vec<char>, checker: impl Fn(&String) -> bool) {
    let mut f = File::create("results").unwrap();
    for &i in &no {
        for &j in &yes {
            for &k in &no {
                for &m in &yes {
                    if i != k {
                        if let Some(v) = get_ab((i, j), (k, m)) {
                            for (a, b) in v {
                                
                                let dec = text
                                    .chunks(2)
                                    .filter_map(|x| Bigram::try_from(x).unwrap().decrypt(a, b))
                                    .map(String::from)
                                    .fold(String::new(), |acc, x| {
                                        acc + &(x
                                            .chars()
                                            .map(|x| {
                                                if x == 'ы' {
                                                    'ь'
                                                } else if x == 'ь' {
                                                    'ы'
                                                } else {
                                                    x
                                                }
                                            })
                                            .collect():String
                                        )
                                    });
                                
                                if checker(&dec) {
                                    println!("a = {}, b = {}, {:?}", a, b, &dec[..1000]);
                                } else {
                                    let slice = if dec.len() == 0 {&""} else {&dec[..1000]};
                                    f.write(
                                        format!("a = {}, b = {}, {:?}\n", a, b, slice).as_bytes(),
                                    )
                                    .unwrap();
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

fn check(s: &String) -> bool {
    let mut counter = HashMap::new();
    for c in s.chars() {
        let count = counter.entry(c).or_insert(0);
        *count += 1
    }
    let mut freqs = counter.iter().collect::<Vec<(&char, &i32)>>();
    freqs.sort_unstable_by(|x, y| y.1.cmp(x.1));
    if let [a, b, ..] = &freqs[..] {
        *a.0 == 'о' && *b.0 == 'е'
    } else {
        false
    }
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

fn gcd(mut x: i32, mut y: i32) -> i32 {
    while x != 0 {
        let temp_x = x;
        x = y.rem_euclid(x);
        y = temp_x;
    }
    y
}

fn solve(a: i32, b: i32, m: i32) -> Option<Vec<i32>> {
    let mut out = vec![];
    let d = gcd(a, m);
    if b % d != 0 {
        None
    } else {
        let sub_m = m / d;
        let res = (reverse(a, sub_m)? * b).rem_euclid(sub_m);

        for i in 0..d {
            out.push(res + (i * sub_m));
        }
        Some(out)
    }
}

#[derive(Debug, Copy, Clone)]
struct SRChar(i32);
impl SRChar {
    const SIZE: i32 = 31;
    const SIZE_SQ: i32 = 961;
}

impl TryFrom<char> for SRChar {
    type Error = &'static str;
    fn try_from(c: char) -> Result<Self, Self::Error> {
        match c {
            'а'..='я' if c != 'ъ' => {
                let shift = match c {
                    'ы'..='я' => 1073,
                    _ => 1072,
                };
                Ok(SRChar(c as i32 - shift))
            }
            _ => Err("Out of range"),
        }
    }
}

impl From<SRChar> for char {
    fn from(s: SRChar) -> char {
        let shift = match s.0 {
            26..=30 => 1073,
            _ => 1072,
        };
        std::char::from_u32(u32::try_from(s.0 + shift).unwrap()).unwrap()
    }
}

#[derive(Debug, Copy, Clone)]
struct Bigram(SRChar, SRChar);

impl Bigram {
    fn encrypt(self, a: i32, b: i32) -> Bigram {
        let num: i32 = self.into();
        ((a * num + b).rem_euclid(SRChar::SIZE_SQ)).into()
    }

    fn decrypt(self, a: i32, b: i32) -> Option<Bigram> {
        let rev = reverse(a, SRChar::SIZE_SQ)?;
        let dec = rev * (i32::from(self) - b);
        let out = dec.rem_euclid(SRChar::SIZE_SQ);
        Some(out.into())
    }
}

impl From<Bigram> for i32 {
    fn from(s: Bigram) -> i32 {
        ((s.0).0 * SRChar::SIZE) + (s.1).0
    }
}

impl From<Bigram> for String {
    fn from(s: Bigram) -> String {
        let mut out = String::new();
        out.push(char::from(s.0));
        out.push(char::from(s.1));
        out
    }
}

impl From<i32> for Bigram {
    fn from(n: i32) -> Bigram {
        let a = n / SRChar::SIZE;
        let b = n - (a * SRChar::SIZE);
        Bigram(
            SRChar(a.rem_euclid(SRChar::SIZE)),
            SRChar(b.rem_euclid(SRChar::SIZE)),
        )
    }
}

impl TryFrom<&str> for Bigram {
    type Error = &'static str;
    fn try_from(c: &str) -> Result<Self, Self::Error> {
        let s = c.chars().collect(): Vec<_>;
        Ok(Bigram(SRChar::try_from(s[0])?, SRChar::try_from(s[1])?))
    }
}

impl TryFrom<&[char]> for Bigram {
    type Error = &'static str;
    fn try_from(c: &[char]) -> Result<Self, Self::Error> {
        Ok(Bigram(SRChar::try_from(c[0])?, SRChar::try_from(c[1])?))
    }
}

impl PartialEq for SRChar {
    fn eq(&self, other: &Self) -> bool {
        self.0 == other.0
    }
}

impl PartialEq for Bigram {
    fn eq(&self, other: &Self) -> bool {
        self.0 == other.0 && self.1 == other.1
    }
}

fn get_ab((x1, y1): (Bigram, Bigram), (x2, y2): (Bigram, Bigram)) -> Option<Vec<(i32, i32)>> {
    let a = solve(
        x1.into(): i32 - x2.into(): i32,
        y1.into(): i32 - y2.into(): i32,
        SRChar::SIZE_SQ,
    )?;
    Some(
        a.iter()
            .map(|ai| {
                (
                    *ai,
                    (y1.into(): i32 - ai * x1.into(): i32).rem_euclid(SRChar::SIZE_SQ),
                )
            })
            .collect(),
    )
}
