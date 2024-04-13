document.getElementById("consentbtn1").onclick = function () {
    const input1 = Number(window.prompt("Give me Proof that you are a Junior Developer , what is 2+2="));
    if (input1 == 4) {
        document.getElementById("lol").textContent = "You can Proceed Now"
    }
    else {
        document.getElementById("lol").textContent = "You Liar"
    }
}

document.getElementById("consentbtn2").onclick = function () {
    const input2 = Number(window.prompt("Give me Proof that you are a Expert Developer , what is 2+2="));
    if (input2 == 4) {
        document.getElementById("lol").textContent = "You can Proceed Now"
    }
    else {
        document.getElementById("lol").textContent = "You Liar"
    }

}
