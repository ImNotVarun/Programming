use std::io;

fn main() {
    function1();
    function2();
    // function3();
    adding_numbers(23, 34);
    loop {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Press x to exit the terminal");
        let input = input.trim();
        if input == "X" {
            println!("Exiting the terminal");
            break;
        } else {
            print!("You have entered wrong input {}", input);
        }
    }
}

fn function1() {
    let num: u8 = 255; // immuataable variable
    let mut num2: u8 = 255; // mutable variable
    print!("{}", num2);
    num2 = 254;
    println!("{} - {}", num, num2);
}

fn function2() {
    // &str - fixes lenght / can't be changed
    // and string are dyanamically expandeble
    let string1: &str = "Hi mom";
    let mut string: String = String::from("Hi mom");
    string.push_str(" Kya kar rahe ho");
    println!("{} - &str {}", string, string1);
}

// fn function3() {
//     // tuple - can store multiple values of different types of data
//     let student: (&str, i8, &str) = ("Varun", 20, "Male");
//     println!("{:?}", student); // the :? is used for debugging purpouses
//     println!("{} {} {}", student.0, student.1, student.2); // .0 .1 .2 are used to access the values of the tuple
// }
// // destructuring

//     let (name, age, gender) = student;
//     print!(
//         "through destructuring , name {} age {} Gender {}",
//         name, age, gender
//     );
// }

fn adding_numbers(num1: u8, num2: u8) {
    print!("{}", num1 + num2) // adding numbers
}
