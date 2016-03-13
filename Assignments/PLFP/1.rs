use std::io;
fn main() {
 let mut num = 10;

	for x in 1..num {
		for y in 1..x{
			print!(" ");
		}
		for y in 1..(2*(num-x)){
		
			print!("*");
		}
		println!("");
	}
}

