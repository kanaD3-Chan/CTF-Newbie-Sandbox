use std::io::{self, Write};

fn check(s: &str) -> bool {
    let enc: [u8; 28] = [
        0xa5, 0xaf, 0xa2, 0xa4, 0xb8, 0xb1, 0xb6, 0xf6,
        0xb7, 0x9c, 0xb1, 0xf0, 0xb5, 0xf0, 0xb1, 0xb0,
        0xf0, 0x9c, 0xb4, 0xf2, 0xb7, 0xab, 0x9c, 0xa4,
        0xa7, 0xa1, 0x9c, 0xbe,
    ];
    let key: u8 = 0xc3;
    if s.len() != 28 { return false; }
    for (i, c) in s.bytes().enumerate() {
        if c ^ key != enc[i] { return false; }
    }
    true
}

fn main() {
    print!("Enter the flag: ");
    io::stdout().flush().unwrap();
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let input = input.trim();
    if check(input) {
        println!("Correct!");
    } else {
        println!("Wrong!");
    }
}
