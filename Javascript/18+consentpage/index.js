const consentbtn1 = document.getElementById("consentbtn1")
const consentbtn2 = document.getElementById("consentbtn2")
const lol = document.getElementById("lol")

consentbtn1.onclick = function () {
    const input1 = Number(window.prompt("Give me Proof that you are a Junior Developer , what is 2+2="));
    if (input1 == 4) {
        lol.textContent = "You can Proceed Now"
    }
    else {
        lol.textContent = "You Liar"
    }
}

consentbtn2.onclick = function () {
    const input2 = Number(window.prompt("Give me Proof that you are a Expert Developer , what is 2+2="));
    if (input2 == 4) {
        lol.textContent = "You can Proceed Now"
    }
    else {
        lol.textContent = "You Liar"
    }

}
