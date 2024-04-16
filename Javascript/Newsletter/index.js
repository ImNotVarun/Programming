const promotions = document.getElementById('promotions');
const updates = document.getElementById('updates');
const submit = document.getElementById('submit');
const success = document.getElementById('success-message');
const para = document.getElementById('para');
const box = document.getElementById('box');
const email = document.getElementById('email');

submit.onclick = function () {
    if (email.value != "") {
        if (promotions.checked && updates.checked && box.checked) {
            success.textContent = `Thank you for signing up!`;
            para.textContent = `You will now receive our latest Promotions and updates and we can collect telemenatry data. `;
        }
        else if (promotions.checked && updates.checked) {
            success.textContent = `Thank you for signing up!`;
            para.textContent = `You will now receive our latest Promotions and updates. `;
        }
        else if (promotions.checked && box.checked) {
            success.textContent = `Thank you for signing up!`;
            para.textContent = `You will now receive our latest Promotions and we can collect telemenatry data.`;
        }
        else if (updates.checked && box.checked) {
            success.textContent = `Thank you for signing up!`;
            para.textContent = `You will now receive our latest updates and we can collect telemenatry data. `;
        }
        else if (box.checked) {
            success.textContent = `Thank you for signing up!`;
            para.textContent = `You will now receive our latest Promotions and updates and we can collect telemenatry data. `;

        }

        else {
            success.textContent = `Getting error while Signing You In`;
        }
    }
    else {
        success.textContent = `Please Provide Your Email Address`;
    }
}