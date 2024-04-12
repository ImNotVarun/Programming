document.getElementById("submit").onclick = function () {
    let startnum = Number(document.getElementById("NUM1").value);
    let endnum = Number(document.getElementById("NUM2").value);
    let randomNUM = Math.floor(Math.random() * (startnum - endnum) + endnum);
    document.getElementById("RandomNum").textContent = randomNUM;
}