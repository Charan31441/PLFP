use std::io;
fn main()
{
	let mut x=3;
	let mut y=2;
	let mut z=5;
	let mut ans=1;
	for i in 0..y
	{
		ans=ans*x;
	}
	ans= ans % z;
	println!("{}",ans);
}
