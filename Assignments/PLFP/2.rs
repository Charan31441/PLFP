use std::io;
fn main()
{
	let  mut  i=0;
	let mut j=0;
	let mut bin_rev=0;
	let mut bin=0;
	let mut n=10;

	i=1;
	let mut done=false;
	while !done{
		bin_rev=bin_rev+(n%2)*i;
		i=i*10;
		n=n/2;
		if n==0{
			done=true;
		}
	}

	i=1;
	done = false;
	while !done {
		bin=bin+(bin_rev%10)*i;
		i=i*10;
		bin_rev=bin_rev/10;
		if bin_rev == 0{
			done=true;
		}
	}
	println!("{}",bin);
}
