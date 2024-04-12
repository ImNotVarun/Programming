let userdata, userdata2, userdata3;

document.getElementById("submitBtn").onclick = function () {
    userdata = document.getElementById("name").value;
    userdata2 = document.getElementById("age").value;
    userdata3 = document.getElementById("email").value;

    console.log(`user name is ${userdata}`);
    console.log(`user age is ${userdata2}`);
    console.log(`user email is ${userdata3}`);
}