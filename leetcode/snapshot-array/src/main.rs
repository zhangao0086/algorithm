struct SnapshotArray {
    snapshots: Vec<Vec<(i32, i32)>>,
    snap_id: i32,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {

    fn new(length: i32) -> Self {
        Self {
            snapshots: vec![vec![(0, 0)]; length as usize],
            snap_id: 0
        }
    }
    
    fn set(&mut self, index: i32, val: i32) {
        if self.snapshots[index as usize].last().unwrap().0 == self.snap_id {
            self.snapshots[index as usize].pop();
        }
        self.snapshots[index as usize].push((self.snap_id, val));

    }
    
    fn snap(&mut self) -> i32 {
        self.snap_id += 1;
        self.snap_id - 1
    }
    
    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let res = self.snapshots[index as usize].binary_search(&(snap_id, i32::MAX));
        match res {
            Ok(pos) => self.snapshots[index as usize][pos].1,
            Err(pos) => self.snapshots[index as usize][pos - 1].1
        }
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */

fn main() {
    let mut obj = SnapshotArray::new(3);
    obj.set(0,5);  // Set array[0] = 5
    assert_eq!(obj.snap(), 0);  // Take a snapshot, return snap_id = 0
    obj.set(0,6);
    assert_eq!(obj.get(0,0), 5);  // Get the value of array[0] with snap_id = 0, return 5
}
