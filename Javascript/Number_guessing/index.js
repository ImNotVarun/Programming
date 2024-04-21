const predefine = Math.ceil(Math.random() * (1 - 100) + 100);
console.log(predefine);

document.getElementById("Submit").onclick = function () {
    const userInput = document.getElementById("Number").value;

    if (userInput < predefine) {
        document.getElementById("Result").textContent = "Too low try again";
    }
    else if (userInput > predefine) {
        document.getElementById("Result").textContent = "Too High try again";
    }
    else if (userInput == predefine) {
        document.getElementById("Result").textContent = "Correct Answer";
    }
    else {
        document.getElementById("Result").textContent = "Invalid Choices";

    }
}
