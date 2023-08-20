use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut count_table: HashMap<char, i32> = HashMap::new();
        count_table.insert('L', 0);
        count_table.insert('R', 0);

        let mut substr_counter = 0;

        for c in s.chars() {
            count_table.insert(c, count_table[&c] + 1);
            if count_table[&'L'] == count_table[&'R'] {
                substr_counter += 1;
            }
        }

        substr_counter
    }
}

fn main() {
    assert_eq!(Solution::balanced_string_split("RLRRLLRLRL".to_string()), 4);
}
