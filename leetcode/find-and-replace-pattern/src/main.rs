use std::{collections::HashMap};

struct Solution();

impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        let pattern = pattern.as_bytes();

        fn is_match(word: &[u8], pattern: &[u8]) -> bool {
            let mut map1 = HashMap::<u8, u8>::new();
            let mut map2 = HashMap::<u8, u8>::new();
            for i in 0..word.len() {
                map1.entry(word[i]).or_insert(pattern[i]);
                map2.entry(pattern[i]).or_insert(word[i]);
                
                if map1.get(&word[i]).unwrap() != &pattern[i] || map2.get(&pattern[i]).unwrap() != &word[i] {
                    return false;
                }
                
            }
            true
        }

        words.into_iter().filter(|word| is_match(word.as_bytes(), pattern)).collect()
    }
}

fn main() {
    let source = vec![String::from("dkd"),String::from("ccc")];
    // let source = vec![String::from("abc"),String::from("deq"),String::from("mee"),String::from("aqq"),String::from("dkd"),String::from("ccc")];
    let pattern = String::from("abb");
    let expect = vec![String::from("mee"),String::from("aqq")];

    let ans = Solution::find_and_replace_pattern(source, pattern);
    assert!(ans == expect);
}