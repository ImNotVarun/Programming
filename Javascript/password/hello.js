const passwordLength = document.getElementById("password-length");
const uppercase = document.getElementById("include-uppercase");
const numbers = document.getElementById("include-numbers");
const specialCharacters = document.getElementById("include-special-characters");
const generateBtn = document.getElementById("generate-password");

function generatePassword() {
    let password = "";
    const passwordLen = parseInt(passwordLength.value);

    const uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lowercaseLetters = "abcdefghijklmnopqrstuvwxyz";
    const numericCharacters = "0123456789";
    const specialChars = "!@#$%^&*()_+";

    let characters = lowercaseLetters; // Default to lowercase letters

    if (uppercase.checked) {
        characters += uppercaseLetters;
    }
    if (numbers.checked) {
        characters += numericCharacters;
    }
    if (specialCharacters.checked) {
        characters += specialChars;
    }

    for (let i = 0; i < passwordLen; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters.charAt(randomIndex);
    }

    document.getElementById("generated-password").textContent = password;
} 12