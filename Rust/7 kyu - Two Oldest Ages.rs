// https://www.codewars.com/kata/511f11d355fe575d2c000001/train/rust
// My solution
fn two_oldest_ages(ages: &[u8]) -> [u8; 2] {
  let mut idx1 = 0;
  let mut idx2 = 1;
 
  if ages[0] < ages[1] {
      idx1 = 1;
      idx2 = 0;
  }

  for i in 0..ages.len() {
      let xi = ages[i];
      if xi > ages[idx1] {
          idx2 = idx1;
          idx1 = i;
      }
      if xi > ages[idx2] && i != idx1 {
          idx2 = i;
      }
  }
  
  [ages[idx2], ages[idx1]]
}

// ...
fn two_oldest_ages(ages: &[u8]) -> [u8; 2] {
  let mut ages = ages.to_vec();
  ages.sort();
  
  [ages[ages.len() - 2], ages[ages.len() - 1]]
}

// ...
fn two_oldest_ages(ages: &[u8]) -> [u8; 2] {
  let mut p: [u8; 2] = [0, 0];
  for &k in ages {
    if k > p[0] {            
      if k > p[1] {
        p[0] = p[1];
        p[1] = k;                
      } else {
        p[0] = k;
      }
    }                
  }
  p
}

// ...
fn two_oldest_ages(ages: &[u8]) -> [u8; 2] {
  let mut all:Vec<&u8> = ages.iter().collect();
  all.sort();
  let fm = *all.pop().unwrap();
  let sm = *all.pop().unwrap();
  [sm,fm]
}