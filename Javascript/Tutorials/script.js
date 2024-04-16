
// //! basics

// //? for printing anything in the console window we use

// console.log("Hello, world!");
// console.log("This is a script file.");

// //* for showing an alert message we use
// // window.alert("This is an alert.");

// // This is a comment.

// /* This is a multi-line
// comment. */

// //? for changing the text content of an element
// document.getElementById("myh1").textContent = "Hello, world!";
// document.getElementById("myp").textContent = " This is a paragraph.";


// //! Variables

// //* declaring a variable and assigement of a varible

// let x = 100;
// console.log(x); // prints the x value


// //? bio data of a user

// let name = "Varun";
// let age = 20;
// let city = "Noida";
// let food = "chole bhature"
// let email = "imnotvarun@gmail.com"

// console.log(`Your Name is ${name}\nYou are ${age} old\nYou are from ${city} \nYour favorite food is ${food}\nContact on ${email}`)

// //! boolean
// let name1 = true
// if (name1 = true) {
//     console.log(`Hello ${name}`)
// }

// //? example
// document.getElementById("myh1").textContent = `Hello ,${name}`;
// document.getElementById("myp").textContent = `My Name is ${name} and i am ${age} old , I am from ${city} and i like to eat ${food} , if you want to contact me please dia anything on this mail ${email}`


// //! accepting User Input

// //? Easy way using window prompt

// let Username = window.prompt("whar is Your Username");

// document.getElementById("username").textContent = `Hello ,${Username}`;
// document.getElementById("usernamep").textContent = `My Name is ${Username}`;

// //? Professional Way to do it

// let myname;

// document.getElementById("button").onclick = function () {
//     myname = document.getElementById("mynamee").value;
//     document.getElementById("user").textContent = `Hello ,${myname}`;
//     document.getElementById("userr").textContent = `My Name is ${myname}`;
// }


// // ! type convertion

// let age = window.prompt("What is your age :");
// age = Number(age);
// age += 1;
// console.log(age, typeof age);

// //? converting types
// let x = "Say my Name";
// let y = 10;
// let z = "hello";

// x = Number(x);
// y = String(y);
// z = Boolean(z);

// console.log(x, typeof x, y, typeof y, z, typeof z);

// //todo using const to find the radius of a circle

// const pi = 3.14159;
// let radius;
// let circumference;

// radius = Number(window.prompt("Enter the radius of a circle"));
// circumference = 2 * pi * radius;
// console.log(circumference);


// //! If statements

// let name = window.prompt("What is your name?");

// if (name == "varun") {
//     document.getElementById("h3").textContent = "Hello, Varun!";
// } else {
//     document.getElementById("h3").textContent = "Hello, stranger!";

// }