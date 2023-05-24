 function openPhoto(event) {
            event.preventDefault();
            var modal = document.getElementById("myModal");
            var modalImg = document.getElementById("modalImg");
            var imgSrc = event.target.getAttribute("src");
            modal.style.display = "block";
            modalImg.src = imgSrc;
        }

        var span = document.getElementsByClassName("close")[0];
        span.onclick = function () {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        };