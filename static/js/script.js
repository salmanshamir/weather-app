
document.addEventListener("DOMContentLoaded", function () {

    const flashMessages = document.querySelectorAll(".flash-message");

    flashMessages.forEach(function (message) {

        setTimeout(function () {
            message.style.transition = "opacity 0.4s ease, transform 0.4s ease";
            message.style.opacity = "0";
            message.style.transform = "translateY(-15px)";

            setTimeout(function () {
                message.remove();

                const overlay = document.getElementById("flashOverlay");

                if (overlay && !overlay.querySelector(".flash-message")) {
                    overlay.remove();
                }

            }, 400);

        }, 4000);

    });

});
