fn fibonacci(n: u32) -> u32 {
    if n <= 1 {
        return n;
    }
    fibonacci(n - 1) + fibonacci(n - 2)
}

fn main() {
    let num = 10;
    println!("Fibonacci sequence up to {} terms:", num);
    for i in 0..num {
        println!("{}", fibonacci(i));
    }
}