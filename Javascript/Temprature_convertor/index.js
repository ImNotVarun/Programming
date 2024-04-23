const input = document.getElementById('input');
const submit = document.getElementById('submit');
const celsiusToFahrenheit = document.getElementById('celsiusToFahrenheit');
const fahrenheitToCelsius = document.getElementById('fahrenheitToCelsius');
const Result = document.getElementById('Result');

submit.onclick = function () {
    if (celsiusToFahrenheit.checked) {
        let tem = (input.value * 9 / 5) + 32;
        Result.textContent = `${tem.toFixed(2)}F`;
    }
    else if (fahrenheitToCelsius.checked) {
        let tem = (input.value - 32) * 5 / 9;
        Result.textContent = `${tem.toFixed(2)}C`;
    }
    else {
        Result.textContent = " You didn't pass a value or not select the convertion type"
    }
}