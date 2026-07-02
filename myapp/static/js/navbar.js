document.addEventListener("DOMContentLoaded", function(){

    const navbar = document.querySelector(".custom-navbar");

    function toggleMenu(){
        navbar.classList.toggle("active");
    }

    // make function global (IMPORTANT)
    window.toggleMenu = toggleMenu;

    window.addEventListener("scroll", function(){
        let scroll = window.scrollY;

        if(scroll > 20){
            navbar.classList.add("expand");
        } else {
            navbar.classList.remove("expand");
        }
    });

});