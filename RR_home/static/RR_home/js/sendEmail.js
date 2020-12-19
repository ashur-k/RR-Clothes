function sendMail(contactForm) {
    emailjs.send('service_yqym4xn', "rr_cloth", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "project_request": contactForm.message.value
    },"user_34NOIeNB8cZcERXuSYCFJ")
    .then(
        function(response) {
            console.log("SUCCESS", response);
            var element = document.getElementById("sendEmailSuccess");
            element.classList.add("d-block");
        },
        function(error) {
            console.log("FAILED", error);
             var element = document.getElementById("sendEmailFail");
            element.classList.add("d-block");
        }
    );
    return false;  // To block from loading a new page
}