const pi = 3.14;

document.getElementById("submit").onclick = function () {
    radius = Number(document.getElementById("input").value);
    circumference = 2 * pi * radius;
    document.getElementById("output").textContent = `circumference is ${circumference.toFixed(2)}`

}