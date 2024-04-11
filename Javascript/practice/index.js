let userdata;

document.getElementById("submitBtn").onclick = function () {
    userdata = document.getElementById("name").value;
    userdata = document.getElementById("age").value;
    userdata = document.getElementById("email").value;

    console.log(`user data is ${userdata}`);
}