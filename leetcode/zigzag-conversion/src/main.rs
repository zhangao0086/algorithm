struct Solution;

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows < 2 { return s; }
        
        let num_rows = num_rows as usize;
        let s = s.as_bytes();
        let cycle_count = 2 * num_rows - 2;
        let mut ans = vec![];

        for row in 0..num_rows {
            let mut location = row;

            while location < s.len() {
                ans.push(s[location]);
    
                if row != 0 && row != num_rows - 1 {
                    let next_location = location + cycle_count - row * 2;
                    if next_location < s.len() {
                        ans.push(s[next_location]);
                    }
                }
                location += cycle_count;
            }
        }

        std::str::from_utf8(&ans).unwrap().into()
    }
}
fn main() {
    assert_eq!(Solution::convert("PAYPALISHIRING".to_string(), 3), "PAHNAPLSIIGYIR");
}
